#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2017 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************

class Dvx(object):
    """
    DVX connection info
    """
    def __init__(self, ip, user_name, password):
        self.ip = ip
        self.user_name = user_name
        self.password = password
