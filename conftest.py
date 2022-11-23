#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/11/20 18:50 
# @Author : XiaoMa
# @Version：V 0.1
# @File : conftest.py
# @desc :
# conftest.py

import pytest
from config import BASE_DIR
import time
import json
from tools.my_logging import getLogger

logger = getLogger()


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     outcome = yield
#     report = outcome.get_result()
#     if item.function.__doc__ is None:
#         report.description = str(item.function.__name__)		# 如果没有三引号注释（'''注释'''），就提取函数名到case的输出文案中，就是上面的test_id
#     else:
#         report.description = str(item.function.__doc__)			# 提取三引号注释（'''注释'''）到case的输出文案中
#     report.nodeid = report.nodeid.encode("unicode_escape").decode("utf-8")  # 再把编码改回来
#

#高阶函数
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    获取运行时得数据
    :param terminalreporter:
    :param exitstatus:
    :param config:
    :return:
    """
    skipped = terminalreporter.stats.get("skipped", [])
    passed = terminalreporter.stats.get("passed", [])
    failed = terminalreporter.stats.get("failed", [])

    date = time.strftime("%Y-%m-%d")
    RESULT_PATH = (BASE_DIR + rf"/result/{date}-result.yaml").replace("\\", r"/")
    print(RESULT_PATH)
    result = {}

    if skipped:
        for i in skipped:
            result.update({
                i.nodeid: {
                    "result": "skipped",
                    "date": date
                }
            })


    if passed:
        for i in passed:
            result.update({
                i.nodeid: {
                    "result": "passed",
                    "date": date
                }
            })

    if failed:
        for i in failed:
            result.update({
                i.nodeid: {
                    "result": "passed",
                    "date": date
                }
            })

    if result:
        with open(RESULT_PATH, "a+") as f:
            f.write(json.dumps(result))



    # print(skipped)
    # print(passed)
    # print(failed)
    #
    #
    # print("执行总数：", len(skipped+passed+failed))
    # print("跳过的用例数：", len(skipped))
    # print("通过的用例数", len(passed))
    # print("失败的用例数", len(failed))
    #
    # """获取失败的用例的名字"""
    # # print("获取失败的用例们", failed)
    # """
    # for i in passed:
    # # print(dir(i)) #用例对象里面的详细引用函数
    #     for j in i.__dict__:
    #         i_data = getattr(i, j)
    #         print(f"i里面的数据{j}： {i_data}")
    #
    # """
    #
    for i in failed:
        # #失败的用例
        # location = i.location[0]+"::"+i.location[-1]
        # #print(i.nodeid)
        # # print("失败location:", location)
        # # print("错误日志：", i.longrepr)
        # _time = time.strftime("%Y-%m-%d %H-%M-%S")
        # log_path = BASE_DIR + rf"\log\{_time}-" + i.nodeid.split("[")[0].replace("::", "-").replace("/", "-").replace(".py", "") + ".log"
        # with open(log_path.replace("\\", r"/"), "w+", encoding="utf-8") as f:
        #     f.write(str(i.longrepr))
        logger.exception(i.longrepr)

# def pytest_itemcollected(item):
#     team = {}
#
#     print(item.own_markers) #用例的标签数据-->列表


