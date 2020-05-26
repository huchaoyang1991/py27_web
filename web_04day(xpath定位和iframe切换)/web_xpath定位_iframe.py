"""
============================
Author:柠檬班-木森
Time:2020/4/28   21:33
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

from selenium import webdriver
import time

"""
定位的时候发现标签元素在iframe中怎么办？

切换到对应的iframe标签中才可以进行定位

切换方法：driver.switch_to.frame
driver.switch_to.frame（名称）
driver.switch_to.frame（索引）
driver.switch_to.frame(elements节点)



"""




driver = webdriver.Chrome()



driver.get('https://mail.qq.com/')

# time.sleep(2)

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



# time.sleep(5)

# driver.quit()