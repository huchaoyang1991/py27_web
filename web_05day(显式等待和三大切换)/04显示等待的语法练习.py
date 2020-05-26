"""
============================
Author:柠檬班-木森
Time:2020/4/29   11:57
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 1、创建一个driver对象，访问qq登录页面,设置隐式等待时间
driver = webdriver.Chrome()
driver.get("https://mail.qq.com/")
driver.implicitly_wait(30)

# 2、输入账号密码,点击登录
# 2.0 点击切换到登录的iframe
driver.switch_to.frame('login_frame')
# 2.1 点击账号密码登录

WebDriverWait(driver, 5, 0.2).until(
    EC.element_to_be_clickable((By.ID, 'switcher_plogin'))
)
driver.find_element_by_id('switcher_plogin').click()
# 2.2定位账号输入框，输入账号

WebDriverWait(driver, 5, 0.5).until(
    EC.visibility_of_element_located((By.ID, 'u'))
)
driver.find_element_by_id("u").send_keys("123292678@qq.com")

# 2.3定位密码输入输入密码
driver.find_element_by_id("p").send_keys("PYTHON01")
# 2.4、点击登录
driver.find_element_by_id('login_button').click()

# 3、切换到滑动验证码的iframe,点击滑动按钮
# 3.1切换到滑动验证码的iframe中
tcaptcha = driver.find_element_by_id("tcaptcha_iframe")
driver.switch_to.frame(tcaptcha)
# 3.2选择拖动滑块的节点
driver.find_element_by_id('tcaptcha_drag_thumb').click()

# 为了看效果 等5秒之后再退出
time.sleep(5)
driver.quit()
