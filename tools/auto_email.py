#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/21 2:13 
# @Author : XiaoMa
# @Version：V 0.1
# @File : auto_email.py
# @desc :
import smtplib
from email.mime.text import MIMEText  #邮件正文类
from email.utils import formataddr  #邮件地址格式化的函数
from email.mime.multipart import MIMEMultipart  #邮件格式类

import time
from tools.utils import get_yaml
from config import BASE_DIR

email_data = get_yaml(BASE_DIR+"/datas/email")

''' 把发邮件的功能封装到类中 '''
class AutoEmail():
    def __init__(self):
        # 配置SMTP发件服务器。例如qq邮箱发件服务器：smtp.qq.com
        self.mail_host = email_data["mail_host"]
        # 发件服务器的ssl协议端口号默认465
        self.mail_port = 465
        # 发件人账号
        self.mail_user = email_data["mail_user"]
        # 发件人邮箱授权码
        self.mail_password = email_data["mail_password"]
        # 发件人地址，与发件人账号一致
        self.mail_sender = email_data["mail_sender"]
        # 收件人邮箱地址
        self.mail_receives = email_data["mail_receives"]

    def send_email(self, report, username, theme="dangdang系统测试报告", report_name="test_report"):
            """ report记录测试报告html文件的地址 """
        # try:
            # 1.创建邮件对象：MIMEMultipart对象(支持各种类型的邮件，比如纯文本、超文本、内嵌资源(图片等)、带附件)
            msg = MIMEMultipart('mixed')
            # 设置邮件的主题(标题)
            msg['Subject'] = f"主题：{theme}"
            # 设置发件人昵称、发件人地址
            msg['From'] = formataddr((f"发送者：{username}", self.mail_sender))
            # 设置多个收件人,通过join将列表转换为以;为间隔的字符串：'2293913554@qq.com;crowbrother@126.com'
            msg['To'] = ';'.join(self.mail_receives)

            # 1.1设置正文
            my_text = '''各位领导、同事，下午好：
                         这是xx系统的自动化测试报告...                                   
                      '''
            text_plain = MIMEText(my_text, 'plain', 'utf-8')
            # 添加 MIMEText 对象
            msg.attach(text_plain)

            # 1.2设置附件
            my_file = open(report, 'rb').read()
            # 字节通过base64编码成ASCII字符串来发送，可方便传输任意数据(字符或字节)
            file = MIMEText(my_file, 'base64', 'utf-8')
            # 添加请求头信息，设置为附件形式
            report_name = report_name
            file.add_header('Content-Disposition', rf'attachment;filename="{report_name}.html"')
            # 添加 MIMEText 对象
            msg.attach(file)


            # 2.发送邮件
            # 2.1 确定SMTP发件服务器。
            send_server = smtplib.SMTP_SSL(self.mail_host, self.mail_port)
            # 2.2登录发件服务器(验证权限)。传入邮箱账号、邮箱授权码（密码）
            send_server.login(self.mail_user, self.mail_password)
            # 2.3发送邮件。传入发件人邮箱地址、收件人邮箱地址、整个邮件内容
            send_server.sendmail(self.mail_sender, self.mail_receives, msg.as_string())
            # 2.4 退出发件服务器
            send_server.quit()
            print("邮件发送成功...")

        # except Exception as e:
            # 捕捉异常对象，并打印出来
            # print(e)
            # print("邮件发送失败...")

if __name__ == '__main__':
    from pprint import pprint
    pprint(email_data)
    ae = AutoEmail() #创建邮箱类的对象
    report = (BASE_DIR+"/report/report.html").replace("\\", "/")
    ae.send_email(report, "小马", "dangdang Web Ui Test")