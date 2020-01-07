#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2017 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************

from SysMgmt.Api.IDL.Main.ApiVms_pb2 import GetRequest, CloneRequest, TakeSnapshotRequest
from .vms import get, take_snapshot, clone