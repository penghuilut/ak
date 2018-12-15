from selenium.webdriver.support.wait import WebDriverWait


class Base():
    # 封装查找元素
    def __init__(self,driver):
        self.driver = driver

    def base_find_element(self, loc, timeout=20, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))
     # 封装输入元素

    def base_input(self,loc,value):
        # 先找到定位,在封装
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)


        # 封装点击元素

    def base_click(self,loc):
        self.base_find_element(loc).click()
