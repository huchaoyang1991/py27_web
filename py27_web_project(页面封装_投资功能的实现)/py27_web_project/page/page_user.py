"""
============================
Author:柠檬班-木森
Time:2020/5/21   21:25
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from selenium.webdriver.remote.webdriver import WebDriver
from locator.user_locator import UserLocator as loc


class UserPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_user_amount(self):
        """获取用户的余额"""
        amount = self.driver.find_element(*loc.user_amount_ele).text
        amount = amount.replace('元', '')
        return amount
