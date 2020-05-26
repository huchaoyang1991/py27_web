"""
============================
Author:柠檬班-木森
Time:2020/5/9   20:35
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
上传文件的两种情况：
一种是js上传的：


一种是input框：


pip install pywinauto -i https://mirrors.aliyun.com/pypi/simple/

pip install pyautogui -i https://mirrors.aliyun.com/pypi/simple/

"""

import time
from selenium import webdriver

driver = webdriver.Chrome()
# 访问图片上传的网页地址
driver.get("https://www.layui.com/demo/upload.html")

#  -----input上传-----------
# driver.find_element_by_xpath('//div[button[@id="test1"]]/input').send_keys('C:\课件\images\9.png')

#  -------js上传文件处理方法--------------------
# 1、pywinauto
# 缺点：只能在windows上使用
# 优点：可以选择多个文件，路径中有中文也能可以

# 2、pyauogui
# 优点： 跨平台(linux,mac,windows都可以用)
# 缺点：只能选择一个文件，文件路径有中文会出问题

# ------------pywinauto  通过窗口上传单个文件----------------------
# from pywinauto.keyboard import send_keys
# 定位文件上传按钮：
# driver.find_element_by_id('test1').click()
#
# time.sleep(2)
# # 输入文件名
# send_keys('C:\课件\images\9.png')
# # 输入回车键
# send_keys('{VK_RETURN}')


# ------------pywinauto 通过窗口上传多个文件----------------------
# from pywinauto.keyboard import send_keys
# 定位文件上传按钮：
# driver.find_element_by_id('test2').click()
#
# time.sleep(2)
# # 输入文件名
# send_keys('"C:\课件\images\9.png"')
# send_keys('"C:\课件\images\8.png"')
# send_keys('"C:\课件\images\9.png"')
# # 输入回车键
# send_keys('{VK_RETURN}')
#

#---------------pyauogui上传文件------------------------
import pyautogui
driver.find_element_by_id('test1').click()
time.sleep(2)
pyautogui.write('C:\project\py27_class\py27_web\google.png')
pyautogui.press('enter', 2)


time.sleep(10)
driver.quit()