#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-21 14:42 
# File: dir_config.py


import  os

#项目路径
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#截图路径
screenshot_path=os.path.join(project_path,'Outputs/screenshot')

#日志路径
log_path=os.path.join(project_path,'Outputs','logs','log.txt')

#测试数据路径
test_datas_path=os.path.join(project_path,'test_datas')

#测试用例路径
test_cases_path=os.path.join(project_path,'test_cases')

#测试报告路径
report_path=os.path.join(project_path,'Outputs/report')