#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-20 16:13 
# File: product_page.py


from web_test.page_locators.product_page_locators import ProductPageLocators as ppc
from web_test.common.base_page import BasePage

class ProductPage(BasePage):

    def isExist_product_ele(self):

        doc = "等待商品页面元素可见"
        res = self.wait_eleVisible(ppc.order_title, doc=doc)
        return res


