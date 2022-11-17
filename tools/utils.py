#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/10/26 19:21 
# @Author : XiaoMa
# @Version：V 0.1
# @File : unti.py
# @desc :


# 定义工具类
import json
import time
import yaml
import re
from selenium import webdriver
from appium import webdriver as app_driver
from selenium.webdriver.chrome.options import Options
import uiautomator2 as u2

class UtilsDriver:
    _web_driver = None  # 表示的是浏览器webdriver驱动
    _app_driver = None  # 表示的是app的驱动
    _app_device = None  # uiautomator2对象

    # 定义修改私有属性的方法
    @classmethod
    def set_quit_driver(cls, mark):
        cls._web_driver, cls._app_driver, cls._app_device = mark

    # 定义获取浏览器驱动
    @classmethod
    def get_web_driver(cls):
        if cls._web_driver is None:
            # chrom_path = '"C:\Program Files\Google\Chrome\Application\\chrome.exe"'
            # cmd_str = chrom_path + ' --remote-debugging-port=9333 --user-data-dir="C:\selenium\ChromeProfile"'
            # run_cmd(cmd_str)
            # chrome_options = Options()
            # chrome_options.add_experimental_option("debuggerAddress",
            #                                        "127.0.0.1:9333")

            chrome_options = Options()
            chrome_options.add_argument("lang=zh_CN.UTF-8")
            chrome_options.add_argument('--headless')
            prefs = {}
            # 设置这两个参数就可以避免密码提示框的弹出
            prefs["credentials_enable_service"] = False
            prefs["profile.password_manager_enabled"] = False
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
            cls._web_driver = webdriver.Chrome(options=chrome_options)
            cls._web_driver.maximize_window()


        return cls._web_driver

    # 定义退出浏览器驱动
    @classmethod
    def quit_web_driver(cls):
        if cls._web_driver is not None:
            cls.get_web_driver().quit()
            cls._web_driver = None


    # 定义获取app的驱动
    @classmethod
    def get_app_driver(cls):
        if cls._app_driver is None:
            des_cap = {
                  'platformName': 'Android', # 被测手机是安卓
                  'platformVersion': '9', # 手机安卓版本
                  'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
                  'appPackage': 'com.tencent.mm', # 启动APP Package名称
                  # 'appActivity': '.ui.splash.SplashActivity', # 启动Activity名称
                  'appActivity': '.ui.LauncherUI',  # 启动Activity界面名称
                  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True采用unicode编码输入
                  'resetKeyboard': True, # 执行完程序恢复原来输入法
                  'noReset': True,       # 不要重置App
                  'newCommandTimeout': 6000,
                  'automationName' : 'UiAutomator2'
                  # 'app': r'd:\apk\bili.apk',
                }
            cls._app_driver = app_driver.Remote("http://127.0.0.1:4723/wd/hub", des_cap)
        return cls._app_driver

    # 定义退出app驱动的方法
    @classmethod
    def quit_app_driver(cls):
        if cls._app_driver is not None:
            cls.get_app_driver().quit()
            cls._app_driver = None

    #定义uiautomator2获取app驱动的方法
    @classmethod
    def get_ui2_device(cls):
        if cls._app_device is None:
            devices_name = "包名"
            cls._app_device = u2.connect(devices_name)
        return cls._app_device

    #定义uiautomator2退出app驱动的方法
    @classmethod
    def quit_ui2_device(cls, clear_cache=False):
        if cls._app_device is not None:
            package_name = "包名"
            cls.get_ui2_device().app_stop(package_name)
            if clear_cache:
                cls.get_ui2_device().app_clear(package_name)
            cls._app_device = None






# 定义app中边滑动边查找的方法
def app_swipe_find(driver, element, target_ele):
    """
    :param driver: 表示的是app的驱动
    :param element: 表示的滑动的元素对象
    :param target_ele: 表示的是要查找的元素的定位的值
    :return:
    """
    location = element.location  # 获取元素的坐标点位置
    x = location["x"]  # 获取坐标点X的值
    y = location["y"]  # 获取坐标点y的值
    size = element.size
    width = size["width"]
    height = size["height"]
    start_x = x + width*0.9
    end_y = y + height * 0.5
    end_x = x + width * 0.1
    while True:
        page_source = driver.page_source
        try:
            time.sleep(1)
            driver.find_element(*target_ele).click()
            return True
        except Exception as e:
            driver.swipe(start_x, end_y, end_x, end_y, duration=1500)
        if page_source == driver.page_source:
            print("已滑屏到最后的页面，没有找到对应频道！")
            return False




def run_cmd(cmd_str='',  echo_print=1):
    """
    执行cmd命令，不显示执行过程中弹出的黑框
    备注：subprocess.run()函数会将本来打印到cmd上的内容打印到python执行界面上，所以避免了出现cmd弹出框的问题
    :param cmd_str: 执行的cmd命令
    :return:
    """
    from subprocess import Popen
    if echo_print == 1:
        print('\n执行cmd指令="{}"'.format(cmd_str))

    print(Popen(cmd_str, shell=True))



def get_vx(data):
    """
    :param data:
    :return: list->data里的VX号
    """

    list_data = re.findall(r"[wvxnWVXN微信薇合作商务/本人联系质询\s\n]?[:：][\s]*([a-zA-Z]["
                           r"-\da-zA-Z_]{6,"
                           r"19})[\s（(]",
                           data)

    for i in range(len(list_data)):
        list_data[i] = re.search(r"[a-zA-Z0-9][-\da-zA-Z_]{6,"
                                  r"19}", list_data[i]).group(0)
    return list_data



def get_yaml(path):
    with open(path, 'r', encoding='UTF-8') as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
    return data



# 封装获取测试数据的方法
def get_case_data(filename):
    testcase = get_yaml(filename)
    for key in testcase:
        for i in range(len(testcase[key])):
            testcase[key][i] = tuple(testcase[key][i].values())
    return testcase

