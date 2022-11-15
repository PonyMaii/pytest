# 定义web的基类
from selenium.webdriver.support.wait import WebDriverWait
from tools.utils import UtilsDriver
import yaml



# 对象库层基类封装
class BasePage:
    def __init__(self):
        self.driver = UtilsDriver.get_web_driver()  # 获取web驱动
        eles = yaml.load(open('', 'rb'), Loader=yaml.FullLoader)[self.__class__.__name__]
        # Loader=yaml.FullLoader是加载器,更安全,以二进制读取，获取对应的class名
        for ele in eles:  # 根据字典动态赋值
            self.__setattr__(ele, eles[ele])

    # 点击操作
    def click(self, *locator):
        self.driver.find_element(*locator).click()

    # 当元素存在就点击
    def click_ele_exist(self, *locator):
        self.driver.find_element(*locator)
        btns = self.driver.find_elements(*locator)
    # 如果出现用户协议弹出按钮
        if btns:
            btns[0].click()

    # 输入元素定位
    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    # 根据css定位的元素
    def by_js(self, css):
        self.driver.execute_script(f"document.querySelector('{css}')")

    # 切换目标窗口
    def switch_window(self, target_title):
        # 切换到产品详情页窗口
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            # 判断切换到窗口句柄——-判断当前窗口的标题是否是：<header>中的<title>
            if target_title == self.driver.title:
                print("切换窗口句柄到产品详情页")
                return True

    # 获取目标元素文本
    def get_text(self, *locator):
        return self.driver.find_element(*locator).text


    def get_url(self, url):
        self.driver.get(url)

    # 后退

    def back(self):
        self.driver.back()

    # 前进
    def forword(self):
        self.driver.forword()

    # 退出
    def quit(self):
        self.driver.quit()

    #显现等待定位
    def get_element(self, location):
        wait = WebDriverWait(self.driver, 10, 1)
        element = wait.until(lambda x: x.find_element(*location))
        return element

    def check_element(self, location):
        elements = self.driver.find_elements(*location)
        if elements:
            return True
        else:
            return False

# 操作层基类封装
class BaseHandle:
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)