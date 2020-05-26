"""
============================
Author:柠檬班-木森
Time:2020/4/25   11:18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from selenium import webdriver
import time

# 启动浏览器
driver = webdriver.Chrome()

# 访问百度
driver.get(url="http://www.baidu.com")
time.sleep(2)


# 定位当搜索输入框
driver.find_element_by_xpath("//input[@id='kw']").send_keys('柠檬班')


# 点击搜索
driver.find_element_by_xpath("//input[@value='百度一下']").click()



















time.sleep(5)
driver.quit()
