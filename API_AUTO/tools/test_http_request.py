#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-04 14:24 
# File: test_http_request.py


import  unittest
from API_AUTO.tools.http_request import HttpRequest
from API_AUTO.tools.get_cookies import GetData
from ddt import ddt ,data
from API_AUTO.tools.do_excel import DoExcel
from API_AUTO.tools.project_path import *
from API_AUTO.tools.my_log import Mylogger
from API_AUTO.tools.do_mysql import DoMysql

my_log=Mylogger()
test_data=DoExcel().get_data(test_case_path)

@ddt
class HttpTest(unittest.TestCase):

    def setUp(self):
        my_log.info("-----开始执行测试用例-----")

    @data(*test_data)
    def test_api(self,item):

        if item['check_database'] !=None:
            my_log.info(".....此条用例需要校验数据库.....")
            before_freeze_amount=DoMysql().do_mysql(item['check_database'])[0][5]
            my_log.info('执行用例{0}前DB冻结余额为{1},提现金额为{2}'.format(item['title'],before_freeze_amount,eval(item['data'])['amount']))
            my_log.info("开始调用接口")
            res = HttpRequest().http_test(item['url'], eval(item['data']), item['method'], getattr(GetData, "Cookie"))
            my_log.info('接口调用完成')
            my_log.info('执行用例{0}后查看数据库'.format(item['title']))
            after_freeze_amount = DoMysql().do_mysql(item['check_database'])[0][5]
            my_log.info('执行用例{0}后DB冻结余额为{1}'.format(item['title'],after_freeze_amount))
            if after_freeze_amount==before_freeze_amount+eval(item['data'])['amount']:
                check_result='数据库校验通过'
                my_log.info(check_result)
            else:
                check_result = '数据库校验未通过'
                my_log.info(check_result)
        else:

            res = HttpRequest().http_test(item['url'], eval(item['data']), item['method'],
                                              getattr(GetData, "Cookie"))
            check_result=None

        if res.cookies:
            setattr(GetData,'Cookie',res.cookies)
        try:
            self.assertEqual(item['expected'],res.json()['code'])
            TestResult='PASS'
        except Exception as e:
            TestResult = 'Failed'
            my_log.error("执行用例出错误了{}".format(e))
            raise e
        finally:
            my_log.info("获取到的结果是：{}".format(res.json()))
            DoExcel().wirte_back(test_case_path,item['sheet_name'],item['code']+1,str(res.json()),TestResult,check_result)
    def tearDown(self):
        my_log.info("----测试用例执行完成-----")


if __name__ == '__main__':
    HttpTest().test_api()
