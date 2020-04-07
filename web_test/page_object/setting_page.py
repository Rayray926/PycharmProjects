#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-20 16:35 
# File: setting_page.py


from web_test.page_locators.setting_page_locators import SettingPageLocators as setploc
from web_test.common.base_page import BasePage

class SettingPage(BasePage):

    def isExist_setting_ele(self):

        doc = "等待设置页面元素可见"
        res = self.wait_eleVisible(setploc.site_title, doc=doc)
        return res