#
# import sys
# import json
# from time import sleep
# import pytest
# from os.path import dirname, abspath
#
# import yaml
#
# from page.test_login import LoginPage
#
# base_path = dirname(dirname(abspath(__file__)))
# sys.path.insert(0, base_path)
#
# @pytest.mark.parametrize(
#     "username, password",
#     [("18850107246", "aaa123..."),
#      ("", "aaa123..."),
#      ("18850107246", " "),
#      ],
#     ids=["case1", "case2", "case3"]
# )
# def test_peixun_login(username,password, browser, base_url):
#     page = LoginPage(browser)
#     page.get(base_url)
#     page.username_input = username
#     page.password_input = password
#     page.login_button.click()
#     sleep(5)
#     normal_welcome = "欢迎您，"+username
#     assert page.welcome_text.text == normal_welcome
