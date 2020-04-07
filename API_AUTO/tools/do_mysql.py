#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-01-07 11:51 
# File: do_mysql.py

import pymysql


class DoMysql:

    def do_mysql(self,query,fetch='all'):

        conn = pymysql.connect(
            host='10.0.10.42',
            port = 3306,
            user = 'root',
            password = 'shinemo123',
            database='saas',
            charset = 'utf8')


        cur=conn.cursor()
        query_sql=query
        cur.execute(query_sql)
        if fetch =='all':
            data=cur.fetchall()
        else:
            data = cur.fetchone()

        return data

if __name__ == '__main__':
    t=DoMysql().do_mysql('select * from payment_account where gift_dealer_id=21' )
    print(t,t[0][4],t[0][5])


