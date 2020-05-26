"""
============================
Author:柠檬班-木森
Time:2020/5/9   20:35
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

input_ele = driver.find_element_by_id('kw')

#  js代码
js = "document.getElementById('kw').value = '柠檬班'"
# 执行js代码
driver.execute_script(js)


time.sleep(10)
driver.quit()
