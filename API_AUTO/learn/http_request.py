#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-04 09:35 
# File: http_request.py
"""
example
一、需求功能：
    XXXX
二、实现过程：
    XXX

"""
import requests

url = 'http://youli.uban360.net/gift-manager/account/login'
data = {
        "mobile": 15634116913,
        "password": "123qazxsw"
    }
s=requests.session()
res_1=s.get(url,params=data)
print(res_1.json())
url_1='http://youli.uban360.net/pre-account/recharge'
data_1 = {
        "mobile": 15634116913,
        "password": "123qazxsw"
    }
res=s.get(url_1,)
print(res.json())