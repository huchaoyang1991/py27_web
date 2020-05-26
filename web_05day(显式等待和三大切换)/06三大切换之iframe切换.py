"""
============================
Author:柠檬班-木森
Time:2020/4/30   21:37
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
iframe切换：


alert换：


窗口切换：


"""
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://mail.qq.com/")
driver.implicitly_wait(30)

# 方式一：切换iframe：通过iframe的名字（name属性）进行切换
# driver.switch_to.frame('login_frame')
# driver.find_element_by_xpath("//a[text()='帐号密码登录']").click()

# 方式二：通过索引去切换iframe标签
# time.sleep(2)
# driver.switch_to.frame(0)

# driver.find_element_by_xpath('//div[@id="wxLoginTab"]').click()
# driver.find_element_by_xpath('//p[@id="auto_login"]/a').click()


# 方式三：通过element节点去进行切换
# ele_iframe = driver.find_element_by_xpath('//iframe[@id="login_frame"]')
# driver.switch_to.frame(ele_iframe)
# driver.find_element_by_xpath("//a[text()='帐号密码登录']").click()


# 方式四：使用显示等待的方式，等待iframe处于可以的状态，然后切换进行
WebDriverWait(driver, 20, 1).until(
    EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@id="login_frame"]'))
)
driver.find_element_by_xpath("//a[text()='帐号密码登录']").click()

#  关于iframe切换回 默认的HTML页面
driver.switch_to.default_content()

# 切换回父级的iframe中
driver.switch_to.parent_frame()


time.sleep(10)

driver.quit()
