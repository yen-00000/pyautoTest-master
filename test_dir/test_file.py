#
# import sys
# import json
# from time import sleep
#
# import allure
# import pytest
# from os.path import dirname, abspath
#
# import yaml
#
# from page.test_login import LoginPage
# from run_tests import logger
#
# base_path = dirname(dirname(abspath(__file__)))
# sys.path.insert(0, base_path)
#
#
# class TestLogin:
#     user_data=yaml.load(open(base_path + "/test_dir/data/user_data.yaml"))
#     @pytest.mark.parametrize(
#           "username, password",user_data
#      )
#     @allure.story("登录")
#     def test_peixun_login(self,username,password, browser, base_url):
#         page = LoginPage(browser)
#         page.get(base_url)
#         page.username_input = username
#         page.password_input = password
#         page.login_button.click()
#         sleep(5)
#         normal_welcome = "欢迎您，"+username
#         assert page.welcome_text.text == normal_welcome
#
#
#
#
