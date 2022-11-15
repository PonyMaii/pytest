#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/13 20:38
# @Author : XiaoMa
# @Version：V 0.1
# @File : test_pytest.py
# @desc :

"""
pytest 的规则：
好处：1、pytest会在内存中回收所有用例生成的内容
    2、提高了运行效率
1、命名规则：
    1）文件名需要以test开头 或者 test结尾
    2）类名需要以Test开头
    3）函数名需要以test开头
    这个规则式为了让pytest能找到对应的用例，因为pytest是使用寻找用例的一种机制

"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Test:
    @pytest.mark.skip
    def test(self):
        driver = webdriver.Chrome()

        driver.implicitly_wait(10)

        driver.get('https://www.baidu.com')

        driver.find_element(By.ID, 'kw').send_keys('长风')

        driver.find_element(By.ID,'su').click()

        time.sleep(2)

        assert driver.title == '长风_百度搜索'

    @pytest.mark.baidu
    def test_baidu01(self):
        print("baidu001")

    @pytest.mark.baidu
    def test_baidu02(self):
        print("baidu002")

    @classmethod
    def setup_class(cls):
        print("所有用例开始时环境初始化")

    @classmethod
    def teardown_class(cls):
        print("所有用例结束时执行环境重置")

    def setup_method(self):
        print("setup_method==================>")

    def teardown_method(self):
        print("teardown_method===============>")

    def setup(self):
        print("环境初始化")

    def teardown(self):
        print("环境重置")

def setup_module():
    print(" setup_module============================")

def teardown_module():
    print("teardown_module============================")

#在每个函数之前执行
def setup_function():
    print("setup_function============================")

#在每个函数之后执行
def teardown_function():
    print("teardown_function============================")

@pytest.mark.baidu
def test_prcase1():
    print("teatcase1")

"""
#在所有用例之前执行
    def setup_module(self):
        print(" setup_module============================")
#在所有用例之后执行
    def teardown_module(self):
        print("teardown_module============================")
#在每个函数之前执行
    def setup_function(self):
        print("setup_function============================")
#在每个函数之后执行
    def teardown_function(self):
        print("teardown_function============================")
        
"""


