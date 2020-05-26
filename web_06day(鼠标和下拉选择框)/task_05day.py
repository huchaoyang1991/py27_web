"""
============================
Author:柠檬班-木森
Time:2020/5/6   10:03
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



def work1():
    """课堂派登录"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get('https://www.ketangpai.com/User/login.html')
    driver.find_element(By.XPATH, '//input[@placeholder="邮箱/账号/手机号"]').send_keys('11234')
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="密码"]').send_keys('123454321')
    driver.find_element(By.XPATH, '//a[text()="登录"]').click()
    time.sleep(5)
    driver.quit()


def work2():
    """腾讯客服页面操作"""
    driver = webdriver.Chrome()
    driver.get('https://kf.qq.com/product/weixin.html')
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='手机版微信']"))).click()
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='微信群']"))).click()
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='微信群创建及设置方法']"))).click()
    time.sleep(5)
    driver.quit()


def work3():
    """艺龙搜索操作"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get('http://www.elong.com/')

    city = driver.find_element(By.XPATH, "//div[@id='domesticDiv']//dl[dt/text()='目的地']//input")
    city.clear()
    # 输入长沙市
    city.send_keys('长沙市')
    # 等待搜索的元素加载出来，然后再进行选择
    # time.sleep(1)
    WebDriverWait(driver, 30, 0.5).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[@method="cityData"]/li[@data=0]'))).click()
    # 输入区域
    driver.find_element(By.XPATH, '//input[@placeholder="如位置\酒店名\品牌"]').send_keys('麓谷')
    # 点击搜索
    driver.find_element(By.XPATH, '//span[@data-bindid="search"]').click()
    time.sleep(5)
    driver.close()
    driver.quit()


def work4():
    """12306"""

    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get('https://www.12306.cn/index/')
    # 点击往返
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="search-tab-hd"]//a[text()="往返"]'))).click()
    # 输入起始地
    start_addr = driver.find_element(By.ID, "fromStationFanText")
    start_addr.click()
    # start_addr.clear()
    start_addr.send_keys('长沙')
    driver.find_element(By.ID, "citem_0").click()
    # # 输入终止地
    driver.find_element(By.ID, "toStationFanText").send_keys('上海')
    driver.find_element(By.ID, "citem_0").click()
    # # 点击高铁
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable((By.XPATH, '//li[@id="isHigh"]/i'))).click()
    # # # 点击搜索
    driver.find_element(By.XPATH, '//a[@id="search_two"]').click()
    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    # work1()
    # work2()
    # work3()
    work4()
