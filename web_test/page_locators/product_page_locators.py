#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-20 16:16 
# File: product_page_locators.py

from selenium.webdriver.common.by import By

class ProductPageLocators:

    #购物订单title
    order_title=(By.XPATH,"//*[@class='item-list__title']")