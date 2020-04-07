#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-16 14:08 
# File: index_page.py



from web_test.page_locators.index_page_locators import IndexPageLocators as inc
from web_test.common.base_page import BasePage

class IndexPage(BasePage):



    def isExist_logout_ele(self):
        """判断是否存在用户信息(是否登录成功)，如果存在返回True，如果不存在返回False"""
        doc="首页元素_判断登录成功后元素是否存在"
        res=self.wait_eleVisible(inc.user_locate, poll_frequency=0.2, doc=doc)
        if res:
            return True
        else:
            return False




    def href_jump(self,data):
        doc="首页超链接跳转"
        self.wait_eleVisible(inc.user_locate, poll_frequency=0.2, doc=doc)
        self.click_ele(data)







