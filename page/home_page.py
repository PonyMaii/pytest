#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/15 22:54 
# @Author : XiaoMa
# @Version：V 0.1
# @File : home_page.py
# @desc :
from base.web.base import BasePage, BaseHandle
from common.commons import HOST


class HomePage(BasePage):
    def __init__(self):
        super().__init__()

        self.get_url(HOST+"/dangdang")

    def find_login_btn(self):
        return self.get_element(*self.login_btn)

    def find_enroll_btn(self):
        return self.get_element(*self.enroll_btn)


class HomeHandle(BaseHandle):

    def __init__(self):
        self.home_page = HomePage()

    def click_login_btn(self):
        #点击登入按钮
        self.click(self.home_page.find_login_btn())

    def click_enroll_btn(self):
        #点击注册按钮
        self.click(self.home_page.find_enroll_btn())


class HomeProxy():
    def __init__(self):
        self.home_handle = HomeHandle()

    def to_login(self):
        #进入登入页面
        self.home_handle.click_login_btn()



if __name__ == '__main__':
    HomeProxy().to_login()