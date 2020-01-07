#!/usr/bin/env python

# import syspath before any other imports
import syspath
from api import tasks
import time


def wait_for_task(dvx, task_response):
    """
    Utility method to wait for task to complete
    :param task_response: TaskResponse with task Id
    :return: Task after successful completion
    """
    state = None
    task = None
    while state not in ["ERROR", "SUCCESS", "CANCELLED"]:
        time.sleep(5) # Wait for 5 seconds
        request = tasks.GetRequest()
        request.id = task_response.taskId
        get_response = tasks.get(dvx=dvx, request=request)
        task = get_response.task[0] # Assume only single task is returned
        state = task.state

    if state == 'SUCCESS':
        return task
    else:
        raise Exception("Task failed")
