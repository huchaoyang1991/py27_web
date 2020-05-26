"""
============================
Author:柠檬班-木森
Time:2020/5/9   20:11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
# 键盘的操作

# Keys.BACK_SPACE：回退键（BackSpace）
# Keys.TAB：制表键（Tab）
# Keys.ENTER：回车键（Enter）
# Keys.SHIFT：大小写转换键（Shift）
# Keys.CONTROL：Control键（Ctrl）
# Keys.ALT：ALT键（Alt）
# Keys.ESCAPE：返回键（Esc）
# Keys.SPACE：空格键（Space）
# Keys.PAGE_UP：翻页键上（Page Up）
# Keys.PAGE_DOWN：翻页键下（Page Down）
# Keys.END：行尾键（End）
# Keys.HOME：行首键（Home）
# Keys.LEFT：方向键左（Left）
# Keys.UP：方向键上（Up）
# Keys.RIGHT：方向键右（Right）
# Keys.DOWN：方向键下（Down）
# Keys.INSERT：插入键（Insert）
# DELETE：删除键（Delete）
# NUMPAD0 ~ NUMPAD9：数字键1-9
# F1 ~ F12：F1 - F12键
# (Keys.CONTROL, ‘a’)：组合键Control+a，全选
# (Keys.CONTROL, ‘c’)：组合键Control+c，复制
# (Keys.CONTROL, ‘x’)：组合键Control+x，剪切
# (Keys.CONTROL, ‘v’)：组合键Control+v，粘贴

"""



import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

input_ele = driver.find_element_by_id('kw')
# 输入柠檬班
input_ele.send_keys('柠檬班')

# 输入回车键
input_ele.send_keys(Keys.ENTER)

# 按F12
# input_ele.send_keys(Keys.F12)

# 全选
# input_ele.send_keys(Keys.CONTROL, 'a')
#
# # 复制
# input_ele.send_keys(Keys.CONTROL, 'c')
#
# # 粘贴
# input_ele.send_keys(Keys.CONTROL, 'v')
# input_ele.send_keys(Keys.CONTROL, 'v')

time.sleep(10)
driver.quit()

