__author__ = 'zhaoyao'


import unittest
import requests
import sys
import os
cur_path = os.path.dirname(os.getcwd())
sys.path.append(cur_path)

from DianJin.common.login import LOGIN
from DianJin.common.db_operation import DBmethod

#测试git提交
#有改变的啊
class Allot(unittest.TestCase):

    def allot_trade(self,applyAmount,tradePwd):
        u'''申购宝宝类类基金000379，申购成功'''
        login = LOGIN()
        res = login.login("13770506773","zy568521")
        token = res["body"]["token"]
        url = "http://djuat.dtfunds.com/fund-app/trade/payment"
        data = {
            "applyAmount": applyAmount,
            "sale_compare": "1",
            "acceptProtocol": "1",
            "fundCode": "000379",
            "buyType": "BB",
            "tradePwd": tradePwd,
            "token":token
        }

        res = requests.post(url,data).json()
        return res

    def test_allot01(self):
        u'''申购宝宝类类基金000379，输入正确密码，申购成功'''
        res = self.allot_trade("1000","568521")
        self.assertEqual(res["head"]["msg"],"成功",res)
        print("申请协议号:%s"%(res["body"]["allotNo"]))

    def test_allot02(self):
        '''申购宝宝类类基金000379，输入错误密码，申购失败'''
        res = self.allot_trade("1000","568520")
        self.assertEqual(res["head"]["msg"],"交易密码输入错误",res)
        print("交易密码错误，申购失败")