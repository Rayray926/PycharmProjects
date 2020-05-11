#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-04-30 16:08 
# File: do_assert.py

from common import my_log
import json


class DoAssert:

    def __init__(self):
        self.log=my_log.Mylog()


    def assert_code(self,code,expected_code):
        """
        验证response 返回状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert int(code)==expected_code
            return True
        except :
            self.log.error("code error,code is %s,expected_code is %s"%(code,expected_code))
            raise

    def asser_body(self,body,body_msg,expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param expected_body:
        :return:
        """
        try:
            msg=body[body_msg]
            assert msg==expected_msg
            return True
        except :
            self.log.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            return True

        except:
            self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)


            raise

    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True

        except:
            self.log.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
            raise
