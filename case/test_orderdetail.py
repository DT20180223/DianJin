__author__ = 'zhaoyao'

import unittest
import sys
import os
cur_path = os.path.dirname(os.path.dirname(os.getcwd()))
sys.path.append(cur_path)
from DianJin.common.login import LOGIN
from DianJin.common.db_operation import DBmethod
import requests

class Login(unittest.TestCase):

    def test_orderdetail(self):

        login = LOGIN()
        res_login = login.login("13770506773","zy568521")
        data ={
            "token": res_login["body"]["token"],
            "type":"JJ",
            "pageIndex":"1",
        }

        url = "http://djuat.dtfunds.com/fund-app/trade/queryUserTransRecord"
        res = requests.post(url,data).json()
        # print(res)
        account = int(res["body"]["totalNumber"])
        if account > 1:
            orderNo = res["body"]["items"][0]["orderNo"]
            url ="http://djuat.dtfunds.com/fund-app/order/getOrderDetail"
            data ={
                "token": res_login["body"]["token"],
                "orderNo":orderNo
            }
            res= requests.post(url,data).json()
            self.assertEqual(res["head"]["msg"],"成功","测试失败，")

















