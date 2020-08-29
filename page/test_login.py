from poium import NewPageElement, Page


class LoginPage(Page):
    username_input = NewPageElement(xpath="/html/body/div[1]/div/div[1]/form/div[1]/div/div[1]/input", describe="用户名")
    password_input = NewPageElement(xpath="/html/body/div[1]/div/div[1]/form/div[2]/div/div[1]/input", describe="密码")
    login_button = NewPageElement(xpath="/html/body/div[1]/div/div[1]/button", describe="登录按钮")
    welcome_text = NewPageElement(xpath="/html/body/div[1]/section/section/header/div/div[3]/span/p", describe="欢迎文案",timeout=5)

