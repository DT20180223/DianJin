__author__ = 'zhaoyao'

import requests
from DianJin.common.log import LOG

class LOGIN():

    def __init__(self):
        self.log = LOG()

    def login(self,mobile,password):
        url = "http://djuat.dtfunds.com/fund-app/user/login"
        # 联动获取公司名称
        corporationName = self.get_corporationName(mobile)
        data = {
            "mobile":mobile,
            "corporationName":corporationName,
            "password":password
        }
        res = requests.post(url,data).json()
        print("登录成功")
        # self.log.debug_debug("登录返回信息'%s'" % (res))
        return res


    # 通过接口获取公司名称
    def get_corporationName(self,mobile):
        url = "http://djuat.dtfunds.com/fund-app/user/getCorporationNameList"
        data = {
            "mobile": mobile
        }
        res = requests.post(url,data).json()
        corporationName = res["body"][0]
        # self.log.debug_debug("用户%s,获取到公司名称'%s'" % (mobile,corporationName))
        return corporationName


if __name__=="__main__":
    login =LOGIN()
    login.login("13770506773","zy568521")