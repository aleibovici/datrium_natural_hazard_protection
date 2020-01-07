#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2017 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************
import sys
import types
import time
from datrium.exception import DaException
from IDL.Protos.Extensions.Exception_pb2 import DaExceptionRpcServiceNotHere, DaExceptionRpcTimeout

class StubImpl:
    """ Proxy class for all remote calls to the server.
        This class intercepts all method calls and then forwards
        the call to the underlying transport to send over to the server
    """

    def __init__(self, iface, instance_id, rpc_client_adapter, endpoint=None,
                 timeout=None, auth_key=None):
        """ Constructor

            @param iface: The remote interface for which this stub is being used
            @param instance_id: Remote instance ID for this stub
            @param rpc_client_adapter: The client adapter through which remote
                                       calls are made
            @param timeout: An optional timeout for this stub, which will override the global timeout.
        """
        assert rpc_client_adapter
        assert iface

        self._iface = iface
        self._rca = rpc_client_adapter
        self._endpoint = endpoint
        self._instance_id = instance_id
        self._timeout = timeout
        self._auth_key = auth_key

    def __getattr__(self, name):
        """ Intercepts call for get method and creates a dummy method
            on which the client can make the call.
            TODO (ssen) do we need to validate that this is a query
            for a method.
            Since our services do not have properties, I am not sure that
            is necessary

            @param name: Name of the property; in this case this is a method
        """
        return types.MethodType(self, name)

    def __call__(self, *args):
        """ Intercepts all method calls and then transforms it to an actual
            remote call using the rpc_client_adapter. The variable arguments
            contain the name of the method and its arguments

            @param args[0]: Name of the method
            @param args[1]: Arguments of the method

            @return: The return value of the method call
        """
        if len(args) > 3 or len(args) < 2:
            raise Exception('Invalid method call, with bad args')
        method = args[0]
        param = args[1]
        pb_method = method
        md = self._iface.DESCRIPTOR.FindMethodByName(method)
        assert not md == None, "Method %s not found" % pb_method
        param_class = self._iface.GetRequestClass(md)
        assert isinstance(param, param_class), \
            "Argument type mismatch. Expected %s, found %s" % (param_class.__name__, type(param).__name__)

        now = time.time()
        end_time = sys.float_info.max if self._timeout is None else now + self._timeout
        while now < end_time:
            # For MAC OSX if requests have huge timeout values, it gives connection error.
            # Specify no timeout instead.
            ret_val, exception = self._rca.invoke_method(self._iface,
                                                         self._instance_id,
                                                         md,
                                                         param,
                                                         self._endpoint,
                                                         (end_time - now) if (end_time < sys.float_info.max) else None,
                                                         auth_key=self._auth_key)
            if exception:
                assert isinstance(exception, Exception)
                # RpcServiceNotHere is a transient error due to sysmgt svr restart.
                # Keep retrying until something else happens.
                if isinstance(exception, DaExceptionRpcServiceNotHere):
                    time.sleep(5)
                else:
                    raise exception
            else:
                return ret_val
            now = time.time()
        raise DaExceptionRpcTimeout()
