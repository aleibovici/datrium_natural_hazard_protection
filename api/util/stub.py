#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2017 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************
from datrium.rpc.client.stub_factory import StubFactory

from .api_invoker import ApiInvoker


def get_stub(dvx, iface):
    """
    Get stub to invoke APIs
    """
    api = ApiInvoker(user_name=dvx.user_name, password=dvx.password)
    stub_factory = StubFactory(api)
    return stub_factory.create_stub(iface, endpoint=dvx.ip)
