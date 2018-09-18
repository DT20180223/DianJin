__author__ = 'zhaoyao'


import unittest
import requests
import sys
import os
cur_path = os.path.dirname(os.path.dirname(os.getcwd()))
sys.path.append(cur_path)
from DianJin.common.login import LOGIN
from DianJin.common.db_operation import DBmethod

class Allot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        login = LOGIN()
        res = login.login("13770506773","zy568521")
        cls.token = res["body"]["token"]
        print(cls.token)
        print("测试多个用例只执行一次")
    # def setUp(self):
    #     '''每条用例执行前的操作'''
    #     login = LOGIN()
    #     res = login.login("13770506773","zy568521")
    #     self.token = res["body"]["token"]

    def allot_trade(slef,applyAmount,tradePwd):
        '''申购宝宝类类基金000379，申购成功'''
        token = slef.token
        print(token)
        url = "http://djuat.dtfunds.com/fund-app/trade/payment"
        data = {
            "applyAmount": applyAmount,
            "sale_compare": "1000",
            "acceptProtocol": "1",
            "fundCode": "210008",
            "buyType": "HQ",
            "tradePwd": tradePwd,
            "token":token
        }

        res = requests.post(url,data).json()
        return res

    def test_allot01(self):
        '''申购活期类基金210008，输入正确密码，申购成功'''
        res = self.allot_trade("10000.00","568521")
        # print(res)
        self.assertEqual(res["head"]["msg"],"成功",res)
        print("申请协议号:%s"%(res["body"]["allotNo"]))

    # def test_allot02(self):
    #     '''申购活期类基金210008，输入错误密码，申购失败'''
    #     res = self.allot_trade("1000.00","568520")
    #     print(res)
    #     self.assertEqual(res["head"]["msg"],"交易密码输入错误",res)
    #     print("交易密码错误，申购失败")

    def test_allot03(self):
        '''申购活期类基金210008，申购金额小于追加金额，申购失败'''
        res = self.allot_trade("1000.00","568521")
        # print(res)
        self.assertEqual(res["head"]["msg"],"申请失败",res)
        print("交易密码错误，申购失败")