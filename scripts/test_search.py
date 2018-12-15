# 实例化类page
import sys
import os

sys.path.append(os.getcwd())

import pytest

from base.read_yaml import ReadYaml
# from base.get_driver import get_driver
# from page.page_search import PageSearch

def get_data():
    datas = ReadYaml("data_login.yaml").read_yaml()
    print(datas)
    arrs = []
    for datat in datas.values():
        arrs.append((datat.get("username"),datat.get("password")))
        return arrs

class TestSearch():
        def setup_class(self):
            pass

        def teardown_class(self):
            pass

        @pytest.mark.parametrize("username,password", get_data())
        def test_yaml(self, username, password):
            print("正在登陆的用户名:", username)
            print("正在登陆的密码:", password)
        def test_int(self):
            print("执行完毕")
        def test_int(self):
            print("test执行完毕")

    # def setup_class(self):
    #     self.login = PageSearch(get_driver())
    #
    # def teardown_class(self):
    #     self.login.driver.quit()
    # @pytest.mark.parametrize("username,password",[("13526548754","123456")])
    # def test_search(self,username,password):
    #     self.login.page_input_username(username)
    #     self.login.page_input_password(password)
    #     self.login.page_click()

