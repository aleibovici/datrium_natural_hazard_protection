#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2013 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************


class ClientAdapterFactory:
    """ Factory class to get RPCClientAdapter to talk to the server"""

    def get_client_adapter(self, is_controller=True, is_cli=False):
        """ Gets a RPCClientAdapter to talk to the server

            @param is_controller: Whether the code is running on controller or host.
            @param is_cli: Whether the request is for CLI method invocation.
            @return: A Client Adapter
        """
        from datrium.rpc.client.impl.http_remote_method_invoker import HTTPRemoteMethodInvoker
        return HTTPRemoteMethodInvoker(is_controller=is_controller, is_cli=is_cli)
