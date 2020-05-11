#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-04-22 10:30 
# File: readYml.py


import os
from common.read_yaml import ReadYaml

#项目路径,私有变量，只有本模块内方法可访问
_project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
#测试用例路径
_test_data_path=_project_path+os.sep+"test_data"+os.sep+"test_data.xlsx"
#日志路径
_log_path=_project_path+os.sep+"log"
#测试报告路径
_report_path=_project_path+os.sep+"report"
#配置文件yaml路径
_configf_path=_project_path+os.sep+"conf"+os.sep+"conf.yml"

def get_project_path():
    return _project_path

def get_test_data_path():
    return _test_data_path

def get_log_path():
    return _log_path

def get_report_path():
    return _report_path

def get_configf_path():
    return _configf_path


class ConfigYaml:

    def __init__(self):
        self.config=ReadYaml(get_configf_path()).get_data_one()

    #返回运行运行模块的sheet名称
    def get_test_module(self):

        return self.config["TEST_MODULE"]
    #返回需要运行的环境
    def get_test_environment(self):

        return self.config["TEST_ENVIRONMENT"]

    def get_debug_environment(self):
        return self.config["DEBUG_ENVIRONMENT"]

    def get_release_environment(self):
        return self.config["RELEASE_ENVIRONMENT"]


if __name__ == '__main__':
    t=ConfigYaml().get_release_environment()
    print(t)