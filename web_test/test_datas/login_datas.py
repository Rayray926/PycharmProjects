#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-16 14:11 
# File: login_datas.py

"""存放登录页所需要的测试数据"""

#正常登录
success_login_data=[{"mobile":'15634116913','pwd':"123qazxsw"}]

#异常登录,手机号不存在、密码错误,手机号为空，密码为空，均为空,手机号不符合长度等
failed_login_data=[
    {"mobile":'15634116919','pwd':"123qazxsw",'check':'账号或密码错误'},
    {"mobile":'15634116913','pwd':"123qazwww",'check':'账号或密码错误'},
    {"mobile":'','pwd':"123qazxsw",'check':'登录账号不能为空'},
    {"mobile":'15634116919','pwd':"",'check':'密码不能为空'},
    {"mobile":'','pwd':"",'check':'登录账号不能为空'},
    {"mobile":'1563411691300','pwd':"123qazxsw",'check':'账号或密码错误'},
]