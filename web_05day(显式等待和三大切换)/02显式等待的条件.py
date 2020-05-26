"""
============================
Author:柠檬班-木森
Time:2020/4/30   20:15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = Chrome()
driver.get('https://www.baidu.com')


# 工作中显式等待的写法：
WebDriverWait(driver, 30, 0.5).until(
    EC.visibility_of_element_located((By.XPATH, "//a[text()='新闻']")))


# 关于显式等待的等待条件
# element_to_be_clickable：等待元素处于可点击的状态
# visibility_of_element_located：等待元素处于可见状态
# presence_of_element_located：等待元素被加载（html中能找到这个元素）



# 隐式等待：等待的条件是元素能够被找到（html中能找到这个元素）

