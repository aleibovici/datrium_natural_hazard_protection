#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2018 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************

class AuthenticationFailedException(Exception):
    """
    Exception that will be raised when authentication fails for the request
    """
    def __init__(self):
        pass

    def __str__(self):
        return "Authentication failed for the request"
