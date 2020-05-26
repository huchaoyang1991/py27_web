"""
============================
Author:柠檬班-木森
Time:2020/5/9   16:36
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


def work1():
    driver = webdriver.Chrome()
    driver.get('https://www.layui.com/demo/slider.html')
    sli_ele = driver.find_element_by_xpath("//div[@id='slideTest2']//div[@class='layui-slider-wrap-btn']")
    action = ActionChains(driver)
    action.click_and_hold(sli_ele)
    action.move_by_offset(200, 0)
    action.release()
    action.perform()
    time.sleep(10)
    driver.close()


# work1()


def work2():
    driver = webdriver.Chrome()
    driver.get('https://www.layui.com/demo/form.html')
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//form[@class='layui-form']//input[@placeholder='请选择省']").click()
    driver.find_element_by_xpath("//dd[text()='浙江省']").click()
    driver.find_element_by_xpath("//form[@class='layui-form']//input[@placeholder='请选择市']").click()
    driver.find_element_by_xpath("//dd[text()='杭州']").click()
    driver.find_element_by_xpath("//form[@class='layui-form']//input[@placeholder='请选择县/区']").click()
    driver.find_element_by_xpath("//dd[text()='西湖区']").click()
    time.sleep(10)
    driver.quit()

work2()