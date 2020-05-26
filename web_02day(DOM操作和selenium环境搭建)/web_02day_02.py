"""
============================
Author:柠檬班-木森
Time:2020/4/23   21:20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import time
from selenium import webdriver

# 创建一个driver对象，启动一个浏览器
driver = webdriver.Chrome()

# 访问页面
driver.get("https://www.baidu.com")


# 窗口最大化
# driver.maximize_window()

# 窗口最小化
# driver.minimize_window()


# 设置窗口的大小
# driver.set_window_size(width=800,height=500)

# 设置窗口的位置
# driver.set_window_rect(x=100, y=200, width=800, height=500)

time.sleep(2)
driver.get("https://www.taobao.com")


# 返回上一个页面
time.sleep(2)
driver.back()


# 下一个页面
time.sleep(2)
driver.forward()


# 刷新页面
time.sleep(2)
driver.refresh()










# # 关闭窗口
# driver.close()

# 程序执行到这里，等待20秒
time.sleep(10)

# 关闭窗口，退出驱动程序
driver.quit()
