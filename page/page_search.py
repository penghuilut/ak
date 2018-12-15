# 创建一个类 继承base
import page
from base.base import Base


class PageSearch(Base):
    # 用户名
    def page_input_username(self,username):
        self.base_input(page.page_username,username)
    # 登录名

    def page_input_password(self,password):
        self.base_input(page.page_wd,password)
    # 登录按钮

    def page_click(self):
        self.base_click(page.page_click)

