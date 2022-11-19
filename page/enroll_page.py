#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/19 19:15 
# @Author : XiaoMa
# @Version：V 0.1
# @File : enroll_page.py
# @desc :
from base.web.base import BasePage, BaseHandle

class EnrollPage(BasePage):
    def __init__(self):
        super().__init__()

    def find_email_input(self):
        return self.get_element(*self.email_input)

    def find_nikename_input(self):
        return self.get_element(*self.nikename_input)

    def find_pwd_input(self):
        return self.get_element(*self.pwd_input)

    def find_repwd_input(self):
        return self.get_element(*self.repwd_input)

    def find_check_code_input(self):
        return self.get_element(*self.check_code_input)

    def find_enroll_btn(self):
        return self.get_element(*self.enroll_btn)

    def find_write_in_info(self):
        #断言验证邮箱
        return self.get_element(*self.write_in_info)

    def find_login_bj_info(self):
        #断言注册成功
        return self.get_element(*self.login_bj_info)

    def find_email_err_info(self):
        return self.get_element(*self.email_err_info)

    def find_name_err_info(self):
        return self.get_element(*self.name_err_info)

    def find_password_err_info(self):
        return self.get_element(*self.password_err_info)

    def find_repassword_err_info(self):
        return self.get_element(*self.repassword_err_info)

    def find_number_err_info(self):
        return self.get_element(*self.number_err_info)

    def find_ent_code_btn(self):
        return self.get_element(*self.ent_code_btn)


class EnrollHandle(BaseHandle):
    def __init__(self):
        self.enroll_page = EnrollPage()

    def set_email_input(self, email):
        self.input_text(self.enroll_page.find_email_input(), email)

    def set_nikename_input(self, nikename):
        self.input_text(self.enroll_page.find_nikename_input(), nikename)

    def set_pwd_input(self, pwd):
        self.input_text(self.enroll_page.find_pwd_input(), pwd)

    def set_repwd_input(self, repwd):
        self.input_text(self.enroll_page.find_repwd_input(), repwd)

    def set_check_code_input(self, check_code):
        self.input_text(self.enroll_page.find_check_code_input(), check_code)

    def click_enroll_btn(self):
        self.enroll_page.find_enroll_btn().click()

    def click_ent_code_btn(self):
        self.click(self.enroll_page.find_ent_code_btn())

    def get_write_in_info(self):
        return self.get_text(self.enroll_page.find_write_in_info())

    def get_login_bj_info(self):
        return self.get_text(self.enroll_page.find_login_bj_info())

    def get_email_err_info(self):
        return self.get_text(self.enroll_page.find_email_err_info())

    def get_name_err_info(self):
        return self.get_text(self.enroll_page.find_name_err_info())

    def get_password_err_info(self):
        return self.get_text(self.enroll_page.find_password_err_info())

    def get_repassword_err_info(self):
        return self.get_text(self.enroll_page.find_repassword_err_info())

    def get_number_err_info(self):
        return self.get_text(self.enroll_page.find_number_err_info())


class EnrollProxy:
    def __init__(self):
        self.enroll_handle =EnrollHandle()

    def enroll_user(self, email, nikename, pwd, repwd, check_code):
        self.enroll_handle.set_email_input(email)
        self.enroll_handle.set_nikename_input(nikename)
        self.enroll_handle.set_pwd_input(pwd)
        self.enroll_handle.set_repwd_input(repwd)
        self.enroll_handle.set_check_code_input(check_code)

    def click_enroll(self):
        #点击完成
        self.enroll_handle.click_enroll_btn()

    def click_ent_code(self):
        self.enroll_handle.click_ent_code_btn()

    def get_write_in(self):
        #点击注册成功后断言信息
        return self.enroll_handle.get_write_in_info()

    def get_login_bj(self):
        #获取验证邮箱后断言信息
        return  self.enroll_handle.get_login_bj_info()

    def get_email_err(self):
        return self.enroll_handle.get_email_err_info()

    def get_name_err(self):
        return self.enroll_handle.get_name_err_info()

    def get_password_err(self):
        return self.enroll_handle.get_password_err_info()

    def get_repassword_err(self):
        return self.enroll_handle.get_repassword_err_info()

    def get_number_err(self):
        return self.enroll_handle.get_number_err_info()

