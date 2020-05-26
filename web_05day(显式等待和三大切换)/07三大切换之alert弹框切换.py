"""
============================
Author:柠檬班-木森
Time:2020/4/30   21:37
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
iframe切换：


alert换：


窗口切换：


"""
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(r"C:\project\py27_class\py27_web\web_01day\web_html_form.html")


# 关于alert弹框的切换
alert = driver.switch_to.alert
# 点击确认
# alert.accept()
# 点击取消
# alert.dismiss()
# alert.send_keys("python34567890")
# alert.accept()

import time

time.sleep(10)

driver.quit()