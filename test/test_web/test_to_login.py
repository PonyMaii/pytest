#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/16 1:09 
# @Author : XiaoMa
# @Version：V 0.1
# @File : test_to_login.py
# @desc :

from page.home_page import HomeProxy
from tools.utils import UtilsDriver


class Test_HomePage:

    def setup_class(self):
        print("用例执行开始===========>")

    def test_to_login(self):
        HomeProxy().to_login()