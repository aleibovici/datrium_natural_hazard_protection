#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2017 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************

class DvxException(Exception):
    """
    DVX Base Exception
    """
    def __init__(self, error_code, error_text):
        self._error_code = error_code
        self._error_text = error_text

    def __str__(self):
        return "%s: %s" % (self._error_code, self._error_text)
