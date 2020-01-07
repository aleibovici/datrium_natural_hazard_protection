#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2017 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************

from SysMgmt.Api.IDL.Main.ApiTasks_pb2 import Tasks_Stub
from api.util.stub import get_stub

# XXX TODO (piyush) autogenerate this file

def get(dvx, request):
    return get_stub(dvx, Tasks_Stub).get(request)
