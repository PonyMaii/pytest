#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/13 21:27 
# @Author : XiaoMa
# @Version：V 0.1
# @File : test_01.py
# @desc :
import pytest


class Test_testxx:

    @pytest.mark.skip    # 跳过用例的标签
    def test_pr01(self):
        print("test01")

    @pytest.mark.moduName         #run是你要自定义添加的标签
    def test_pr02(self):
        print("test02")

    def test_pr03(self):
        print("test03")