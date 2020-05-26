"""
============================
Author:柠檬班-木森
Time:2020/5/9   20:35
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
window.scrollTo:滑动到相对于坐标原点的位置

window.scrollBy:相对于当前位置进行滑动

document.body.scrollHeight:获取当前窗口的可滑动的最大高度

"""


import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.xfz.cn')

date_ele = driver.find_element_by_xpath('//div[@class="more-news"]')

js = """
window.scrollBy(0,500);
"""

js1 = """
window.scrollBy(0,document.body.scrollHeight);
"""


time.sleep(10)
driver.quit()



