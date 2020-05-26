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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(5)

driver.find_element(By.ID, 'kw').send_keys('柠檬班')
driver.find_element(By.ID, 'su').click()

# 在点击打开新窗口之前获取一下，所有的窗口句柄
start_window = driver.window_handles
try:
    # 点击搜索出来的柠檬班：点击之后会打开一个新窗口
    driver.find_element(By.XPATH,"//div[@id=1]/h3/a").click()
    # 等待新窗口打开
    WebDriverWait(driver,5,0.5).until(
        EC.new_window_is_opened(start_window)
    )
    # 切换窗口
    driver.switch_to.window(driver.window_handles[-1])
    # 定位新窗口上的元素
    driver.find_element_by_id("js_keyword").send_keys('柠檬班')

except Exception  as e:
    pass
finally:
    time.sleep(10)
    driver.quit()
