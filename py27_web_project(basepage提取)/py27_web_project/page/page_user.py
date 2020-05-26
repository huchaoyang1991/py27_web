"""
============================
Author:柠檬班-木森
Time:2020/5/21   21:25
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from selenium.webdriver.remote.webdriver import WebDriver

from common.base_page import BasePage
from locator.user_locator import UserLocator as loc


class UserPage(BasePage):

    def get_user_amount(self):
        """获取用户的余额"""
        amount = self.get_element_text(loc.user_amount_ele,'用户页面_获取余额')
        amount = amount.replace('元', '')
        return amount
