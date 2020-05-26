"""
============================
Author:柠檬班-木森
Time:2020/5/9   20:35
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.12306.cn/index/')


# ----------------------------通过js代码修改元素的属性--------------------
# from_ele = driver.find_element_by_id("fromStationText")
# to_ele = driver.find_element_by_id('toStationText')
# time.sleep(3)
#  js代码
# js = """
# var fro_ele = arguments[0];
# var to_ele = arguments[1];
# fro_ele.value = '上海';
# to_ele.value = '太原';
# return '操作完了';
# """
# # 执行js代码
# res = driver.execute_script(js,from_ele,to_ele)
# print('js代码执行之后的返回值：',res)



# -----------------------通过js来定位元素-------------------------------------

# js = """
# var forEle =  document.getElementById('fromStationText');
# return forEle;
# """
# res = driver.execute_script(js)
# time.sleep(3)
# res.send_keys('长沙')
# print(res)


# -----------------------理解arguments---------------------------
# arguments:execute_script方法中传进入的参数，除了js代码，都会保存在arguments中
# js = """
# console.log(arguments)
# """
# driver.execute_script(js,9999,111,222,333,44,555)



time.sleep(10)
driver.quit()
