#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2013 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************
from abc import ABCMeta, abstractmethod


class RPCClientAdapter:
    """ All remote method invocation are handled by implementations of this
        abstract class.
    """

    __metaclass_ = ABCMeta

    @abstractmethod
    def invoke_method(self, interface, method, arg, endpoint=None, timeout=None, auth_key=None):
        """ Entry point of all method invocations in the RPC application stack
            on the client

            @param interface: The interface on which a method is invoked
            @param method: The method being invoked
            @param arg: List of protocol buffer messages which represent the parameters
                        of the method
            @param endpoint: The endpoint where the interface is hosted
            @param timeout: An optional timeout for this particular call. This will override
                            the global timeout
            @param auth_key: Auth_key to use for the request.
        """
        return

    @abstractmethod
    def disconnect(self):
        """ Disconnect any connections to the server and free up all
            network resources
        """
        return
