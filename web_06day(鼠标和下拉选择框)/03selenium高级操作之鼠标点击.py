"""
============================
Author:柠檬班-木森
Time:2020/5/7   20:49
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
click:鼠标左击

double_click：鼠标双击

context_click：鼠标右击

"""

import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(5)

driver.find_element_by_id('kw').send_keys('柠檬班')

btn = driver.find_element_by_id('su')
# 第一步：创建一个鼠标操作的对象
action = ActionChains(driver)
# 第二步：进行点击动作（事实上不会进行操作，只是添加一个点击的动作）
action.click(btn)
# action.context_click(btn)

# 第三步：执行动作
action.perform()



time.sleep(10)
driver.quit()



