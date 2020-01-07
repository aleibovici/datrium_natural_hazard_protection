#!/usr/bin/env python

import requests
import json


def __supress_security():
    # supress security warnings
    requests.packages.urllib3.disable_warnings()


def __htpp_get(base_url, username, password):
    # supress security warnings
    __supress_security()

    s = requests.Session()
    s.auth = (username, password)
    s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
    return json.dumps(s.get(base_url, verify=False).json(), sort_keys=True)


def __http_post(base_url, username, password):
    # supress security warnings
    __supress_security()

    # data to be sent to api
    data = {'planId': 'c96e526c-8073-40fa-8ade-79e71b99ea14', 'isPlanned': False, 'failureStrategy': 'FAIL_STRATEGY_STOP_ON_FAILURE', 'selectedSnapshots': [
        {'protectionGroupId': '9eab3c42-8d91-11e9-b7f5-7fd7494dee25', 'protectionGroupSnapshotId': 'cf451330-8f32-11e9-87e1-07aa0e254695', 'dvxId': '35565350-1706-2621-8c6a-d544322b4388', 'dvxName': 'dvx98', 'snapshotName': 'Citrix 30min RPO - Hourly - 2019-06-15T06:00 UTC'}]}

    # sending post request and saving response as response object
    r = requests.session()
    r.auth = (username, password)
    r.headers.update(
        {'referer': 'https://dvx110.slab.datrium.com:7443/cloud/?cloud_id=87bb2615-85ad-4593-ae86-c1083d338e63'})
    r.headers.update({'datriumapi': 'true'})
    response = r.post(url=base_url, data=data, verify=False)
    print(response.text)
    return response
