# -*- coding: utf-8 -*-
import os
import sys
import logging
import json
import datetime
import string
import requests
from random import randint

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from Config.DingDang_API_Config import *
from Tools.random_test import *


def Get_BidAndInnId(**self):
    logging.debug("Get_BidAndInnId函数...")
    r = requests.request('POST', Login_API_url, headers=Headers, data=json.dumps(user_Ota))
    login_data=json.loads(r.text)
    StatusCode=CommonMoudle(login_data['status'], 0)
    logging.debug("开始判断StatusCode ...")
    Login={}
    if StatusCode == True:
        Login = {
            'status': login_data['status'],
            'message': login_data['message'],
            'bid': login_data['data']['bid'],
            'Result': True
        }
        logging.debug("StatusCode正确，返回值为:%s"%login_data['status'])
        logging.debug(login_data['message'])
        bid = {
            "bid":Login['bid']
        }
        # bid = Login['bid']
        payload = {}
        date_A = random_date()
        date_B = random_date()
        if date_A > date_B: 
            startDate = date_B
            endDate = date_A
            payload = {
                "startDate": startDate, 
                "endDate":  endDate
            }
        else:
            startDate = date_A
            endDate = date_B
            payload = {
                "startDate": startDate, 
                "endDate":  endDate
            }
        logging.debug("开始请求登录接口...")
        r = requests.request('POST', Login_API_url_innId,params=bid, headers=Headers,data=json.dumps(payload))
        innId_data = json.loads(r.text)
        Login_A={
            'status':innId_data['status'],
            'message':innId_data['message'],
            'data':innId_data['data']['innList'],
            'Result':True
            }

        list_innids = []
        for i in range(len(Login_A['data'])):            
            innid=Login_A['data'][i]['innId']
            list_innids.append(innid)
        
        ids = {
            "bid":bid['bid'],
            "innId": list_innids
        }
        return ids 
        # break     
    else:
        Login={
            'status':login_data['status'],
            'message':login_data['message'],
            'Result':False,
            }
        logging.error("StatusCode错误，返回值为:%s"%login_data['status'])
        logging.error(login_data['message'])
        return Login


def Get_RoomId(**self):
    ids = Get_BidAndInnId()
    logging.debug("存在以下innId:%s"%ids['innId'])
    while True:
        i = random.randint(0, len(ids['innId']) - 1)
        logging.debug("此时随机取到的innId为:%s" % ids['innId'][i])
        logging.debug("开始请求获取roomId的接口...")
        r = requests.request('GET', url="%s/%s?bid=%s" %
                            (getRoomList_API_url, ids['innId'][i], ids['bid']), headers=Headers)
        innId_data = json.loads(r.text)
        logging.debug("开始判断innId为%s时roomId是否为空..." % ids['innId'][i])
        if len(innId_data['data'])!=0:
            logging.debug("当innId为%s时，此时满足roomId不为空" % (ids['innId'][i]))
            break

    Inn = innId_data['data'][0]['roomDetail']
    j = random.randint(0, len(Inn)-1)
    roomId = Inn[j]['roomId']
    logging.debug("当前取得到的RoomId为:%s" % roomId)
    return roomId



def Get_OrderId(**self):
    logging.debug("进入Get_OrderId方法...")
    ids = Get_BidAndInnId()
    logging.debug("存在以下innId:%s" % ids['innId'])
    while True:
        i = random.randint(0, len(ids['innId']) - 1)
        date_A = random_date()
        date_B = random_date()
        payloads = {}
        if date_A > date_B:
            startDate = date_B
            endDate = date_A
            payloads = {
                "innId": ids['innId'][i],
                "dateType":1,
                "startDate": startDate,
                "endDate":  endDate
            }
        else:
            startDate = date_A
            endDate = date_B
            payloads = {
                "innId": ids['innId'][i],
                "dateType": 1,
                "startDate": startDate,
                "endDate":  endDate
            }
        logging.debug("接口请求参数为:%s" % payloads)
        logging.debug("开始请求获取OrderId的接口...")
        r = requests.request('POST', url="%s?bid=%s" %
                             (getOrderId_API_url, ids['bid']), headers=Headers, data=json.dumps(payloads))
        order_data = json.loads(r.text)
        if len(order_data['data']['list']) != 0:
            logging.debug("当innId为%s时，此时满足roomId不为空" % (ids['innId'][i]))
            break    
    Inn = order_data['data']['list']
    j = random.randint(0, len(Inn) - 1)
    orderId = Inn[j]['orderId']
    logging.debug("当前取得到的orderId为:%s" % orderId)
    return orderId
