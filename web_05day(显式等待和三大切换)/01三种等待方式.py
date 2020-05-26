"""
============================
Author:柠檬班-木森
Time:2020/4/30   20:15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 强制等待：需要等的时候就要加上对应的代码
# time.sleep(2)

driver = Chrome()
driver.get('https://www.baidu.com')

# 隐式等待：设置隐式等待的时间
# driver.implicitly_wait(30)


# 显式等待：

# 第一步：创建一个等待计时器对象
# wait = WebDriverWait(driver, 30, 0.5)
# 第二步：元素的定位方式以及定位表达式
# located = ("xpath", "//a[text()='新闻']")
# 第三步：设置等待的条件
# conditions = EC.visibility_of_element_located(located)
# 第四步
# wait.until(conditions)

# wait = WebDriverWait(driver, 30, 0.5)
# located = ('id', 'su')
# conditions = EC.visibility_of_element_located(located)
# wait.until(conditions)

# 将选择器的方式，改成BY模块
# wait = WebDriverWait(driver, 30, 0.5)
# located = (By.XPATH, "//a[text()='新闻']")
# conditions = EC.visibility_of_element_located(located)
# wait.until(conditions)


# 工作中显式等待的写法：
WebDriverWait(driver, 30, 0.5).until(
    EC.visibility_of_element_located((By.XPATH, "//a[text()='新闻']")))


