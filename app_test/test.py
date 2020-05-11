#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-04-24 21:39 
# File: test.py.py

from appium import  webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import time
desire_caps={}

desire_caps['platformName']="Android"

desire_caps['platformVersion']="9"

desire_caps['deviceName']='MI 8 SE'

# desire_caps['automationName']='UiAutomator2'

desire_caps['appPackage']='com.shinemo.qoffice.zjcc'

desire_caps['appActivity']='com.shinemo.qoffice.biz.login.SplashActivity'

desire_caps["noReset"]=True
print(desire_caps)

#链接appium server
#将服务器参数传送过去
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desire_caps)
time.sleep(2)
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.shinemo.qoffice.zjcc:id/tab_service_icon")))

# WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.shinemo.qoffice.zjcc:id/tab_service_icon")))
# driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
driver.find_element_by_id("com.shinemo.qoffice.zjcc:id/tab_service_icon").click()
# driver.implicitly_wait(1)
# driver.find_element_by_id("com.shinemo.qoffice.zjcc:id/setting_btn").click()
# driver.implicitly_wait(1)
# driver.find_element_by_id("com.shinemo.qoffice.zjcc:id/safe_setting_layout").click()
# driver.implicitly_wait(1)
# driver.find_element_by_id("com.shinemo.qoffice.zjcc:id/switch_btn_gesture").click()


#九宫格手势
#九宫格view获取宽度、高度
# lock=driver.find_element_by_id("com.shinemo.qoffice.zjcc:id/lock_pattern")
# #获取九宫格的X，Y坐标
#
# x=lock.location.get('x')
# print(x)
# y=lock.location.get('y')
# print(y)
# width = lock.get_window_size()['width']
# height = lock.get_window_size()['height']

#计算偏移量
# offset=width/6
# p11=int(x+width/6),int(y+width/6)
# p12=int(x+width/2),int(y+width/6)
# p13=int(x+width-offset),int(y+width/6)
# p21=int(x+width/6),int(y+height/2)
# p22=int(x+width/2),int(y+height/2)
# p23=int(x+width-offset),int(y+height/2)
# p31=int(x+width/6),int(y+height-offset)
# p32=int(x+width/2),int(y+height-offset)
# p33=int(x+width-offset),int(y+height-offset)
#
#
# for i in range(2):
#     TouchAction(driver).press(x=p11[0],y=p11[1]).wait(1000)\
#         .move_to(x=p12[0],y=p12[1]).wait(1000)\
#         .move_to(x=p13[0],y=p13[1]).wait(1000)\
#         .move_to(x=p23[0],y=p23[1]).wait(1000)\
#         .move_to(x=p33[0],y=p33[1]).wait(1000).release().perform()





# WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.shinemo.qoffice.zjcc:id/tv_agree")))
# driver.find_element_by_id("com.shinemo.qoffice.zjcc:id/tv_agree").click()
#
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.android.packageinstaller:id/permission_allow_button")))
# driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
# driver.implicitly_wait(2)
# # WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"ccom.android.packageinstaller:id/permission_allow_button")))
# driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
#
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.shinemo.qoffice.zjcc:id/btnLogin")))
# driver.find_element_by_id("com.shinemo.qoffice.zjcc:id/btnLogin").click()
#
# driver.find_element_by_id("com.shinemo.qoffice.zjcc:id/userhead").click()
# driver.implicitly_wait(1)
#
# driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("测试环境")').click()
# driver.implicitly_wait(1)
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("请输入手机号码")')))
# driver.implicitly_wait(2)
# driver.find_element_by_id("com.shinemo.qoffice.zjcc:id/tvPhone").click()
# driver.find_element_by_id("com.shinemo.qoffice.zjcc:id/tvPhone").send_keys("13500000018")
# driver.find_element_by_id("com.shinemo.qoffice.zjcc:id/tvPasswd").click()
# driver.find_element_by_id("com.shinemo.qoffice.zjcc:id/tvPasswd").send_keys("test1234")
# driver.find_element_by_id("com.shinemo.qoffice.zjcc:id/ib_submit").click()