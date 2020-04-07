#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-21 17:00 
# File: conftest.py.py


import pytest
from selenium import webdriver
import  web_test.test_datas.common_datas as CD
from web_test.page_object.login_page import LoginPage



driver=None
@pytest.fixture(scope="class")
def access_web():

    global driver
    #前置操作
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    lg=LoginPage(driver)
    yield (driver,lg)
    driver.quit()

@pytest.fixture
def refresh_page():
    global driver
    yield
    driver.refresh()



