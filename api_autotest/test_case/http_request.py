#
# import sys
# import os
# sys.path.append(os.path.abspath("../common"))
# from common.do_excel import DoExcel
# from common.http_request import  HttpRequest
# # from common.common_data import CommonData
# # from common.my_log import MyLogging
# from common.do_mysql import DoMysql
# import pytest
# import allure
#
#
# # test_data=DoExcel().get_data(test_data_path)
#
# @pytest.fixture
# def before_after_action():
#     MyLogging().info("——————————开始执行测试用例——————————")
#     print(sys.path)
#     yield
#     MyLogging().info("=========测试用例执行完成==========")
#
#
@allure.feature("测试接口")
@pytest.mark.usefixtures('before_after_action')
class TestHttp():
    @pytest.mark.parametrize("item",test_data)
    def test_api(self, item): #调用请求接口

        #判断是否需要校验DB
        if item['check_database'] !=None:
            MyLogging().info("需要校验DB------{}  ".format(item))
            before_sql_result=DoMysql().do_mysql(item['check_database'])  #获取调用接口前DB数据
            MyLogging().info("掉接口前sql获得的数据是{}".format(before_sql_result))
            before_amount=before_sql_result[4]
            before_freeze_amount=before_sql_result[5]

            MyLogging().info("提现前amount 是{},提现前freeze_amount 是{},待提现金额为{}".format(before_amount,before_freeze_amount,eval(item['data'])['amount']))
            MyLogging().info("开始调用接口")
            res=HttpRequest().http_request(item['url'], eval(item['data']), item['method'],getattr(CommonData, "Cookie"))
            after_sql_result=DoMysql().do_mysql(item['check_database'])
            MyLogging().info("掉接口后sql获得的数据是{}".format(before_sql_result))
            after_amount = after_sql_result[4]
            after_freeze_amount = after_sql_result[5]
            MyLogging().info("提现后amount 是{},提现后freeze_amount 是{},待提现金额为{}".format(after_amount,after_freeze_amount,eval(item['data'])['amount']))

            #判断数据是否更新正确
            if after_amount==before_amount-eval(item['data'])['amount']:
                check_result = '数据库校验通过'
                MyLogging().info(check_result)
            else:
                check_result = '数据库未校验通过'
                MyLogging().info(check_result)

        else:
            res = HttpRequest().http_request(item['url'], eval(item['data']), item['method'],getattr(CommonData, "Cookie"))
            check_result=None

        if res.cookies: #如果返回数据cookies有值，则更新Cookie字段
            setattr(CommonData,'Cookie',res.cookies)

        try:
            print(item['expected'],res.json()['code'])
            assert item['expected']==res.json()['code']
            # self.assertEqual(item['expecxted'],res.json()['code'])
            test_result='Pass'
        except Exception as e:
            test_result = 'Fail'
            MyLogging().error("执行用例失败{}".format(e))
            raise e
        finally:
            MyLogging().info('获取到的结果是{}'.format(res.json()))
            DoExcel().write_back(test_data_path,item['sheet_name'],item['code']+1,str(res.json()),check_result,test_result)

