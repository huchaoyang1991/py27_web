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

# 1、创建一个driver对象，访问qq登录页面,设置隐式等待时间
driver = webdriver.Chrome()
driver.get("https://mail.qq.com/")
driver.implicitly_wait(30)

# 2、输入账号密码,点击登录
# 2.0 点击切换到登录的iframe
driver.switch_to.frame('login_frame')
# 2.1 点击账号密码登录
driver.find_element_by_id('switcher_plogin').click()
# 2.2定位账号输入框，输入账号
driver.find_element_by_id("u").send_keys("123292678@qq.com")
# 2.3定位密码输入输入密码
driver.find_element_by_id("p").send_keys("PYTHON01")
# 2.4、点击登录
driver.find_element_by_id('login_button').click()

# 3、切换到滑动验证码的iframe,点击滑动按钮
# 3.1切换到滑动验证码的iframe中
tcaptcha = driver.find_element_by_id("tcaptcha_iframe")
driver.switch_to.frame(tcaptcha)
# 3.2选择拖动滑块的节点
sli_ele = driver.find_element_by_id('tcaptcha_drag_thumb')


# ------------鼠标滑动操作------------
action = ActionChains(driver)
# 第一步：在滑块处按住鼠标左键
action.click_and_hold(sli_ele)
# 第二步：相对鼠标当前位置进行移动
action.move_by_offset(100,0)
# 第三步：释放鼠标
action.release()
# 执行动作
action.perform()


# 为了看效果 等5秒之后再退出
time.sleep(10)
driver.quit()

