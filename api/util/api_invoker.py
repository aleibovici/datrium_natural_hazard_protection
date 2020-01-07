#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2017 Datrium, Inc. All rights reserved. *
#*                -- Datrium Confidential --                  *
#**************************************************************
import logging
import requests
import sys
from datrium.rpc.client.method_not_found_exception import MethodNotFoundException
from datrium.rpc.client.authentication_failed_exception import AuthenticationFailedException
from datrium.rpc.client.dvx_exception import DvxException
from datrium.rpc.client.rpc_client_adapter import RPCClientAdapter
from datrium.rpc.client.service_not_found_exception import ServiceNotFoundException
from google.protobuf.descriptor import ServiceDescriptor
from random import randint
from IDL.Protos.Extensions.APIException_pb2 import DvxException as BaseException
from requests.adapters import HTTPAdapter
from requests.packages import urllib3

if hasattr(urllib3, 'disable_warnings'):
    urllib3.disable_warnings()

# Create a mapping in CustiomOptions.proto
http_requests = {
                  0 : 'GET',
                  1 : 'PUT',
                  2 : 'POST',
                  3 : 'DELETE',
                  4 : 'HEAD'
                }
REQ_ID_HEADER = "X-Datrium-Request-ID"
AUTH_KEY_HEADER = "X-DatriumAuthKey"
USE_PB_SERIALIZER_HEADER = "X-Datrium-Use-PB"
CONTENT_TYPE = "application/octet-stream"

logger = logging.getLogger('api_invoker')


def parse_rest_method(md):
    """
    Parses rest method options.
    """
    if not md.has_options:
        return
    path = None
    http_request_type = None
    mo = md.GetOptions()
    fields = mo.ListFields()
    assert fields
    for _, da_msg_opt in fields:
        rest = da_msg_opt.rest
        assert rest is not None
        path = rest.path
        assert path
        http_request_type = rest.requestType

    query_params = []
    itd = md.input_type
    for fi in itd.fields:
        if fi.has_options:
            of = fi.GetOptions().ListFields()
            for _, da_msg_opt in of:
                rest = da_msg_opt.rest
                if rest:
                    if rest.queryParam:
                        query_params.append(fi.name)

    return path, http_request_type, query_params


def get_rest_service_path(descriptor):
    """
    Helper function to figure out if a service has a rest mapping.
    """
    if not isinstance(descriptor, ServiceDescriptor):
        return
    if descriptor.has_options:
        mo = descriptor.GetOptions()
        fields = mo.ListFields()
        for _, da_msg_opt in fields:
            rest = da_msg_opt.rest
            if rest:
                path = rest.path
                return path
    return None


