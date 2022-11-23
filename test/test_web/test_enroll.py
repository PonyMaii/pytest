#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/19 20:10 
# @Author : XiaoMa
# @Version：V 0.1
# @File : test_enroll.py
# @desc :
import time
from tools.utils import UtilsDriver, get_case_data
from page.home_page import HomeProxy
from page.enroll_page import EnrollProxy
import pytest
from common.commons import BASE_DIR
from tools.dd_mysql import d_mysql
from tools.my_logging import getLogger
logger = getLogger()

case_data = get_case_data(BASE_DIR+r"/../datas/testcase_datas/enroll")


@pytest.mark.user("小马")
class TestEnroll:

    def setup_method(self):
        self.home_proxy = HomeProxy()
        self.enrool_proxy = EnrollProxy()


    def teardown_method(self):
        UtilsDriver().quit_web_driver()

    def teardown_class(self):
        d_mysql.Delete(table_name="`dang`.`d_user`",
                       condition=f"email=+'{case_data['p_example'][0][0]}'")

    @pytest.mark.parametrize("email,nikename,pwd,repwd,check_code,expected1,expected2",
                             case_data['p_example'])
    def test_case01_enroll(self, email, nikename, pwd, repwd,
                           check_code, expected1, expected2):
        logger.info([email, nikename, pwd, repwd, check_code, expected1, expected2])
        self.home_proxy.to_enroll()
        self.enrool_proxy.enroll_user(email, nikename, pwd, repwd, str(check_code)+"\n")
        time.sleep(2)
        #点击注册按钮
        self.enrool_proxy.click_enroll()
        time.sleep(2)
        self.enrool_proxy.click_enroll()
        time.sleep(2)
        assert self.enrool_proxy.get_write_in() == expected1
        #点击确认邮箱验证码
        time.sleep(2)
        self.enrool_proxy.click_ent_code()
        time.sleep(2)
        assert expected2 in self.enrool_proxy.get_login_bj()

    @pytest.mark.parametrize("email,nikename,pwd,repwd,check_code,expected",
                             case_data["email_err_example"])
    def test_email_err_enroll(self, email, nikename, pwd, repwd, check_code, expected):
        logger.info(f"{email, nikename, pwd, repwd, check_code, expected}")
        self.home_proxy.to_enroll()
        self.enrool_proxy.enroll_user(email, nikename, pwd, repwd, check_code)
        time.sleep(2)
        assert self.enrool_proxy.get_email_err() == expected

    @pytest.mark.parametrize("email,nikename,pwd,repwd,check_code,expected",
                             case_data["nikename_err_example"])
    def test_nikename_err_enroll(self, email, nikename, pwd, repwd, check_code, expected):
        logger.info(f"{email, nikename, pwd, repwd, check_code, expected}")
        self.home_proxy.to_enroll()
        self.enrool_proxy.enroll_user(email, nikename, pwd, repwd, check_code)
        time.sleep(2)
        assert self.enrool_proxy.get_name_err() == expected

    @pytest.mark.parametrize("email,nikename,pwd,repwd,check_code,expected",
                             case_data["pwd_err_example"])
    def test_pwd_err_example(self, email, nikename, pwd, repwd, check_code, expected):
        logger.info(f"{email, nikename, pwd, repwd, check_code, expected}")
        self.home_proxy.to_enroll()
        self.enrool_proxy.enroll_user(email, nikename, pwd, repwd, check_code)
        time.sleep(2)
        assert self.enrool_proxy.get_password_err() == expected

    @pytest.mark.parametrize("email,nikename,pwd,repwd,check_code,expected",
                             case_data["repwd_err_example"])
    def test_repwd_err_example(self, email, nikename, pwd, repwd, check_code, expected):
        logger.info(f"{email, nikename, pwd, repwd, check_code, expected}")
        self.home_proxy.to_enroll()
        self.enrool_proxy.enroll_user(email, nikename, pwd, repwd, check_code)
        time.sleep(2)
        assert self.enrool_proxy.get_repassword_err() == expected

    @pytest.mark.parametrize("email,nikename,pwd,repwd,check_code,expected",
                             case_data["check_code_err_example"])
    def test_check_code_err_example(self, email, nikename, pwd, repwd, check_code, expected):
        logger.info(f"{email, nikename, pwd, repwd, check_code, expected}")
        self.home_proxy.to_enroll()
        self.enrool_proxy.enroll_user(email, nikename, pwd, repwd, check_code)
        self.enrool_proxy.enroll_handle.enroll_page.find_email_input().click()
        time.sleep(2)
        assert self.enrool_proxy.get_number_err() == expected

if __name__ == '__main__':
    # TestEnroll().test_case01_enroll(*case_data["p_example"][0])
    print(case_data['p_example'][0][0])
    d_mysql.Delete(table_name="`dang`.`d_user`",
                   condition=f"email=+'{case_data['p_example'][0][0]}'")