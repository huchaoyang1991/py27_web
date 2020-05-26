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

driver.get('https://www.12306.cn/index/')

date_ele = driver.find_element_by_id("train_date")

time.sleep(3)
#  js代码
js = """
var date_ele = arguments[0];
date_ele.readOnly=false;
date_ele.value ='2020-06-09'; 
"""
# 执行js代码
driver.execute_script(js, date_ele)

time.sleep(10)
driver.quit()



