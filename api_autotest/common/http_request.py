#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-04-01 15:18 
# File: http_request.py

import requests
from my_log import MyLogging

class HttpRequest:

    def http_request(self,url,data,http_method,cookie=None):

        try:

            if http_method.upper()=="GET":
                res=requests.get(url,data,cookies=cookie)
                return res

            elif http_method.upper()=="POST":
                res=requests.post(url,data,cookies=cookie)
                return res
            else:
                MyLogging().info('http_mrthod 有误')
        except Exception as e:
            MyLogging().error("请求出错了".format(e))
            raise e


if __name__ == '__main__':
    HttpRequest().http_request('http://youli.uban360.net/gift-manager/account/login','{"mobile": 15634116913,"password": "123qazxsw"}','post')



