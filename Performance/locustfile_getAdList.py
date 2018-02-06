# -*- coding: utf-8 -*-
import sys
import os
import logging
import json
import requests
import random
from random import randint

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from Config.DingDang_API_Config import Headers,getAdList_API
from Common.GetPreIds import Get_BidAndInnId

from locust import HttpLocust, TaskSet, task


class ApiTask_A(TaskSet):
    ids = Get_BidAndInnId()
    bid = ids['bid']

    @task
    def runtask_A(self):
        logging.debug("开始请求获取活动信息的接口...")
        resp = self.client.get("%s?bid=%s" % (getAdList_API,
                                              self.bid), headers=Headers)
        getRoomList_resp_data = json.loads(resp.text)


class MyUser(HttpLocust):

    host = 'http://10.32.231.205:8080'

    task_set = ApiTask_A

    min_wait = 1000

    max_wait = 5000
