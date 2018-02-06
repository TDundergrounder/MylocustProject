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

from Config.DingDang_API_Config import Headers, sendMessage_API,user_Ota
from Common.GetPreIds import Get_BidAndInnId

from locust import HttpLocust, TaskSet, task
from Tools.random_test import random_date,random_days,random_PhoneNO

class ApiTask_A(TaskSet):
    
    ids = Get_BidAndInnId()
    bid = ids['bid']
    
    i = random.randint(0, len(ids['innId']) - 1)
    innId = ids['innId'][i]

    cur_date = random_date()
    # cellNum = random_PhoneNO()
    cellNum = user_Ota['username']

    @task
    def runtask_A(self):
        payloads={
            "uid":self.cellNum,
            "token":self.bid,
        }
        logging.debug("请求的参数为:%s"%payloads)
        logging.debug("开始请求推送用户验证的接口...")
        resp = self.client.post(sendMessage_API,headers=Headers,data=json.dumps(payloads))
        getRoomList_resp_data = json.loads(resp.text)
        

class MyUser(HttpLocust):
    
    host = 'http://10.32.231.205:8080'

    task_set = ApiTask_A

    min_wait = 1000

    max_wait = 5000
