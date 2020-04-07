#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-04-01 14:33 
# File: project_path.py


import  os

#项目路径
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#测试用例路径
test_data_path=os.path.join(project_path,'test_data','test_data.xlsx')

#日志路径
log_path=os.path.join(project_path,'test_result','log','test_api_log.txt')

#测试报告路径
test_report_path=os.path.join(project_path,'test_result','test_report','test_report.html')

#配置文件目录
case_config_path=os.path.join(project_path,'conf','case_config.py')