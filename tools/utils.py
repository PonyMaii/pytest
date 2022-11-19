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



def get_BASE_DIR():
    import sys, os
    if getattr(sys, "frozen", False):
        BASE_DIR = os.path.dirname(sys.executable)
    else:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    return BASE_DIR


class UtilsDriver:
    _web_driver = None  # 表示的是浏览器webdriver驱动
    _app_driver = None  # 表示的是app的驱动


    # 定义修改私有属性的方法
    @classmethod
    def set_quit_driver(cls, mark):
        cls._web_driver, cls._app_driver = mark

    # 定义获取浏览器驱动
    @classmethod
    def get_web_driver(cls, brower="Chrome"):
        if cls._web_driver is None:
            brower = brower.capitalize()
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
            cls._web_driver = getattr(webdriver, brower)(options=chrome_options)
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


class UtilsDevice:
    _app_device = None  # uiautomator2对象

    # 定义修改私有属性的方法
    @classmethod
    def set_quit_driver(cls, mark):
        cls._app_device = mark

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


import pymysql
class MySql:
    """
    pymysql数据库封装
    pymysql.connect()
    管理数据库，给数据库传入参数
    pymysql.connect().cursor()
    打开游标，切记
    python
    上的mysql
    一定要打开游标
    pymysql.connect().close()
    关闭数据库
    pymysql.connect().cursor()
    关闭游标
    """
    def __init__(self, db, user, passwd, host='localhost', port=3306, charset='utf8'):
        """
        数据库配置
        :param db:              数据库名字
        :param user:            链接的用户名
        :param passwd:          链接的密码
        :param host:            IP地址默认是：127.0.0.1  localhost
        :param port:            端口默认：3306 可修改
        :param charset:         默认转码：utf8
        """
        self.__db = db
        self.__user = user
        self.__passwd = passwd
        self.__host = host
        self.__port = port
        self.__charset = charset
        self.__connect = None
        self.__cursor = None



    def connect_db(self):
        """
        dbManager._connect_db()
        连接数据库
        :return:
        """
        params = {
            "db": self.__db,
            "user": self.__user,
            "passwd": self.__passwd,
            "host": self.__host,
            "port": self.__port,
            "charset": self.__charset
        }
        self.__connect = pymysql.connect(**params)
        self.__cursor = self.__connect.cursor()

    def Close_DB(self):
        """
        dbManager._close_db()
        :return:
        """
        self.__cursor.close()
        self.__connect.close()

    def Establish_DB(self, DB_name):
        """
        创建数据库
        :param DB_name: 创建的数据库名字
        :return:
        """
        self.connect_db()
        try:
            self.__cursor.execute("CREATE DATABASE %S" % DB_name)
        except Exception as e:
            print('创建数据库失败，失败原因：', e)
        else:
            print('数据库创建成功')

    def Establish_table(self, surface_name, condition):
        """
        创建表
        :param surface_name: 要创建的表名字
        :param condition: 要创建表的条件
        :return:
        """
        self.connect_db()
        try:
            create_table = "CREATE TABLE {table_name} ({value})".format(table_name=surface_name,value=condition)
            self.__cursor.execute(create_table)
        except Exception as e:
            print("创建表失败：",e)
        else:
            print("创建表成功")

    def Insert_DB(self, table_name, insert_data):
        """
        DBManager.insert(table, insert_data)
        :param table_name: str --> table 为字符串
        :param insert_data: [a:b] --> 为列表中嵌套字典类型
        :return:
        """
        # 用户传入数据自读那列表数据，根据key, value 添加进数据库
        # 连接数据库
        self.connect_db()
        try:
            data = self.Handle_value(insert_data)
            key = data[0]
            value = data[1]
            sql = "INSERT INTO {table_name}({key}) values ({values})".format(table_name=table_name, key=key,
                                                                             values=value)
            self.__cursor.execute(sql)
            self.__connect.commit()

        except Exception as e:
            print('数据插入失败，失败原因：', e)
        else:
            self.Close_DB()
            print('数据插入成功')

    def Delete(self, table_name, condition):
        """
        dbManager.delete(table, condition)
        传入相应的条件 -- > 删除数据库中的数据
        :param table_name: 表名
        :param condition: 传入条件
        :return:
        """
        self.connect_db()
        condition_Text = condition
        if type(condition) is not str:
            condition_Text = ' and '.join(self.Handle_value(condition))

        try:
            # 构建sql语句
            sql = "DELETE FROM {table_name} WHERE {condition}".format(table_name=table_name, condition=condition_Text)
            print(sql)
            self.__cursor.execute(sql)
            self.__connect.commit()
        except Exception as e:
            print('删除失败：', e)
        else:
            self.Close_DB()
            print('删除成功')

    def Update(self, table_name, data, condition=None):
        """
        dbManager.update(table, date,condition)
        :param table_name: 表名
        :param data: dict -> data 字典类型
        :param condition: dict -> condition 字典类型
        :return:
        """
        self.connect_db()
        update_data = ','.join(self.Handle_value(data))
        try:
            if condition is not None:
                # 处理传入的条件
                condition_data = ' and '.join(self.Handle_value(condition))
                sql = "UPDATE {table} SET {values} WHERE {conditions}".format(table=table_name, values=update_data,
                                                                              conditions=condition_data)
            else:
                sql = "UPDATE {table} SET {values}".format(table=table_name, values=update_data)
            self.__cursor.execute(sql)
            self.__connect.commit()
        except Exception as e:
            print('更新失败：', e)
        else:
            self.Close_DB()
            print('更新成功')

    def Select_DB(self, table_name, show_ist, condition=None, get_one=False):
        """
        查数据
        :param table_name: --> str 字符串类型
        :param show_ist: --> 列表类型
        :param condition: --> 字典类型
        :param get_one: --> 布尔类型
        :return:
        """
        self.connect_db()
        # 处理显示的数据
        shou_list = ','.join(show_ist)
        try:
            if condition is not None:
                condition_list = self.Handle_value(condition)
                condition_data = ' and '.join(condition_list)
                sql = "SELECT {key} FROM {table} WHERE {values}".format(key=shou_list, table=table_name,
                                                                        values=condition_data)
            else:
                sql = "SELECT {key} FROM {table}".format(key=shou_list, table=table_name)

            self.__cursor.execute(sql)
            self.__connect.commit()
            if get_one:
                result = self.__cursor.fetchone()
            else:
                result = self.__cursor.fetchall()
            print(result)

        except Exception as e:
            print("查询失败：", e)
        else:
            self.Close_DB()
            print("查询成功")

        # todo 处理传进来的Value

    def Handle_value(self, value):
        """
        处理传进来的value
        self.deal_values(value) --> str or list
        :param value: 传进来的value
        :return:
        """
        result = []
        for k, v in value[0].items():
            if isinstance(k, int):
                if k == 0:
                    content_KEY = []
                    content_VALUE = []
                    for vs in v:
                        for kx, vx in vs.items():
                            value = self.handel_text(value=vx, ks=k)
                            content_KEY.append(str(kx))
                            content_VALUE.append(value)
                    condition_key = ','.join(content_KEY)
                    condition_value = ','.join(content_VALUE)
                    return condition_key, condition_value
                else:
                    for vs in v:
                        for kx, vx in vs.items():
                            res = self.handel_text(key=kx, value=vx, ks=k)
                            result.append(res)

        return result

    def handel_text(self, value, ks, key=None):
        """
        处理进来的条件
        :param key: 传进来的Key
        :param value: 传进来的Value
        :param ks 传进来的K值
        :return:
        """
        condition = self.Judeg_parameter(ks)
        if isinstance(value, str):
            v = ("'{value}'".format(value=value))
        else:
            v = str(value)
        if ks == 0:
            return v
        else:
            return "{key}{condition}{value}".format(key=key, condition=condition, value=v)

    def Judeg_parameter(self, judeg_structure):
        if judeg_structure == 1:
            return "="
        elif judeg_structure == 2:
            return ">"
        elif judeg_structure == 3:
            return "<"
        elif judeg_structure == 4:
            return ">="
        elif judeg_structure == 5:
            return "<="