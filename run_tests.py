# coding=utf-8
import os
import time
import logging
import pytest
import click
from conftest import REPORT_DIR
from config import RunConfig
import shutil

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python run_tests.py  (回归模式，生成HTML报告)
  > python run_tests.py -m debug  (调试模式)
'''


def init_env(new_report):
    """
    初始化测试报告目录
    """
    # os.mkdir(new_report)
    # os.mkdir(new_report + "/image")



@click.command()
@click.option('-m', default=None, help='输入运行模式：run 或 debug.')
def run(m):
    if m is None or m == "run":
        logger.info("回归模式，开始执行✈✈！")
        # now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        NEW_REPORT=REPORT_DIR+"Allure_report"
        if os.path.exists(NEW_REPORT):
            shutil.rmtree(NEW_REPORT)
        else:
            pass
        RunConfig.NEW_REPORT = os.path.join(REPORT_DIR, "Allure_report")
        init_env(RunConfig.NEW_REPORT)
        pytest.main(["-s", "-v", RunConfig.cases_path,
                     "--alluredir",RunConfig.NEW_REPORT+'/json',
                     "--maxfail", RunConfig.max_fail,
                     "--reruns", RunConfig.rerun])
        os.system('allure generate '+RunConfig.NEW_REPORT+'/json'+' -o ' + RunConfig.NEW_REPORT+'/html'+ ' --clean')
        logger.info("运行结束，生成测试报告♥❤！")
    elif m == "debug":
        print("debug模式，开始执行！")
        pytest.main(["-v", "-s", RunConfig.cases_path])
        print("运行结束！！")


if __name__ == '__main__':
    run()
