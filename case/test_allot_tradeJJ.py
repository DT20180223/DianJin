__author__ = 'zhaoyao'


import unittest
import requests
from DianJin.common.login import LOGIN
from DianJin.common.db_operation import DBmethod

class Allot(unittest.TestCase):

    def allot_trade(self,applyAmount,tradePwd):
        '''申购宝宝类类基金000379，申购成功'''
        login = LOGIN()
        res = login.login("13770506773","zy568521")
        token = res["body"]["token"]
        url = "http://djuat.dtfunds.com/fund-app/trade/payment"
        data = {
            "applyAmount": applyAmount,
            "sale_compare": "1000",
            "acceptProtocol": "1",
            "fundCode": "002564",
            "buyType": "JJ",
            "tradePwd": tradePwd,
            "token":token
        }

        res = requests.post(url,data).json()
        return res

    def test_allot01(self):
        '''申购精选基金002564，输入正确密码，申购成功'''
        res = self.allot_trade("10.00","568521")
        print(res)
        self.assertEqual(res["head"]["msg"],"成功",res)
        allotNo = res["body"]["allotNo"]
        print("申请协议号:%s"%(res["body"]["allotNo"]))
        return allotNo


    def test_allot02(self):
        '''申购精选基金002564，输入错误密码，申购失败'''
        res = self.allot_trade("10.00","568520")
        print(res)
        self.assertEqual(res["head"]["msg"],"交易密码输入错误",res)
        print("交易密码错误，申购失败")