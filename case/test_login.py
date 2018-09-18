import unittest
import sys
import os
cur_path = os.path.dirname(os.path.dirname(os.getcwd()))
sys.path.append(cur_path)
from DianJin.common.login import LOGIN
from DianJin.common.db_operation import DBmethod

class Login(unittest.TestCase):

    def test_login(self):
        '''正确的用户名和密码登录成功'''
        login = LOGIN()
        res = login.login("13770506773","zy568521")
        name = res["body"]["name"]
        # totalAsset =  res["body"]["totalAsset"]

        self.assertEqual(name,"赵耀测试数据","用例执行错误")

    def test_login2(self):
        '''正确的用户名和错误密码'''
        login = LOGIN()
        res = login.login("18752311511","zy5685212")
        print(res)
        msg = res["head"]["msg"]
        self.assertEqual(msg,"您输入的手机号与密码不符！","用例执行错误")













