"""
============================
Author:柠檬班-木森
Time:2020/4/25   10:07
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
元素定位的方法：



"""

from selenium import webdriver
import time

# 启动浏览器
driver = webdriver.Chrome()
# 访问百度
driver.get(url="http://www.baidu.com")
time.sleep(2)

# 1、通过id去查找
res_ele = driver.find_element_by_id('kw')
# res_ele.send_keys("柠檬班")


# 2、通过name属性来查找
# driver.find_element_by_name('wd').send_keys("python27期666")

# 3、通过标签名去找
# 返回第一个
# ele = driver.find_element_by_tag_name('input')
# 返回所有的
# ele = driver.find_elements_by_tag_name('input')
# print(ele)

# 4、通过class类属性去找
# ele = driver.find_element_by_class_name('s_ipt_wr')
# print(ele)

# 5、通过链接标签的文本进行查找
# driver.find_element_by_link_text("新闻").click()

# 6、通过链接标签的部分文本去匹配
# driver.find_element_by_partial_link_text('抗击').click()

# 7、通过xpath来进行定位
# driver.find_element_by_xpath("//input[@id='kw']").send_keys('musen')

# 8、通过css选择器来定位
# driver.find_element_by_css_selector('#kw').send_keys("9989989")
#









time.sleep(5)
driver.quit()


