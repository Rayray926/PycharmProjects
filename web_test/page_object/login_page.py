#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-16 14:07 
# File: login_page.py



from web_test.page_locators.login_page_locators import LoginPageLocators as loc
from web_test.common.base_page import BasePage

class LoginPage(BasePage):


    #输入用户名、密码，点击登录
    def login(self,name,pwd):
        doc="登录页面_登录页面"
        self.wait_eleVisible(loc.name_text,doc=doc)
        self.input_text(loc.name_text,name,doc=doc)
        self.input_text(loc.pwd_text, pwd, doc=doc)
        self.click_ele(loc.login_but,doc=doc)


    #获取登录错误信息
    def get_errMsg_from_pageCenter(self):

        doc="登录页面_获取登录错误信息"
        self.wait_eleVisible(loc.err_msg_locate,poll_frequency=0.2,doc=doc)
        return  self.get_text(loc.err_msg,doc)


 



