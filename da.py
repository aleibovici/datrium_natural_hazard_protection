#!/usr/bin/env python

# import syspath before any other imports
from api.util.stub import get_stub
from api.PythonRoot.SysMgmt.Api.IDL.Main.ApiVms_pb2 import Vms_Stub
from utils import wait_for_task
from api import vms
from api.dvx import Dvx
from api.vms import snapshots
import syspath
import helper
import sys
import logging
from botocore.response import get_response
sys.path.insert(0, '/usr/local/lib/python3.7/site-packages/datrium')

logger = logging.getLogger()

'''Function to establish connection to DVX'''


def connect(ip, username, password):
    dvx1 = Dvx(ip, username, password)
    logger.info('')
    logger.info('-------------------------------------')
    logger.info('DVX connection sucesfully established')
    test_connection(dvx1)   # Test DVX connectivy
    return dvx1


'''Function to retrieve a single vm by name'''


def get_vm(dvx, name):
    request = vms.GetRequest()
    request.namePattern.extend(name)
    response = vms.get(dvx=dvx, request=request)
    return response.vm[0]


'''Function to list all vms'''


def get_vms(dvx):
    request = vms.GetRequest()
    get_response = vms.get(dvx=dvx, request=request)
    return get_response


''' Function to take snapshot of individual vms'''


def take_vm_snapshot(dvx, name, retention, prefix):
    request = vms.TakeSnapshotRequest()
    request.id = get_vm(dvx, name).id
    request.snapshotName = prefix + "-" + str(name) + "-snapshot"
    request.retention = retention
    task_response = vms.take_snapshot(dvx=dvx, request=request)
    logger.info('Snapshotting ' + name[0] + ' with expiration set to ' + str(int(retention)/60) + ' minutes')
    task = wait_for_task(dvx, task_response)
    return task


''' Function to replicate a given vm snapshot'''


def replicate_vm_snapshot(dvx, snapId, replicaSiteName, retention):
    assert snapId != None, "SnapId not found"
    request = snapshots.ReplicateRequest()
    request.id = snapId
    request.replicaSiteName = replicaSiteName
    request.retention = retention
    logger.info('Replicating snapshot %s' % snapId)
    task_response = snapshots.replicate(dvx=dvx, request=request)
    return task_response


''' Function to test connectivity to DVX with a vm.GetRequest '''


def test_connection(dvx):

    try:
        request = vms.GetRequest()
        get_response = vms.get(dvx=dvx, request=request)
    except:
        logger.error('Unexpected error: ' + str(sys.exc_info()[0]))
        raise
