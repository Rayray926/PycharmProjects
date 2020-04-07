#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-20 14:46 
# File: index_datas.py

from web_test.page_locators.index_page_locators import IndexPageLocators as inc


#跳转至购物订单页
to_porder=[inc.today_order_amount,inc.today_order_count,inc.today_pay_count,inc.to_be_delivery_count,inc.order_manage]

#跳转至商品列表页
to_products=[inc.product_count,inc.product_manage]

#跳转至站点列表页
to_site=[inc.site_count,inc.site_manage]

#跳预付款
to_pre_account=[inc.pre_account_manage]

#跳设置页
to_setting=[inc.setting_manage]
