#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/15 22:55 
# @Author : XiaoMa
# @Version：V 0.1
# @File : login_page.py
# @desc :
from base.web.base import BasePage, BaseHandle
import time

class LoginPage(BasePage):
    def __init__(self):
        super().__init__()

    def find_title_info(self):
        #定位title元素
        return self.get_element(*self.title)

    def find_user_input(self):
        #定位用户输入框
        return self.get_element(*self.user_input)

    def find_pwd_input(self):
        #定位密码输入框
        return self.get_element(*self.pwd_input)

    def find_enter_btn(self):
        #定位确认按钮
        return self.get_element(*self.enter_btn)

    def find_loginErr_info(self):
        return self.get_element(*self.loginErr_info)



class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    def get_title_info(self):
        #获取title运行信息
        return self.get_text(self.login_page.find_title_info())

    def send_user_input(self, username):
        self.input_text(self.login_page.find_user_input(), username)

    def send_pwd_input(self, password):
        self.input_text(self.login_page.find_pwd_input(), password)

    def click_enter_btn(self):
        self.click(self.login_page.find_enter_btn())

    def get_loginErr_inf(self):
        return self.get_text(self.login_page.find_loginErr_info())

class LoginProxy():
    def __init__(self):
        self.login_handle = LoginHandle()

    def get_title(self):
        return self.login_handle.get_title_info()

    def enter(self, username, password):
        #登入
        self.login_handle.send_user_input(username)
        self.login_handle.send_pwd_input(password)
        self.login_handle.click_enter_btn()

    def get_loginErr(self):
        #获取登入错误信息
        return self.login_handle.get_loginErr_inf()


if __name__ == '__main__':
    from page.home_page import HomeProxy
    home_proxy = HomeProxy()
    home_proxy.to_login()
    time.sleep(2)
    LoginProxy().enter("xiaoma@126.com", "123456")