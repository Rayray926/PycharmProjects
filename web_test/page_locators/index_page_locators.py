#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-20 11:33 
# File: index_page_locators.py

from selenium.webdriver.common.by import By
class IndexPageLocators:
    """存放首页页面的元素定位数据"""

    #首页是否有用户信息展示，判断是否登录成功
    user_locate=(By.XPATH,"//*[@class='mr1 relative']")

    #今日订单金额
    today_order_amount=(By.XPATH,"//*[@class='topBlockWrapper']/div/a/p")

    #今日订单数
    today_order_count=(By.XPATH,"//*[@class='topBlockWrapper']/div[2]/a/p")

    #今日支付人数
    today_pay_count=(By.XPATH,"//*[@class='topBlockWrapper']/div[3]/a/p")

    #待发货订单数
    to_be_delivery_count=(By.XPATH,"//*[@class='bottomBlockWrapper']/div[1]/a/p")

    #站点总数
    site_count=(By.XPATH,"//*[@class='bottomBlockWrapper']/div[2]/a/p")

    #商品总数
    product_count=(By.XPATH,"//*[@class='bottomBlockWrapper']/div[3]/a/p")

    #站点管理
    site_manage=(By.XPATH,"//*[@class='itemWrapper']/a[1]/div/span")

    #商品管理
    product_manage=(By.XPATH,"//*[@class='itemWrapper']/a[2]/div/span")

    #订单管理
    order_manage=(By.XPATH,"//*[@class='itemWrapper']/a[3]/div/span")

    #预付款账户
    pre_account_manage=(By.XPATH,"//*[@class='itemWrapper']/a[4]/div/span")

    #信息设置
    setting_manage=(By.XPATH,"//*[@class='itemWrapper']/a[5]/div/span")