#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2017 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************

from SysMgmt.Api.IDL.Main.ApiVms_pb2 import Vms_Stub
from api.util.stub import get_stub

# XXX TODO (piyush) autogenerate this file

def get(dvx, request):
    return get_stub(dvx, Vms_Stub).get(request)

def take_snapshot(dvx, request):
    return get_stub(dvx, Vms_Stub).take_snapshot(request)

def clone(dvx, request):
    return get_stub(dvx, Vms_Stub).clone(request)
