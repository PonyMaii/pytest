#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/15 23:20 
# @Author : XiaoMa
# @Version：V 0.1
# @File : commons.py
# @desc :

# ​​com​mons.py文件​​
# 获取项目路径、项目的各环境的url，处理数据文件的方法，框架执行相关日志功能的实现方法

import os, configparser


# os: 获取操作系统级别的目录/文件夹的操作和文件的操作（读取，写入）
# configparser: 在python中的主要功能是读取配置文件config.ini

# 获取config.ini路径
def congfig_path():
    # return os.path.split(os.path.realpath(__file__))[0].split('C')[0]
    # 获取当前文件的路径
    curPath = os.path.dirname(os.path.realpath(__file__))
    # 返回config.ini路径
    return os.path.join(curPath, "config.ini")


# 返回config.ini中的testUrl
def config_url(key, value):
    # 创建配置文件管理对象
    config = configparser.ConfigParser()
    # 读取config.ini文件
    config.read(congfig_path(), encoding="utf-8")
    return config.get(key, value)
HOST = config_url('Url', 'url')

# 获取正确的路径
import sys, os
if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    print("项目路径是：" + congfig_path())
    print("项目的url是： " + config_url('Url', 'url'))