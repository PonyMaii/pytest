# 定义web的基类
from selenium.webdriver.support.wait import WebDriverWait

from tools.utils import UtilsDriver, get_yaml

from common.commons import BASE_DIR

# 对象库层基类封装
class BasePage:
    def __init__(self):
        self.driver = UtilsDriver.get_web_driver()  #获取web驱动

        eles = get_yaml(BASE_DIR+"/../datas/element_datas/dangdang")[self.__class__.__name__]

        # Loader=yaml.FullLoader是加载器,更安全,以二进制读取，获取对应的class名
        for ele in eles:  # 根据字典动态赋值
            self.__setattr__(ele, eles[ele])
        self.driver.implicitly_wait(5)

    def get_url(self, url):
        self.driver.get(url)

    def get_element(self, *location):
        wait = WebDriverWait(self.driver, 10, 1)
        element = wait.until(lambda x: x.find_element(*location))
        return element

    def check_element(self, *location):
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

    def click(self, element):
        element.click()

    def get_text(self, element):
        return element.text