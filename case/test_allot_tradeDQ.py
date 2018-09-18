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

    def allot_trade(self,applyAmount,tradePwd):
        '''申购宝宝类类基金000379，申购成功'''
        login = LOGIN()
        res = login.login("13770506773","zy568521")
        token = res["body"]["token"]
        url = "http://djuat.dtfunds.com/fund-app/trade/payment"
        data = {
            "applyAmount": applyAmount,
            "sale_compare": "1000000",
            "acceptProtocol": "1",
            "fundCode": "202306",
            "buyType": "DQ",
            "tradePwd": tradePwd,
            "token":token
        }

        res = requests.post(url,data).json()
        return res

    def test_allot01(self):
        u'''申购活期类基金210008，输入正确密码，申购成功'''
        res = self.allot_trade("100000000.00","568521")
        print(res)
        self.assertEqual(res["head"]["msg"],"成功",res)
        # print("申请协议号:%s"%(res["body"]["allotNo"]))
        # 需要查库操作，目前测试库链接不上，暂不校验

    def test_allot02(self):
        '''申购活期类基金210008，输入错误密码，申购失败'''
        res = self.allot_trade("1000000.00","568520")
        print(res)
        self.assertEqual(res["head"]["msg"],"交易密码输入错误",res)
        print("交易密码错误，申购失败")

    def test_allot03(self):
        '''定期理财，输入的申购金额小于最小起投金额'''
        res = self.allot_trade("1000.00","568521")
        print(res)
        self.assertEqual(res["head"]["msg"],"申请失败","接口没有判断最小申购金额")
        # print("交易密码错误，申购失败")