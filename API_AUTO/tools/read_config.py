#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-04 16:22 
# File: read_config.py
"""
example
一、需求功能：
    XXXX
二、实现过程：
    XXX

"""
import configparser

class ReadConfig:

    @staticmethod
    def get_config(file_path,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]

# if __name__ == '__main__':
#     from API_AUTO.tools import project_path
#     print(eval(ReadConfig.get_config(project_path.config_path,'MODE','mode')))
