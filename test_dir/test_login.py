#
# import sys
# from time import sleep
#
# import allure
# import pytest
# from os.path import dirname, abspath
#
# from page.test_home import HomePage
# from page.test_login import LoginPage
#
# sys.path.insert(0, dirname(dirname(abspath(__file__))))
#
#
# class TestLogin:
#     """体能管理系统"""
#     @allure.feature("登录")
#     def test_peixun_login_case(self, browser, base_url):
#         """
#         名称：培训系统登录
#         步骤：
#         1、打开浏览器
#         2、输入用户名
#         3、输入密码
#         3、点击登录
#         检查点：
#         * 检查页面标题是否包含关键字。
#         """
#         page = LoginPage(browser)
#         page.get(base_url)
#         page.username_input="18850107246"
#         page.password_input="aaa123..."
#         page.login_button.click()
#         sleep(5)
#         normal_welcome = "欢迎您，"+username
#         assert page.welcome_text.text == normal_welcome
#
#
#
#
# if __name__ == '__main__':
#     pytest.main(["-v", "-s", "test_login.py"])
#

