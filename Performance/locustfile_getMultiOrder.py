# -*- coding: utf-8 -*-
import sys
import os
import json
import logging
import random
from random import randint

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from Config.DingDang_API_Config import Headers, getMultiOrder_API
from Common.GetPreIds import Get_BidAndInnId,Get_OrderId

from locust import HttpLocust, TaskSet, task
from Tools.random_test import random_date, random_days,random_fromType


class ApiTask_A(TaskSet):

    ids = Get_BidAndInnId()
    bid = ids['bid']

    orderId = Get_OrderId()
    from_type = random_fromType()

    @task
    def runtask_A(self):
        payloads = {
            "orderId": self.orderId,
            "from": self.from_type,
        }
        logging.debug("请求的参数为:%s"%payloads)
        logging.debug("开始请求查询多张订单的接口...")
        resp = self.client.post("%s?bid=%s" % (
            getMultiOrder_API, self.bid), headers=Headers, data=json.dumps(payloads))
        getRoomList_resp_data = json.loads(resp.text)


class MyUser(HttpLocust):

    host = 'http://10.32.231.205:8080'

    task_set = ApiTask_A

    min_wait = 1000

    max_wait = 5000
