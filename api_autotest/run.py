#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-04-02 11:21 
# File: run.py.py

import unittest
import HTMLTestRunner
from common.project_path import test_report_path
from common.test_http_request import HttpTest

suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(HttpTest))

with open(test_report_path,'wb') as file:
    runner=HTMLTestRunner.HTMLTestRunner(stream=file,verbosity=1,title='api_autotest 测试报告',description='这是api_autotest 测试报告')
    runner.run(suite)
