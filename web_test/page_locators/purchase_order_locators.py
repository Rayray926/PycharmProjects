#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-20 15:48 
# File: purchase_order_locators.py

from selenium.webdriver.common.by import By

class POrderLocators:
    """存放订单管理页元素"""

    #页面title
    page_title=(By.XPATH,"//*[@class='breadcrumb']")


