__author__ = 'zhaoyao'
import unittest
import time
from DianJin.common import HTMLTestRunner_cn
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os

cur_path = os.path.dirname(os.path.realpath(__file__))
case_path = os.path.join(cur_path,"case")
cofig_Path = os.path.join(cur_path,"config\mailconfig")
print(cofig_Path)



def add_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    return discover

def run_case(all_case):
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, "reports\\")
    report_name =report_path+now+"report.html"
    fp = open(report_name, "wb")

    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title=u'自动化测试报告,测试结果如下：',description=u'用例执行情况：')
    runner.run(all_case)
    fp.close()
    send_mail(report_name,cofig_Path)

def send_mail(report_name,cofig_Path):

    config = configparser.ConfigParser()
    config.read(cofig_Path)

    sender = config.get("MAIL","sender")
    psw = config.get("MAIL","psw")
    smtp_server = config.get("MAIL","smtp_server")
    receiver = config.get("MAIL","receiver")
    port = config.get("MAIL","port")
    print(sender,psw,smtp_server,receiver,port)
    print(type(sender))

    '''发送测试报告内容'''
    with open(report_name, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"自动化测试报告"
    msg["from"] = sender
    msg["to"] = str(receiver)    # 只能字符串
    msg.attach(body)
    # 添加附件
    att = MIMEText(mail_body, "base64", _charset="utf-8")
    # att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server)                     # 连服务器
        smtp.login(sender, psw)
        print("第一个链接方式")
    except:
        smtp = smtplib.SMTP_SSL(smtp_server,port)
        smtp.login(sender, psw)                       # 登录
        print("第二个链接方式")

    smtp.sendmail(sender,receiver,msg.as_string())

    smtp.quit()
    print('test report email has send out !')



# if __name__=="__main__":
#     all_case =add_case()
#     run_case(all_case)
report_name = "F:\PycharmProjects\Study\DianJin\\reports\\2018_08_07_14_51_38report.html"
send_mail(report_name,cofig_Path)