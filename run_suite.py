"""
    目标：
        1.搜索组装测试套件
        2.运行测试套件并生成测试报告
"""
# 导包 unittest HTMLTestRunner time
import unittest
import time
from tools.HTMLTestRunnerNew import HTMLTestRunner

# 组装测试套件
suite = unittest.defaultTestLoader.discover("./case",pattern="test*.py")

# 指定报告存放路径，及文件名称
file_path = "./report/{}.html".format(time.strftime("%Y_%m_%d_%H_%M_%S"))

# 运行测试套件并生成报告
with open(file_path, "wb") as f:
    HTMLTestRunner(stream=f,verbosity=2,title='测试报告名称', description='这里是描述', tester='测试者').run(suite)