#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/13 21:04 
# @Author : XiaoMa
# @Version：V 0.1
# @File : main.py
# @desc :

"""
pyest在企业中是怎么运行用例的?
pytest.main([]) #pytest运行用例的方式 可以在任意py文件下使用；它会检索所有同级及其一下的用例
"""

import pytest
from tools.auto_email import AutoEmail
from config import BASE_DIR

"""
    Python测试发现约定
    *如果未指定任何参数，则收集从testpaths
    (如果已配置）或当前目录开始。另外，命令行参数可以在目录，
    文件名或节点ID的任何组合中使用。
    ★递归到目录，除非它们匹配norecursedirs（排除哪些目录）.
    *在这些目录中，搜索test_*.py或*_test.py-*从这些文件中，收集测试项目:
    *在类之外拥有test前缀的测试函数或方法
    *在拥有Test前缀中的测试类（不含__init__方法)中的拥有test前缀的测试函数或方法
    可自定义测试发现规则
    pytest也可以发现使用标准的unittest.TestCase子类技术的测试用例(完全兼容unittest的原因)
"""


if __name__ == '__main__':
    pytest.main(["--html=./report/report.html",
                 "--self-contained-html",
                 "--junit-xml=./report/report.xml",
                 "--durations=10", "-vv",
                 "--alluredir", "./report/temp_allure",
                 "--clean-alluredir",
                 ])

    """
    -s: 输出用例中所有需要打印的内容
    """
    import os
    os.system("allure generate ./report/temp_allure -o ./report/report_allure/ --clean")
    # generate 后面指的是执行收集的用例目录
    # -o 标识生成的报告放在哪个目录
    ae = AutoEmail() #创建邮箱类的对象
    report = (BASE_DIR+"/report/report.html").replace("\\", "/")
    ae.send_email(report, "小马")