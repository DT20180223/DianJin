__author__ = 'zhaoyao'

import pymysql
import configparser
import os
# rootDir = os.path.split(os.path.realpath(__file__))[0]

cofigFilePath =os.path.abspath('..\config') + "\dbconfig"

class DBmethod():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(cofigFilePath)
        host = config.get("MYSQL","host")
        print(host)
        port = config.get("MYSQL","port")
        user = config.get("MYSQL","user")
        passwd = config.get("MYSQL","passwd")
        db= config.get("MYSQL","db")
        charset = config.get("MYSQL","charset")
        self.conn = pymysql.connect(host=host,port=3306,user=user,passwd=passwd,db=db,charset=charset)
        self.cur = self.conn.cursor()

    def select_sql(self,sql):
        self.cur.execute(sql)
        data = self.cur.fetchall()
        self.cur.close()
        self.conn.commit()
        self.conn.close()
        return data


if __name__=="__main__":
    DB = DBmethod()
    DB.select_sql("111")

