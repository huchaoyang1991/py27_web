"""
============================
Author:柠檬班-木森
Time:2020/5/7   20:49
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
move_to_element:将鼠标移动到某个元素上

"""

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(5)

# 定位设置元素
set_ele = driver.find_element_by_xpath("//div[@id='u1']//a[text()='设置']")
# # 第一步：创建一个鼠标操作的对象
# action = ActionChains(driver)
# # 第二步：进行移动
# action.move_to_element(set_ele)
# # 第三步：执行动作
# action.perform()

# 三行代码写成一行：支持链式调用
ActionChains(driver).move_to_element(set_ele).perform()

# 等待高级设置可点击
WebDriverWait(driver,5,0.2).until(
    EC.element_to_be_clickable((By.XPATH,"//a[text()='高级搜索']"))
).click()

time.sleep(20)
driver.quit()



