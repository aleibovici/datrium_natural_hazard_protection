#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2017 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************

from SysMgmt.Api.IDL.Main.ApiVmsSnapshots_pb2 import GetRequest, ReplicateRequest, CloneRequest
from .vms_snapshots import get, replicate, clone