# -*- coding: utf-8 -*-
import requests
import json
import random
import logging
import datetime
import time 
import string
from random import choice
import sys
import os

sys.path.append(os.getcwd())

ownerid = random.sample(xrange(90000000), 100)
orgid   = random.sample(xrange(80000000), 100)

 
def CommonMoudle(Path, data):
    if Path == data:
        return True
    else:
        return False
        
 
 
Headers={'Content-Type':'application/json' }

 

FileName = time.strftime('%Y%m%d_%H:%M:%S',time.localtime(time.time()))
today = datetime.date.today()
yesterday= today - datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)
thedaybeforeyes = today - datetime.timedelta(days=2)
thedayaftertom = today + datetime.timedelta(days=2)
threedaylater = today + datetime.timedelta(days=3)


user_common={"username": "18516096847", 
                 "password": "123456789",
                "channel": 3}

user_Ota={"username":"18201458971",
          "password":"123456",
          "channel":3}

user_Ota_a = {
    "username": "18221293942",
    "password":"123456",
    "channel":3
}

Ota_name="平凡酒店" 

Server='http://10.32.231.205:'
Port='8080'
hotelname="刘颖的客栈"
Login_API = '/api/v1/pms/login'
SearchRoomList_API = '/api/v1/pms/api/room/getByInnId'
Room_type_1="标准单人间"

# Inn ADMIN API


getAdList_API = '/api/v1/pms/api/helpCenter/getAdList'
getMultiOrder_API = '/api/v1/pms/api/order/multi'
getOrderId_API = '/api/v1/pms/api/order/query'
getAcailableOrder_API = '/api/v1/pms/api/order/getAvailableOrderType'
getInnList_API = '/api/v1/pms/api/inn/get'
sendMessage_API = '/api/v1/pms/push/valid'
getDayInninfo_API = '/api/v1/pms/api/order/getDayInnInfo'
getRoomStatusInfo_API = '/api/v1/pms/api/order/getInnInfo'
getByInnId_API = '/api/v1/pms/api/room/getByInnId'
Login_Create='/api/v1/pms/api/inn/create'
Login_Edit='/api/v1/pms/api/inn/edit'
login_innId='/api/v1/pms/api/stat2/allInn'
delet='/api/v1/pms/api/inn/del/'
get_list='/api/v1/pms/api/inn/get'
get_hotel='/api/v1/pms/api/inn/'
get_ota='/api/v1/pms/api/inn/otaOrderCount/'
validata='/api/v1/pms/api/inn/validate'


getAdList_API_url = Server + Port + getAdList_API
getMultiOrder_API_url = Server + Port + getMultiOrder_API
getOrderId_API_url = Server + Port + getOrderId_API
getRoomList_API_url = Server+Port+getByInnId_API
Login_API_url = Server+Port+Login_API
Login_API_url_create=Server+Port+Login_Create
Login_API_url_edit=Server+Port+Login_Edit
Login_API_url_innId=Server+Port+login_innId
Login_API_url_del=Server+Port+delet
Login_API_url_get=Server+Port+get_list
Login_API_url_hotel=Server+Port+get_hotel
Login_API_url_ota=Server+Port+get_ota
Login_API_url_validata=Server+Port+validata

SearchRoomList_API_url =Server+Port+SearchRoomList_API
# Inn ADMIN API










