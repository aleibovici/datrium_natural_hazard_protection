#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2017 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************

from SysMgmt.Api.IDL.Main.ApiVmsSnapshots_pb2 import VmsSnapshots_Stub
from api.util.stub import get_stub

# XXX TODO (piyush) autogenerate this file

def get(dvx, request):
    return get_stub(dvx, VmsSnapshots_Stub).get(request)

def replicate(dvx, request):
    return get_stub(dvx, VmsSnapshots_Stub).replicate(request)

def clone(dvx, request):
    return get_stub(dvx, VmsSnapshots_Stub).clone(request)
