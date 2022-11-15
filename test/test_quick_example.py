#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/14 18:32 
# @Author : XiaoMa
# @Version：V 0.1
# @File : test_quick_example.py
# @desc :

# import pytest

# @pytest.fixture
# def first_var():
#     return ["a"]
#
#
# @pytest.mark.runs
# def test_str(first_var):
#     first_var.append("b")
#
#     assert first_var == ["a", "b"]
#
#     print(first_var)
#

# import pytest
# # 环境准备
# @pytest.fixture()
# def first_entry():
#     return "a"
#
# @pytest.fixture()
# def order(first_entry):
#     return [first_entry]
#
# @pytest.mark.runs
# def test_string(order):
#     order.append("b")
#     assert order == ["a", "b"]
#     print(order)


# import pytest
#
# @pytest.fixture()
# def fix1():
#     print("fix1==========>")
#
# @pytest.fixture()
# def fix2():
#     print("fix2==============>")
#
#
# @pytest.mark.usefixtures("fix1", "fix2")
# def test_fix01():
#     print("用例1=====")
#
#
# @pytest.mark.usefixtures("fix2")
# class Test_Case:
#
#     def test_fix02(self):
#         print("用例2=========")
#
#     def test_fix03(self):
#         print("用例3=========")

import pytest

def read_list():
    return ["1", "2", "3"]

@pytest.fixture(params=read_list())
def get_params(request):
    #request时pytest内置的fixture， 主要用于传递参数
    return request.param

def test_001(get_params):
    print("测试用例："+get_params)















