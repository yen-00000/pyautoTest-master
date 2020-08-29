
import sys
import json
from time import sleep

import allure
import pytest
from os.path import dirname, abspath

import yaml

from page.test_home import HomePage
from page.test_login import LoginPage

class TestSelCourse:
       @allure.story("登录")
       @allure.title("登录--10001")
       @pytest.mark.parametrize(
           "username, password",[("18850107246", "aaa123...")]
       )
       def test_login_success(self,username,password, browser, base_url):
           page = LoginPage(browser)
           page.get(base_url)
           page.username_input = username
           page.password_input = password
           page.login_button.click()
           sleep(5)
           normal_welcome = "欢迎您，"+username
           assert page.welcome_text.text == normal_welcome

       @allure.story("考核")
       @allure.title("考核--10002")
       def test_selcourse_success(self,browser):
           homepage = HomePage(browser)
           homepage.course_button.click()
           homepage.examine_button.click()
           homepage.check_button.click()
           sleep(2)
           homepage.submit_button.click()
           sleep(2)
           print(homepage.pass_text)
           assert "A" in homepage.pass_text.text
