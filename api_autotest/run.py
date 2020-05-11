#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-04-02 11:21 
# File: run.py.py

import pytest
from common.do_shell import Shell
from common.my_log import Mylog

from conf import config
import os

if __name__ == '__main__':

    report_path = config.get_report_path() + os.sep + "result"
    report_html_path = config.get_report_path() + os.sep + "html"
    report_xml_path = config.get_report_path() + os.sep + "xml"
    shell=Shell()
    # 定义测试集
    args = ['-s', '-q', '--alluredir', report_xml_path]

    pytest.main(args)
    cmd = 'allure generate %s -o %s' % (report_xml_path , report_html_path)

    try:
        shell.invoke(cmd)
    except Exception:
        Mylog().error('执行用例失败，请检查环境配置')
        raise



