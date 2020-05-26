"""
============================
Author:柠檬班-木森
Time:2020/4/23   21:20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

from selenium import webdriver

# 配置了环境变量，不用传参数
driver = webdriver.Chrome()

# 没有给chromedriver配置环境变量，要通过参数去指定chromedriver所在的路径
# driver = webdriver.Chrome(executable_path=r"C:\project\py27_class\chromedriver.exe")








