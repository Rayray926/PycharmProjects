#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-04 10:11 
# File: http_request.py
"""
example
一、需求功能：
    XXXX
二、实现过程：
    XXX

"""
import requests
from API_AUTO.tools.my_log import Mylogger

my_log=Mylogger()

class HttpRequest:
    def http_test(self,url,data,http_method,cookie=None):
        try:
            if http_method.upper()=="GET":
                res=requests.get(url,data,cookies=cookie)


            elif  http_method.upper()=="POST":
                res = requests.post(url, data,cookies=cookie)


            else:
                my_log.info("http_method 有误")
        except Exception as e:
            my_log.info("请求报错了{0}".format(e))
            raise e
        finally:
            return  res


