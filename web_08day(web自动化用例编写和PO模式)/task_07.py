"""
============================
Author:柠檬班-木森
Time:2020/5/12   18:00
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get('https://www.12306.cn/index/')
# 点击往返
time.sleep(1)
WebDriverWait(driver, 10, 0.5).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="search-tab-hd"]//a[text()="往返"]'))).click()

# 输入起始地
start_addr = driver.find_element(By.ID, "fromStationFanText")
start_addr.click()
start_addr.send_keys('长沙')
driver.find_element(By.ID, "citem_0").click()
# 输入终止地
driver.find_element(By.ID, "toStationFanText").send_keys('上海')
driver.find_element(By.ID, "citem_0").click()

# 定位起始时间和终止时间输入框
start_date = driver.find_element_by_id('go_date')
end_date = driver.find_element_by_id('from_date')
js = """
var s_ele = arguments[0];
var e_ele = arguments[1];
s_ele.readonly = false;
s_ele.value ='2020-05-15';
e_ele.readonly=false;
e_ele.value ='2020-07-15';
"""

# 输入起始时间和终止时间
res = driver.execute_script(js, start_date, end_date)

# 下滑到网页底部
time.sleep(3)
driver.find_element_by_id('index_ads').location_once_scrolled_into_view

time.sleep(10)
driver.quit()
