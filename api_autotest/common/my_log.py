#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-06 13:17
# File: my_log.py

"""
功能：提供收集日志能力
不同级别的日志分不同文件保存，文件名如下：error.log.2020-01-01
调用不同级别打印日志时，创建对应handler
"""

import logging
import os
from conf.config import get_log_path
import  datetime


def create_file(level):
    file_path=get_log_path()+os.sep+level+'.log.'+datetime.datetime.now().strftime("%Y-%m-%d")
    if not os.path.exists(file_path):
        file=open(file_path,'wb')
        file.close()
    return file_path

class Mylog:
    def __init__(self):
        self.logger=logging.getLogger("test_api")
        self.logger.setLevel("DEBUG")
        if not self.logger.handlers:
            fh_stream=logging.StreamHandler()
            fh_stream.setLevel("DEBUG")
            fh_stream.setFormatter(self.set_formatter())
            self.logger.addHandler(fh_stream)


    def debug(self,msg):
        self.add_handler("debug")
        self.logger.debug(msg)
        self.remove_handler("debug")

    def warning(self,msg):
        self.add_handler("warning")
        self.logger.warning(msg)
        self.remove_handler("warning")

    def info(self, msg):
        self.add_handler("info")
        self.logger.info(msg)
        self.remove_handler("info")

    def error(self,msg):
        self.add_handler("error")
        self.logger.error(msg)
        self.remove_handler("error")

    def critical(self,msg):
        self.add_handler("critical")
        self.logger.critical(msg)
        self.remove_handler("critical")

    def  add_handler(self,level):
        if level.lower() == "debug":
            self.debug_fh = logging.FileHandler(create_file("debug"))
            self.debug_fh.setLevel("DEBUG")
            self.debug_fh.setFormatter(self.set_formatter())
            self.logger.addHandler(self.debug_fh)

        elif level.lower() == "warning":
            self.warning_fh = logging.FileHandler(create_file("warning"))
            self.warning_fh.setLevel("WARNING")
            self.warning_fh.setFormatter(self.set_formatter())
            self.logger.addHandler(self.warning_fh)

        elif level.lower() == "info":
            self.info_fh = logging.FileHandler(create_file("info"))
            self.info_fh.setLevel("INFO")
            self.info_fh.setFormatter(self.set_formatter())
            self.logger.addHandler(self.info_fh)

        elif level.lower() == "error":
            self.error_fh = logging.FileHandler(create_file("error"))
            self.error_fh.setLevel("ERROR")
            self.error_fh.setFormatter(self.set_formatter())
            self.logger.addHandler(self.error_fh)

        else:
            self.critical_fh = logging.FileHandler(create_file("critical"))
            self.critical_fh.setLevel("CRITICAL")
            self.critical_fh.setFormatter(self.set_formatter())
            self.logger.addHandler(self.critical_fh)


    def remove_handler(self,level):
        if level.lower() == "debug":
            self.logger.removeHandler(self.debug_fh)
        elif level.lower() == "warning":
            self.logger.removeHandler(self.warning_fh)
        elif level.lower() == "info":
            self.logger.removeHandler(self.info_fh)
        elif level.lower() == "error":
            self.logger.removeHandler(self.error_fh)
        else:
            self.logger.removeHandler(self.critical_fh)



    def set_formatter(self):
        # return  logging.Formatter("%(asctime)s %(levelname)s %(filename)s %(name)s %(lineno)d 日志信息：%(message)s ")
        return logging.Formatter('%(asctime)s  %(name)s %(levelname)s %(message)s')




if __name__ == '__main__':
    Mylog().debug("debug")
    # Mylog().error("error")
    # Mylog().info("info")
    # Mylog().warning("warning")
    # Mylog().critical("critical")



