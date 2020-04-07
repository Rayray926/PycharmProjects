#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-20 10:16 
# File: login_page_locators.py


from selenium.webdriver.common.by import By
class LoginPageLocators:

    """存放登录页面的元素定位数据"""

    #手机号
    name_text=(By.XPATH,"//input[@id='phone']")
    #密码
    pwd_text=(By.XPATH,"//input[@id='pass']")
    #登录按钮
    login_but=(By.XPATH,"//div[@class='login__form f-14']/div[4]")
    #页面toast错误提示
    err_msg=(By.XPATH,"//*[@class='ant-message-notice-content']")
    # 页面toast错误提示locate,等待该元素出现
    err_msg_locate=(By.XPATH,"//*[@class='ant-message-notice-content']")


