#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/16 1:09 
# @Author : XiaoMa
# @Version：V 0.1
# @File : test_to_login.py
# @desc :
import pytest
from page.home_page import HomeProxy
from page.login_page import LoginProxy
from tools.utils import UtilsDriver
import time

@pytest.mark.team("李四团队")
class Test_HomePage:

    def setup_class(self):
        print("用例执行开始===========>")
        self.home_proxy = HomeProxy()
        self.login_proxy = LoginProxy()


    def test_to_login(self):
        self.home_proxy.to_login()
        time.sleep(2)
        login_page_title = self.login_proxy.get_title()
        assert login_page_title == "登录 - 当当网"

    def teardown_class(self):
        UtilsDriver().quit_web_driver()