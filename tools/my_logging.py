#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/23 15:45 
# @Author : XiaoMa
# @Version：V 0.1
# @File : my_logging.py
# @desc :

import logging
import logging.config
from config import BASE_DIR

# 封装
def getLogger(confName="applog"):
    with open(BASE_DIR+"/common/logging.conf", "r", encoding="utf-8") as f:
        logging.config.fileConfig(fname=f)
    return logging.getLogger(confName)


if __name__ == '__main__':
    logger = getLogger()
    logger.info("123456")