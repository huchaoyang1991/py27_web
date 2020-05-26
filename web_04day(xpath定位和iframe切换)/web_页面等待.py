"""
============================
Author:柠檬班-木森
Time:2020/4/28   22:00
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""

页面等待三种方式：
方式一：强制等待：time.sleep()

方式二：隐式等待：

方式：显示等待：


"""
from selenium import webdriver
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
# 隐式等待：设置查找元素的时候，最大的等待时间
driver.implicitly_wait(30)


# 显示等待：WebDriverWait
# wait = WebDriverWait(driver,30,0.2)
# wait.until()




driver.get('https://mail.qq.com/')



driver.switch_to.frame('login_frame')
driver.find_element_by_xpath("//a[text()='帐号密码登录']").click()
