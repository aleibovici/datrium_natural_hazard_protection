#!/usr/bin/env python
#**************************************************************
#* Copyright (c) 2017 Datrium, Inc. All rights reserved.      *
#*                -- Datrium Confidential --                  *
#**************************************************************

import sys
import os

CURRENT_PATH = os.path.realpath(os.path.dirname(__file__))

PATHS = [
    CURRENT_PATH,
    os.path.realpath(os.path.join(CURRENT_PATH, 'api/PythonGenRoot')),
    os.path.realpath(os.path.join(CURRENT_PATH, 'api/PythonRoot'))
]

for path in PATHS:
    if path not in sys.path:
        sys.path.insert(0, path)