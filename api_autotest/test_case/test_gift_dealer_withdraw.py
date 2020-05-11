#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-05-02 10:46 
# File: test_gift_dealer_withdraw.py

import sys
import os
sys.path.append(os.path.abspath("../common"))
from common.do_excel import  DoExcel
from common.my_log import Mylog
from conf import config
from common.do_mysql import DoMysql
from common.http_request import  HttpRequest
from common.do_assert import  DoAssert
import pytest
import allure


test_data_path = config.get_test_data_path()
test_data = DoExcel(test_data_path).get_module_test_data('withdraw')
print(test_data)

@allure.feature("提现")
class TestGiftDealerWithdraw:

    @pytest.mark.parametrize("item",test_data)
    def test_withdraw(self,item):
        """
        登录状态下，提现成功
        :return:
        """

        # 判断是否需要校验DB
        if item['check_database'] != None:
            Mylog().info("需要校验DB------{}  ".format(item))
            before_sql_result = DoMysql().do_mysql(item['check_database'])  # 获取调用接口前DB数据
            Mylog().info("掉接口前sql获得的数据是{}".format(before_sql_result))
            before_amount = before_sql_result[4]
            before_freeze_amount = before_sql_result[5]

            Mylog().info("提现前amount 是{},提现前freeze_amount 是{},待提现金额为{}".format(before_amount, before_freeze_amount,
                                                                                  eval(item['data'])['amount']))
            Mylog().info("开始调用接口")
            res = HttpRequest().get_request(item['url'], eval(item['data'])) #返回dict类型
            after_sql_result = DoMysql().do_mysql(item['check_database'])
            Mylog().info("掉接口后sql获得的数据是{}".format(before_sql_result))
            after_amount = after_sql_result[4]
            after_freeze_amount = after_sql_result[5]
            Mylog().info("提现后amount 是{},提现后freeze_amount 是{},待提现金额为{}".format(after_amount, after_freeze_amount,
                                                                                  eval(item['data'])['amount']))

            # 判断数据是否更新正确
            if after_freeze_amount == before_freeze_amount + eval(item['data'])['amount']:
                check_result = '数据库校验通过'
                Mylog().info(check_result)
            else:
                check_result = '数据库未校验通过'
                Mylog().info(check_result)
        else:
            res = HttpRequest().get_request(item['url'], eval(item['data']))
            check_result=None
            print(res,type(res))


        try:
            DoAssert().assert_code(item['expected'],res['code'])
            # assert item['expected']==res.json()['code']
            # self.assertEqual(item['expecxted'],res.json()['code'])
            test_result='Pass'
        except Exception as e:
            test_result = 'Fail'
            Mylog().error("执行用例失败{}".format(e))
            raise e
        finally:
            pass
            Mylog().info('获取到的结果是{}'.format(res))
            DoExcel(test_data_path).write_back("gift_dealer_manage",item['case_id']+1,str(res),check_result,test_result)

if __name__ == '__main__':
    TestGiftDealerWithdraw()
