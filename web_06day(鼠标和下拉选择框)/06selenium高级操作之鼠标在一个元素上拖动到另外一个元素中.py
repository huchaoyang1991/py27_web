"""
============================
Author:柠檬班-木森
Time:2020/5/7   20:49
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
click_and_hold: 按下鼠标左键
move_by_offset:相对鼠标当前位置进行移动
release:释放鼠标


"""

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1、创建一个driver对象，访问qq登录页面,设置隐式等待时间
driver = webdriver.Chrome()
driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
driver.implicitly_wait(30)

# 切换iframe
driver.switch_to.frame(driver.find_element_by_id('iframeResult'))


s = WebDriverWait(driver, 30, 0.5).until(
    EC.visibility_of_element_located((By.ID, 'draggable'))
)
t = WebDriverWait(driver, 30, 0.5).until(
    EC.visibility_of_element_located((By.ID, 'droppable'))
)

# ------------鼠标滑动操作------------
action = ActionChains(driver)
# 第一步：拖动元素
action.drag_and_drop(s, t)
# 执行动作
action.perform()

# 为了看效果 等5秒之后再退出
time.sleep(10)
driver.quit()
