

class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = "./test_dir/"

    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    driver_type = "chrome"

    # 配置运行的 URL
    # url = "https://www.baidu.com"
    url = "http://47.115.125.217:8000/pxf/#/login"

    # 失败重跑次数
    rerun = "0"

    # 当达到最大失败数，停止执行
    max_fail = "0"

    # 浏览器驱动（不需要修改）
    driver = None

    # 报告路径（不需要修改）
    NEW_REPORT = None
