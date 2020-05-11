#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-04-24 16:01 
# File: get_session.py

import requests
from conf.config import ConfigYaml
from common.my_log import Mylog



class Session:

    def get_session(self,env):



        # header={
        #     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        #     "Content-Type":"application/x-www-form-urlencoded"
        #
        if env=="TEST_DEBUG":
            Mylog().info("本次执行的是测试环境用例")
            login_url=ConfigYaml().get_debug_environment()['giftDealerManageHost']+'/gift-manager/account/login'
            data=ConfigYaml().get_debug_environment()['giftDealerManageLoginInfo']
            debug_session=requests.Session()
            debug_response=debug_session.post(login_url,data,)
            return debug_response.cookies

        elif env=="TEST_RELEASE":
            Mylog().info("本次执行的是线上环境用例")
            login_url = ConfigYaml().get_release_environment()['giftDealerManageHost'] +'/gift-manager/account/login'
            print(login_url)
            data = ConfigYaml().get_release_environment()['giftDealerManageLoginInfo']
            print(data)
            release__session = requests.Session()
            release__response = release__session.post(login_url, data,verify=False)
            return release__response.cookies
        else:
            Mylog().error("获取cookie 错误")



if __name__ == '__main__':

    print(Session().get_session('TEST_RELEASE'))
    # print(Session().get_session('TEST_DEBUG'))



