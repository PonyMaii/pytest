#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/14 1:14 
# @Author : XiaoMa
# @Version：V 0.1
# @File : test_02.py
# @desc :
import pytest

"""
@pytest.mark.parametrize(argnames=, argvalues=, indirect=, ids=, scope=)
argnames:参数名
argvalues：参数对应值，类型必须为list
            当参数为一个时格式：[value1, vlaue2....]
            当参数个数大于1个时格式:[(value1_01, value2_01....),(value1_02, value2_02....),...]
indirect:
ids: 对每次用例命名
scope:
"""
#多个参数时
# @pytest.mark.parametrize(
#     "user,pwd,expected",
#     [("xiaoma", "123456", "登入成功"), ("张三", "456789", "登入失败")],
#     ids=["case1","case2"]
# )
# def test_parpmetrize(user, pwd, expected):
#     print(f"用户名：{user}， 密码:{pwd}")
#     assert "登入成功" == expected
#
#
# #只有一个参数时
# @pytest.mark.parametrize(
#     "user",
#     ["test001", "pwd001", "001"]
# )
# def test_001(user):
#     print(f"002用户名:{user}")


