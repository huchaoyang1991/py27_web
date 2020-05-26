"""
============================
Author:柠檬班-木森
Time:2020/4/30   21:58
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(30)

driver.find_element(By.ID, 'kw').send_keys('柠檬班')

driver.find_element(By.ID, 'su').click()


w = driver.current_window_handle

driver.find_element(By.XPATH,"//div[@id=1]/h3/a").click()
ws = driver.window_handles
print(w)
print(ws)
print(driver.current_window_handle)

# 切换窗口的方法（窗口名）
driver.switch_to.window(ws[-1])




time.sleep(10)

driver.quit()
