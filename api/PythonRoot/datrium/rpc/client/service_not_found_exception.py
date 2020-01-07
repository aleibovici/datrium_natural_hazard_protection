#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2013 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************

class ServiceNotFoundException(Exception):
    """
    Exception that will be raised when a service with the specified ID is not found.
    """
    def __init__(self, service_name):
        self._service_name = service_name

    def __str__(self):
        return "Service %s not found" % self._service_name