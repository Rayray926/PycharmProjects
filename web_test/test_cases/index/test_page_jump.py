#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-20 14:20 
# File: page_jump.py



import web_test.test_datas.index_datas as ID
from web_test.page_object.porder_page import POrderPage
from web_test.common.logger import Mylogger
import pytest

@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("page_back")
class TestIndexPageJump():
    """首页超链接跳转"""

    #跳转购物订单

    @pytest.mark.parametrize("podata",ID.to_porder)
    def test_jumpTo_Porder(self,podata,access_web):

        Mylogger().info("****礼品商后台_首页跳转_跳转至购物订单页****")
        access_web.href_jump(podata)
        print(access_web)
        try:
            assert POrderPage(access_web).isExist_order_ele()
        except AssertionError:
            Mylogger().error("断言失败")
            raise

    #
    # @pytest.mark.parametrize("prdata", ID.to_products)
    # def test_jumpTo_products(self,prdata,access_web):
    #     Mylogger().info("****礼品商后台_首页跳转_跳转至商品列表页****")
    #     access_web.href_jump(prdata)
    #     try:
    #         assert ProductPage(access_web).isExist_product_ele()
    #     except AssertionError:
    #         Mylogger().error("断言失败")
    #     # self.assertTrue(ProductPage(self.driver).isExist_product_ele())
    #
    # @pytest.mark.parametrize("stdata", ID.to_site)
    # def test_jumpTo_site(self,stdata,access_web):
    #     Mylogger().info("****礼品商后台_首页跳转_跳转至站点列表页****")
    #     access_web.href_jump(stdata)
    #     try:
    #         assert SitePage(access_web).isExsit_site_ele()
    #     except AssertionError:
    #         Mylogger().error("断言失败")
    #     # self.assertTrue(SitePage(self.driver).isExsit_site_ele())
    #
    #
    # @pytest.mark.parametrize("prdata", ID.to_pre_account)
    # def test_test_jumpTo_preaccount(self,prdata,access_web):
    #     Mylogger().info("****礼品商后台_首页跳转_跳转至预付款账户页****")
    #     access_web.href_jump(prdata)
    #     try:
    #         assert Preaccountpage(access_web).isExsit_preaccount_ele()
    #     except AssertionError:
    #         Mylogger().error("断言失败")
    #         # self.assertTrue(Preaccountpage(self.driver).isExsit_preaccount_ele())
    #
    #
    # @pytest.mark.parametrize("stingdata", ID.to_setting)
    # def test_test_jumpTo_sitting(self,stingdata,access_web):
    #     Mylogger().info("礼品商后台_首页跳转_跳转至设置页")
    #     access_web.href_jump(stingdata)
    #     try:
    #         assert SettingPage(access_web).isExist_setting_ele()
    #     except AssertionError:
    #         Mylogger().error("断言失败")
    #         # self.assertTrue(SettingPage(self.driver).isExist_setting_ele())
    #



