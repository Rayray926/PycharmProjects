#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-04-02 20:28 
# File: do_mysql.py

import  pymysql
from common.my_log import Mylog


class DoMysql:
    def do_mysql(self,query,fetch='one'):
        conn=pymysql.connect(
            host='10.0.10.42',
            port=3306,
            user='root',
            password='shinemo123',
            database='saas',
            charset='utf8')

        cur=conn.cursor()
        Mylog().info("操作的sql是：{}".format(query))
        cur.execute(query)
        if fetch=='all':
            data=cur.fetchall()
        else:
            data=cur.fetchone()
        return data



if __name__ == '__main__':
    t=DoMysql().do_mysql('select * from payment_account where gift_dealer_id=21','all')
    print(t,t[0][4])

