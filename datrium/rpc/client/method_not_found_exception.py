#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2014 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************

class MethodNotFoundException(Exception):
    """
    Exception that will be raised when a method with the specified ID is not found.
    """
    def __init__(self, method_name):
        self._method_name = method_name

    def __str__(self):
        return "Method %s not found" % self._method_name