#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/16 16:16 
# @Author : XiaoMa
# @Version：V 0.1
# @File : test_login.py
# @desc :
import time
from page.home_page import HomeProxy
from page.login_page import LoginProxy
from tools.utils import UtilsDriver, get_case_data
import pytest
from common.commons import BASE_DIR
from tools.my_logging import getLogger

logger = getLogger()
testcase = get_case_data(BASE_DIR + "/../datas/testcase_datas/login")

@pytest.mark.team("小马团队")
class Test_Login:

    def setup_method(self):
        print("登入流程测试用例开始执行==========>")
        self.home_proxy = HomeProxy()
        self.login_proxy = LoginProxy()


    def teardown_method(self):
        #环境初始化退出webdirver
        print("环境初始化=============>")
        UtilsDriver().quit_web_driver()

    @pytest.mark.parametrize("username, password, expected",
                             testcase["p_example"])
    def test_01_login(self, username, password, expected):
        logger.info(f"{username, password, expected}")
        print(username, password, expected)
        self.home_proxy.to_login()
        time.sleep(2)
        self.login_proxy.enter(username, password)
        time.sleep(2)
        logout_text = self.home_proxy.get_logout()
        assert logout_text == expected

    @pytest.mark.parametrize("username, password, expected",
                             testcase["c_example"])
    def test_02_login(self, username, password, expected):
        logger.info(f"{username, password, expected}")
        self.home_proxy.to_login()
        time.sleep(2)
        self.login_proxy.enter(username, password)
        time.sleep(2)
        loginErr_text = self.login_proxy.get_loginErr()
        assert loginErr_text == expected

if __name__ == '__main__':
    print(testcase)
