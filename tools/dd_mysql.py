#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/19 21:43 
# @Author : XiaoMa
# @Version：V 0.1
# @File : dd_mysql.py
# @desc :


from tools.utils import MySql

d_mysql = MySql(db="dang",
               user="root",
               passwd="123456",
               host="192.168.31.253")

# d_mysql.Delete(table_name="`dang`.`d_user`", condition=" `email`='1915856663@qq.com'")