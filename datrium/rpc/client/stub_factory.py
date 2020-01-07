#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2013 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************
import logging

from google.protobuf.descriptor import Descriptor

from datrium.rpc.client.impl.stub_impl import StubImpl


class StubFactory:
    """ Class to generate stubs for the service interfaces"""

    def __init__(self, rpc_client_adapter, auth_key=None):
        """ Constructor

            @param rpc_client_adapter: The client adapter through which all
                                      calls are made
            @param auth_key: An optional auth key which maybe used to authenticate with a remote
                             server.
        """
        self._rca = rpc_client_adapter
        self._logger = logging.getLogger(__name__)
        self._auth_key = auth_key

    def create_stub(self, iface, instance_id=None,
                    endpoint=None, timeout=None, auth_key=None):
        """ Creates a Stub for the given interface. Returns a proxy stub
            on which remote calls are made.

            @param iface: The remote interface class.
            @param instance_id: Instance ID of remote interface
            @param endpoint: The name of the endpoint where the service is hosted
            @param timeout: An optional timeout per stub which will override the default timeout.
            @param auth_key: Auth key (if any) to use for communication.

            @return A Stub for the remote interface
        """
        if not iface or issubclass(iface, Descriptor):
            raise Exception("No iface given")
        iface_name = iface.DESCRIPTOR.full_name
        self._logger.debug("Creating stub for %s" % iface_name)
        if not auth_key:
            auth_key = self._auth_key
        return StubImpl(iface, instance_id, self._rca, endpoint, timeout, auth_key)
