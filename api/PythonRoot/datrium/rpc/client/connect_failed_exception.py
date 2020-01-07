#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2013 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************
ex_message = 'Unable to connect to %s'


class ConnectFailedException(Exception):
    """
    Exception that will be raised when a connection attempt fails.
    """
    def __init__(self, url):
        self.url = url
        message = ex_message % url
        Exception.__init__(self, message)
