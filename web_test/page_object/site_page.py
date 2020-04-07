#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-20 16:33 
# File: site_page.py

from web_test.page_locators.site_page_locators import SitePageLocators as sloc
from web_test.common.base_page import BasePage

class SitePage(BasePage):


    def isExsit_site_ele(self):

        doc = "首页元素_判断登录成功后元素是否存在"
        res = self.wait_eleVisible(sloc.site_title, poll_frequency=0.2, doc=doc)
        return res
