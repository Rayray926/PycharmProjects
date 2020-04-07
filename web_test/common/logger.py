#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-21 14:43 
# File: logger.py

import logging
import web_test.common.dir_config  as dirconf

class Mylogger:

    def my_log(self,msg,level):
        my_log=logging.getLogger("API_AUTO")
        my_log.setLevel("DEBUG")

        formater=logging.Formatter("%(asctime)s - %(levelname)s -%(filename)s -%(name)s -%(lineno)d-日志信息：%(message)s ")

        fh=logging.FileHandler(dirconf.log_path)
        fh.setLevel("DEBUG")
        fh.setFormatter(formater)

        my_log.addHandler(fh)

        if level== "DEBUG":
            my_log.debug(msg)
        elif level== "INFO":
            my_log.info(msg)
        elif level=="WARNING":
            my_log.warning(msg)
        elif level=="ERROR":
            my_log.error(msg,exc_info=True)
        elif level=="CRITICAL":
            my_log.critical(msg)

        my_log.removeHandler(fh)

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

