from poium import NewPageElement, Page


class HomePage(Page):
    course_button = NewPageElement(xpath='//*[@id="app"]/section/section/main/div/div[3]/div/div[1]', describe="课程")
    examine_button = NewPageElement(xpath='/html/body/div/section/section/main/div/div/div/div/div[2]/div[2]/button[2]', describe="开始考核")
    check_button = NewPageElement(xpath='/html/body/div/section/section/main/div/div[1]/div[1]/div[2]/div/ul/li/div[2]/div/label[1]', describe="选择答案")
    submit_button = NewPageElement(xpath='/html/body/div/section/section/main/div/div[1]/div[2]/button[1]', describe="提交答案")
    pass_text = NewPageElement(xpath="/html/body/div[1]/section/section/main/div/div[2]/div/div/div[2]/div[1]/ul/li/span[2]/span[1]", describe="通知答案")