class ApiInvoker(RPCClientAdapter):
    """
    Rest Adapter for RPC
    """
    def __init__(self, user_name=None, password=None):
        self._logger = logging.getLogger(__name__)

        self._HEADER_TEMPLATE = {
                                 REQ_ID_HEADER : None,
                                 USE_PB_SERIALIZER_HEADER : "True",
                                 "content-type" : CONTENT_TYPE
                                 }

        from base64 import b64encode
        user_pass = b64encode((user_name + ':' + password).encode("utf-8")).decode("ascii")
        self._HEADER_TEMPLATE.update(
            {
                'Authorization' : 'Basic %s' %  user_pass
            }
        )
        self.session = requests.Session()
        self.session.mount('https://', HTTPAdapter())

    def get_rest_endpoint(self, ip):
        """ Gets the SysMgmt server endpoint.
            @return: REST endpoint url
        """
        return 'https://%s/api' % ip

    def _get_http_request_path(self, interface, md, args, endpoint):
        """ Constructs the REST request path from the interface and the methods and the args.

            @param  interface : The service on which the rest call is being made.
                                Its DESCRIPTOR is used to make up the path
            @param md: The DESCRIPTOR for the remote method.
            @param args: The arguments to the method.
                         The path is populated if needed from the args.
            @param endpoint: The ip on which the rest call needs to be made

            @return: A Tuple of the HTTP request type and the path to make the request on
        """
        service_path = get_rest_service_path(interface.DESCRIPTOR)
        assert service_path is not None
        method_path, http_request_type, query_params = parse_rest_method(md)

        # Method path in the .proto file is of the form e.g. "/{name}/enable",
        # where {name} should be replaced by the value of
        # req.name. Conveniently, this is the same format that string.format()
        # takes.
        fields_by_name = dict((field_desc.name, value) for field_desc, value in args.ListFields())

        try:
            path = method_path.format(**fields_by_name)
        except KeyError as keyError:

            # Support both /resource and /resource/{id}
            loc = method_path.rfind("/{%s}" % (keyError.args[0]))
            if loc >= 0:
                path = method_path[:loc]
            else:
                raise

        query_params_path = ''
        # Now do the query params
        for qp in query_params:
            if hasattr(args, qp):
                val = getattr(args, qp)
                if val:
                    for fi in md.input_type.fields:
                        if fi.name == qp:
                            if fi.label == fi.LABEL_REPEATED:
                                for v in val:
                                    query_params_path += '%s=%s&' % (qp, v)
                            else:
                                query_params_path += '%s=%s&' % (qp, val)
        if '&' in query_params_path:
            query_params_path = query_params_path[:-1]
        if query_params_path:
            path += '?' + query_params_path

        final_path = '%s%s%s' % (endpoint, service_path, path)
        return http_requests[http_request_type], final_path

    def invoke_method(self, interface, instance_id, md, args, endpoint=None,
                        timeout=600, auth_key=None):
        """
        REST method invocation.
        The path for the rest call is looked up by the path specified in the
        descriptor for the service.
        The http method is also looked up using the same.
        The args are serialized using protocol buffers and sent in the body.
        The response is expected to be serialized protocol buffer.
        """
        self._logger.debug("Invoking rest method %s on interface %s" % (md.name,
                                                                        interface.DESCRIPTOR.full_name))
        rest_endpoint = self.get_rest_endpoint(endpoint)
        self._logger.debug("Http Server endpoint is %s" % rest_endpoint)
        http_request_type, final_path = self._get_http_request_path(interface, md, args, rest_endpoint)
        req_id = randint(0, sys.maxsize)

        # Copy the headers to avoid interfering with other requests.
        headers = dict(self._HEADER_TEMPLATE)
        headers[REQ_ID_HEADER] = str(req_id)
        if auth_key:
            headers[AUTH_KEY_HEADER] = auth_key
        self._logger.debug("Making http %s call on path %s with request id %s" % (http_request_type,
                                                                                  final_path,
                                                                                  req_id))
        response = None
        if http_request_type == 'POST':
            response =\
                self.session.post(final_path, data=args.SerializeToString(), headers=headers, timeout=timeout, verify=False)
        elif http_request_type == 'GET':
            response =\
                self.session.get(final_path, headers=headers, timeout=timeout, verify=False)
        elif http_request_type == 'PUT':
            response =\
                self.session.put(final_path, data=args.SerializeToString(), headers=headers, timeout=timeout, verify=False)
        elif http_request_type == 'DELETE':
            response =\
                self.session.delete(final_path, headers=headers, timeout=timeout, verify=False)
        else:
            raise NotImplementedError()

        if response.status_code == 200:
            self._logger.debug("Received successful response for request id %s" % req_id)
            md_instance = interface.GetResponseClass(md)()
            md_instance.ParseFromString(response.content)
            return md_instance, None
        elif response.status_code == 500:
            ex = BaseException()
            ex.ParseFromString(response.content)

            self._logger.debug("Received exceptional response for request id %s" % req_id)
            return None, DvxException(ex.errorCode, ex.errorMsg)
        elif response.status_code == 404:
            self._logger.debug("Received service not found for request id %s" % req_id)
            return None, ServiceNotFoundException(interface.DESCRIPTOR.full_name)
        elif response.status_code == 405:
            self._logger.debug("Received method not found for request id %s" % req_id)
            return None, MethodNotFoundException("%s" % md.name)
        elif response.status_code == 401:
            self._logger.debug("Authentication failed for request id %s" % req_id)
            return None, AuthenticationFailedException()
        else:
            assert False, "Error code %s not handled" % response.status_code

    def disconnect(self):
        pass
