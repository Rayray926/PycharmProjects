#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-04-01 15:18 
# File: http_request.py

import requests
from common.my_log import Mylog
from common.get_session import Session
from conf.config import ConfigYaml




class HttpRequest():

    def __init__(self):

        env = ConfigYaml().get_test_environment()
        if env == "TEST_DEBUG":
            self.url = ConfigYaml().get_debug_environment()['giftDealerManageHost']
        else:
            self.url= ConfigYaml().get_release_environment()['giftDealerManageHost']
        self.get_session=Session().get_session(env)

    def get_request(self,url,data,headers=None):
        """
        :param url: 地址
        :param data: 数据
        :param headers: 头信息
        :return:
        """
        url=self.url+url
        try:
            if data is None:
                res=requests.get(url,headers=headers,cookies=self.get_session,)
            else:
                res=requests.get(url,data,headers=headers,cookies=self.get_session)
            return  res.json()

        except requests.RequestException as e:
            Mylog().error("请求出错了{}".format(e))
            raise e

    def post_request(self,url,data,files=None,headers=None):
        url = self.url + url
        try:
            if data is None:
                res=requests.post(url,headers=headers,files=files,cookies=self.get_session)
            else:
                res=requests.post(url,data,headers=headers,files=files,cookies=self.get_session)
            return  res.json()

        except requests.RequestException as e:
            Mylog().error("请求出错了{}".format(e))
            raise e




if __name__ == '__main__':
    headers = {'Conteny-Type': 'multipart/form-data; boundary=----WebKitFormBoundary62WdLU4aAEvvPf8p'}
    file = {"uploadFile": ("s-14.png", open("/Users/ibell/Downloads/pictures/s-14.png", "rb"), "image/png")}

    # print(HttpRequest().post_request('/gift-manager/file/manager/upload?isMainPic=true',data=file,headers=headers))
    # print(requests.post(url='http://youli.uban360.net/gift-manager/file/manager/upload?isMainPic=true',data=file).text)
    res=HttpRequest().post_request(url='/gift-manager/file/manager/upload?isMainPic=true',data=None,files=file,headers=headers)
    print(res)











