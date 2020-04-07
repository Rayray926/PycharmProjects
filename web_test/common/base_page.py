#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-21 11:40 
# File: base_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import web_test.common.dir_config as dirconf
from web_test.common.logger import Mylogger
from selenium.webdriver.common.by import By
import datetime


#封装基本函数--执行日志，异常处理，失败截图

class BasePage:
    #所有页面公共的部分

    def __init__(self,driver):
        self.driver=driver

    #等待元素可见
    def wait_eleVisible(self,locator,timeout=30,poll_frequency=0.5,doc=""):
        Mylogger().info("等待元素{}可见".format(locator))
        try:
            #开始等待时间
            start_time=datetime.datetime.now()
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located(locator))
            end_time = datetime.datetime.now()
            #等待时间
            wait_time=(end_time-start_time).seconds
            Mylogger().info("元素等待结束，等待时间为:{}".format(wait_time))
            return True

        except:
            Mylogger().error("等待元素可见失败～～～")
            #截图
            self.save_screenshot(doc)
            raise


    #保存截图
    def save_screenshot(self,doc):
        #图片名称：模块名_页面名称_元素名称_时间.png
        file_path=dirconf.screenshot_path+"/"+"{0}_{1}.png".format(doc,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.driver.save_screenshot(file_path)
        Mylogger().info("截取网页成功，文件路径为:{0}".format(file_path))

    #查找元素
    def get_ele(self,locator,doc=""):
        Mylogger().info("查找元素{}".format(locator))
        try:
            return self.driver.find_element(*locator)

        except:
            Mylogger().error("查找元素失败～～～")
            #截图
            self.save_screenshot(doc)
            raise

    #点击元素
    def click_ele(self, locator, doc=""):
        Mylogger().info("点击元素{}".format(locator))
        ele=self.get_ele(locator,doc)
        try:
             ele.click()

        except:
            Mylogger().error("点击元素失败!!!!!")
            # 截图
            self.save_screenshot(doc)
            raise

    #输入操作
    def input_text(self, locator,text,doc=""):
        Mylogger().info("点击元素{}".format(locator))
        ele=self.get_ele(locator,doc)
        try:
            ele.send_keys(text)
        except:
            Mylogger().error("元素输入失败!!!!!")
            # 截图
            self.save_screenshot(doc)
            raise

    #获取元素属性

    def get_text(self, locator,  doc=""):
        Mylogger().info("点击元素{}".format(locator))
        ele = self.get_ele(locator, doc)
        try:
            return ele.text

        except:
            Mylogger().error("获取元素文本内容失败!!!!!")
            # 截图
            self.save_screenshot(doc)
            raise

    # alert处理

    #iframe切换