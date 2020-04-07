#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-20 15:40 
# File: order_page.py

from web_test.page_locators.purchase_order_locators import POrderLocators as poc
from web_test.common.base_page import BasePage


class POrderPage(BasePage):


    def isExist_order_ele(self):

        doc="等待购物订单元素可见"
        res=self.wait_eleVisible(poc.page_title,doc=doc)
        if res:
            return True
        else:
            return False

