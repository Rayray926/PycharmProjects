#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-04-02 12:31 
# File: get_config.py

import configparser
from project_path import case_config_path

class ReadConfig:

    def get_config(self,file_path,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_path)
        return cf.get(section,option)




if __name__ == '__main__':
    ReadConfig().get_config(case_config_path,'MODE','mode')
