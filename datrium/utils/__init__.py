##############################################################
# Copyright (c) 2013-2017 Datrium, Inc. All rights reserved. #
#                -- Datrium Confidential --                  #
##############################################################

'''
This module defines common basic utilities for Datrium python infrastructure.

Please add unit test cases in Prod/PythonTests/UtilTestPlan.py
'''

# This is used by both the HEAD and VAAI VIBs on ESX.
# Please be EXTRA careful about what to import!

import os
import errno
import logging

def create_file_path(file_name):
    """
    Create the filepath including any missing directories.
    """
    folder = os.path.dirname(file_name)
    try:
        os.makedirs(folder)
    except OSError as e:
        # If the error is anything other than what we expect, raise.
        if e.errno not in [os.errno.EEXIST, os.errno.ENOENT]:
            raise e

    # Touch the file.
    with open(file_name, "a") as file_handle:
        pass


def get_zk_url_from_configfile(conf_file):
    """
    Read the zk_url from the dva.conf config file. We need to parse the conf file
    in the same way as the C side, including the handling of spaces in sscanf()
    since the conf file is shared.
    """
    return get_value_from_configfile("Registry.zookeeper", conf_file)

def get_value_from_configfile(key, conf_file='/etc/dva.conf'):
    """
    Read a particular key from dva.conf config file.
    If the key cannot be found 'None' will be returned.
    We need to parse the conf file in the same way as the C side,
    including the handling of spaces in sscanf()
    since the conf file is shared.
    """
    with open(conf_file, "r") as f:
        # See if the entry for Registry.zooKeeper exists.
        lines = f.readlines()
        for line in lines:
            if len(line.strip()) == 0:
                # Ignore empty lines.
                continue
            chunks = line.replace(" ", "").rstrip().split("=")
            if chunks[0] == key:
                return chunks[1].strip()
    return None

def make_dirs(path):
    '''
    mkdir -p
    '''
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else:
            raise e


def get_camelcase_name_chunks(name):
    """
    Given a name, get its parts.
    E.g: maxCount -> ["max", "count"]
    """
    out = []
    out_str = ""
    for c in name:
        if c.isupper():
            if out_str:
                out.append(out_str)
            out_str = c.lower()
        else:
            out_str += c
    out.append(out_str)
    return out

MIN_SUPPORTED_MAJ = 5
MIN_SUPPORTED_MIN = 5
MIN_BUILD_NUM_SUPPORTED = 2001466
def is_supported_vc_version(version, build_num):
    """
    https://www.vmware.com/support/vsphere5/doc/vsphere-vcenter-server-55u2-release-notes.html
    Is the version atleast 5.5.0, build: 2001466
    """
    major, minor, _ = version.split('.')
    if MIN_SUPPORTED_MAJ > int(major):
        return False
    elif MIN_SUPPORTED_MAJ == int(major):
        if MIN_SUPPORTED_MIN > int(minor):
            return False
        elif MIN_BUILD_NUM_SUPPORTED > build_num:
            return False
    return True
