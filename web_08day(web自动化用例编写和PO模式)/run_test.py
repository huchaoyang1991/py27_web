"""
============================
Author:柠檬班-木森
Time:2020/5/12   21:36
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest

from HTMLTestRunnerNew import HTMLTestRunner

# 加载用例到套件
suite = unittest.defaultTestLoader.discover(r'C:\project\py27_class\py27_web\web_08day\testcase')
# 创建一个运行程序
runner = HTMLTestRunner(stream=open('report.html', 'wb'), title='27期第一份web自动化测试报告')
# 执行测试用例
runner.run(suite)
