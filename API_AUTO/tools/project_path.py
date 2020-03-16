#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-04 15:33
# File: project_path.py
"""
example
一、需求功能：
    XXXX
二、实现过程：
    XXX

"""
import os

project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#测试用例的路径
test_case_path=os.path.join(project_path,'test_data','test_data.xlsx')

#测试报告的路径
test_report_path=os.path.join(project_path,'test_result','html_report','test_api.html')

#cofig的路径
config_path=os.path.join(project_path,'conf','case_config.py')

#log的路径
log_path=os.path.join(project_path,'test_result','log','test_api_log.txt')

