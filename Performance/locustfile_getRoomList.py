# -*- coding: utf-8 -*-
import sys
import os
import json
import logging
import requests
import random
from random import randint

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from Config.DingDang_API_Config import Headers, getByInnId_API
from Common.GetPreIds import Get_BidAndInnId
# from Common.Login import *

from locust import HttpLocust, TaskSet, task

class ApiTask_A(TaskSet):
    
    ids = Get_BidAndInnId()
    bid = ids['bid']
    
    i = random.randint(0, len(ids['innId']) - 1)
    innId = ids['innId'][i]

    @task
    def runtask_A(self):
        logging.debug("开始请求获取房型与房间列表的接口...")
        resp = self.client.get("%s/%s?bid=%s"%(getByInnId_API,self.innId,self.bid),headers=Headers)
        getRoomList_resp_data = json.loads(resp.text)
        

class MyUser(HttpLocust):
    
    host = 'http://10.32.231.205:8080'

    task_set = ApiTask_A

    min_wait = 1000

    max_wait = 5000
