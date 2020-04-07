#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-16 14:12 
# File: test_login.py


from web_test.page_object.index_page import IndexPage
import web_test.test_datas.login_datas as LD
from web_test.common.logger import Mylogger
import pytest


@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
class TestLogin():
    """
    打开一个浏览器，先执行错误数据用例(错误用例执行对后面正常用例执行没有影响)，
    每执行一次后刷新浏览器，全部执行完成之后关闭浏览器
    pytest 按照文件名，方法名的位置运行
    """

    @pytest.mark.parametrize("WrongData", LD.failed_login_data)
    def test_login_failed(self, WrongData,access_web):

        Mylogger().info("*****登录测试，异常场景，手机号密码错误等******")
        print(WrongData['mobile'],WrongData['pwd'])
        access_web[1].login((WrongData['mobile']), WrongData['pwd'])
        try:
            assert access_web[1].get_errMsg_from_pageCenter() == WrongData['check']
        except AssertionError:
            Mylogger().error("断言失败")
            raise



    @pytest.mark.parametrize("data",LD.success_login_data)
    def test_login_success(self,data, access_web):

        #输入用户名密码，点击登录
        Mylogger().info("*****登录测试，正常场景，登录成功******")
        access_web[1].login((data['mobile']),data['pwd'])
        print(IndexPage(access_web[0]).isExist_logout_ele())
        #判断首页中是否有用户名元素
        try:
            assert IndexPage(access_web[0]).isExist_logout_ele()
        except AssertionError:
            Mylogger().error("断言失败")
            raise








