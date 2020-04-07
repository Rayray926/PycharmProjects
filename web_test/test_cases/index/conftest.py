#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-22 10:51 
# File: conftest.py.py

from selenium import webdriver
import web_test.test_datas.common_datas as CD
import web_test.test_datas.login_datas as LD
from web_test.page_object.login_page import LoginPage
from web_test.page_object.index_page import IndexPage
import pytest

driver=None



@pytest.fixture(scope="class")
def access_web():
    global driver
    driver=webdriver.Chrome()
    driver.get(CD.web_login_url)
    jump_driver=IndexPage(driver)
    LoginPage(driver).login(LD.success_login_data[0]["mobile"],LD.success_login_data[0]['pwd'])
    yield  jump_driver
    driver.quit()

@pytest.fixture
def page_back():
    global  driver
    yield
    driver.back()


