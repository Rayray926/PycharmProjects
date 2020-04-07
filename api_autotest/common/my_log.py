#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-04-01 18:34 
# File: my_log.py

import logging
from project_path import log_path
from logging import handlers

class MyLogging:

    def my_log(self,msg,level):
        """
        1. 创建日志收集器，设置日志输出级别
        2. 添加日志处理器，有3种常见处理器，设置处理器级别，以及日志格式
        ps: 打印完日志后需要移除处理器，否则会重复打印日志(第二次打印内容包括第一次的日志内容)
        :return:
        """
        logger=logging.getLogger('api_autotest')
        logger.setLevel("DEBUG")
        formatter=logging.Formatter("%(asctime)s - %(levelname)s -%(filename)s -%(funcName)s -%(lineno)d-日志信息：%(message)s ")
        fh=handlers.TimedRotatingFileHandler(filename=log_path,when='S')
        # fh=logging.FileHandler(log_path)
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        
        if level=='DEBUG':
            logger.debug(msg)

        elif level=="INFO":
            logger.info(msg)

        elif level=="WARNING":
            logger.warning(msg)

        elif level=="ERROR":
            logger.error(msg)

        elif level=="CRITICAL":
            logger.critical(msg)

        logger.removeHandler(fh)
        
    def debug(self,msg):
        self.my_log(msg,"DEBUG")

    def info(self,msg):
        self.my_log(msg,"INFO")

    def warning(self,msg):
        self.my_log(msg,"WARNING")

    def error(self,msg):
        self.my_log(msg,"ERROR")

    def critical(self,msg):
        self.my_log(msg,"CRITICAL")
        
        

if __name__ == '__main__':
    MyLogging().error("111111")
    MyLogging().debug("111111")