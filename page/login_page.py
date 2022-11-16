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


class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    def get_title_info(self):
        #获取title运行信息
        return self.get_text(self.login_page.find_title_info())

class LoginProxy():
    def __init__(self):
        self.login_handle = LoginHandle()

    def get_title(self):
        time.sleep(2)
        return self.login_handle.get_title_info()



