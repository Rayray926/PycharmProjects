#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-04 09:48 
# File: run.py.py
"""
example
一、需求功能：
    XXXX
二、实现过程：
    XXX

"""
import  unittest
import HTMLTestRunner
from API_AUTO.tools.test_http_request import HttpTest
from API_AUTO.tools.project_path import *

suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(HttpTest))


with open(test_report_path,'wb') as file:
    runner=HTMLTestRunner.HTMLTestRunner(stream=file,
                                         verbosity=1,
                                         title='test_api单元测试',
                                         description='这个是test_api单元测试报告')


    runner.run(suite)

