#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-20 16:28 
# File: preaccount_page.py


from web_test.page_locators.preaccount_page_locators import PreAccountPageLocators as preloc
from web_test.common.base_page import BasePage

class Preaccountpage(BasePage):



    def isExsit_preaccount_ele(self):

        doc = "等待预付款账户元素可见"
        res = self.wait_eleVisible(preloc.pre_account_title, doc=doc)
        return res

