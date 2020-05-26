"""
============================
Author:柠檬班-木森
Time:2020/4/30   21:21
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

input_ele = driver.find_element(By.ID, 'kw')

btn_ele = driver.find_element(By.ID, 'su')

# 页面元素的属性
# tag_name:标签名
# print(input_ele.tag_name)
# print(btn_ele.tag_name)
# text:文本内容
# new = driver.find_element(By.XPATH,'//a[text()="新闻"]')
# parent:获取父级标签
# print(input_ele.parent)


# 页面标签的方法：
# get_attribute(属性名):获取标签的属性
# v = btn_ele.get_attribute("value")
# print(v)

# is_displayed():判断元素是否处于可见状态
# print(btn_ele.is_displayed())

# send_keys():输入内容
# input_ele.send_keys('柠檬班')

# click()点击
# btn_ele.click()

# 清空表单
input_ele.clear()


import time
time.sleep(10)

driver.quit()
