#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-05-11 19:28 
# File: do_shell.py

import  subprocess

class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()  #subprocess.PIPE 表示为子进程创建新的管道
        o = output.decode("utf-8")
        return o

if __name__ == '__main__':

    print(Shell.invoke("ls"))