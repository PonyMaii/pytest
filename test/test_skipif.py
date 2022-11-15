#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/14 22:43 
# @Author : XiaoMa
# @Version：V 0.1
# @File : test_skipif.py
# @desc :


import pytest

pytestmark = pytest.mark.skip(reason="跳过所有模块")  #变量必须时 pytestmark 不可更改，跳过当前py文件（模块）

skipif = pytest.mark.skipif(condition=2 > 1, reason="跳过")

class Test_A:

    def test_a(self):
        print("a=============>")

    def test_b(self):
        print("b===============>")