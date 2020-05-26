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

driver.get('https://www.xfz.cn')

date_ele = driver.find_element_by_xpath('//div[@class="more-news"]')

# 滑动窗口到元素可见位置,返回当前元素在页面的坐标位置
res = date_ele.location_once_scrolled_into_view
print(res)




time.sleep(10)
driver.quit()



