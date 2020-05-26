import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(3)
driver.maximize_window()
driver.get(url="https://voice.baidu.com/act/newpneumonia/newpneumonia/")

try:
    ele = driver.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div/a")
    print(ele.text)
    ele = driver.find_element_by_xpath("//*[@id='main']/div/div/header/div[1]/span/span")
    print(ele.text)
    ele = driver.find_element_by_xpath("//*[@id='ptab-0']/div[1]/div[3]/div[1]/div[2]")
    print(ele.text)
    # 此元素页面已经取消了，故无法定位到了
    # ele = driver.find_element_by_class_name("VirusSummarySix_1-1-255_szVrQM")
    # print(ele.text)
    ele = driver.find_element_by_class_name("Virus_1-1-255_1KG-A3")
    print(ele.text)
except:
    print("异常退出")
    driver.quit()
else:
    driver.quit()
