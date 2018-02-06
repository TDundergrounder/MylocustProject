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

from Config.DingDang_API_Config import Headers,getAcailableOrder_API
from Common.GetPreIds import Get_BidAndInnId,Get_RoomId

from locust import HttpLocust, TaskSet, task
from Tools.random_test import random_date,random_days

class ApiTask_A(TaskSet):
    
    ids = Get_BidAndInnId()
    bid = ids['bid']

    i = random.randint(0, len(ids['innId']) - 1)
    innId = ids['innId'][i]
    
    roomId = Get_RoomId()
    ch_date = random_date()

    @task
    def runtask_A(self):
        payloads={
            "innId":self.innId,
            "roomId":self.roomId,
            "checkonDate":self.ch_date
        }
        logging.debug("请求提交的参数为:%s"%payloads)
        logging.debug("开始请求app获取可创建订单类型的接口...")
        resp = self.client.post("%s?bid=%s" % (
            getAcailableOrder_API, self.bid), headers=Headers, data=json.dumps(payloads))
        getRoomList_resp_data = json.loads(resp.text)
        

class MyUser(HttpLocust):
    
    host = 'http://10.32.231.205:8080'

    task_set = ApiTask_A

    min_wait = 1000

    max_wait = 5000
