"""
============================
Author:柠檬班-木森
Time:2020/4/28   15:34
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

from selenium import webdriver

# 打开一个driver对象
driver = webdriver.Chrome()

# 访问百度页面
driver.get("https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1")

#  百度首页
driver.find_element_by_xpath("//a[text()='百度首页']")

# 切换地区
driver.find_element_by_xpath('//span[@class="Virus_1-1-255_G4gAvs"]')

# 现有确诊
driver.find_element_by_xpath('//div[@class="VirusSummarySix_1-1-255_3wCKWi VirusSummarySix_1-1-255_123ZxM"]')

# >
driver.find_element_by_xpath('//div[@class="VirusSummarySix_1-1-255_szVrQM"]')

# 累计确诊
driver.find_element_by_xpath('//label[@class="Virus_1-1-255_1KG-A3"]')

driver.quit()
