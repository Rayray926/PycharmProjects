#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-04-22 10:41 
# File: read_yaml.py

import os
import yaml

class ReadYaml:

    def __init__(self,yamlf):
        """
        初始化，判断文件是否存在
        :param yamlf: yaml配置文件路径
        """
        if os.path.exists(yamlf):
            self.yamlf=yamlf
        else:
            raise FileNotFoundError("文件不存在")
        self._data_one=None
        self._data_all=None

    #获取单个文档
    def get_data_one(self):
        #判断是否第一次读取，非第一次读取则返回上次读取的数据
        if not self._data_one:
            with open(self.yamlf,'rb') as f:
                self._data_one=yaml.safe_load(f)

        return self._data_one

    #获取所有文档
    def get_data_all(self):
        # 判断是否第一次读取，非第一次读取则返回上次读取的数据
        if not self._data_all:
            with open(self.yamlf, 'rb') as f:
                self._data_all = list(yaml.safe_load_all(f))
        return self._data_all







