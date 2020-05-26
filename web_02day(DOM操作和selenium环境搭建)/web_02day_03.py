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

"""
driver对象的属性


"""

# 创建一个driver对象，启动一个浏览器
driver = webdriver.Chrome()

# 访问页面
driver.get("https://www.baidu.com")

# 获取当前页面的url地址
print(driver.current_url)


# 获取当前页面的标题
print(driver.title)


# 获取页面的代码
# print(driver.page_source)

# 获取当前窗口的句柄
# print(driver.current_window_handle)


# 获取所有窗口的句柄
print(driver.window_handles)




# 程序执行到这里，等待20秒
# time.sleep(10)

# 关闭窗口，退出驱动程序
driver.quit()
