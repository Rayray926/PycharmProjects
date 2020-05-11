#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-21 15:59 
# File: run.py.py

import unittest
import HTMLTestRunner

import web_test.common.dir_config as dirconf

suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.discover(dirconf.test_cases_path+'/modelA'))

print(suite)

# discover=unittest.defaultTestLoader.discover(dirconf.test_cases_path+"/login",pattern='test_')
# print(discover)
# now = time.strftime("%Y-%m-%d_%H_%M_%S")
# file_name=dirconf.report_path+'\\' + now + 'result.html'

with open(dirconf.report_path+'/auto_Test.html','wb') as file:
    runner=HTMLTestRunner.HTMLTestRunner(stream=file,
                                         verbosity=1,
                                         title='测试报告',
                                         description='用例执行情况')


    runner.run(suite)
