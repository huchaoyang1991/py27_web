"""
============================
Author:柠檬班-木森
Time:2020/5/21   20:46
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import time

from selenium.webdriver.remote.webdriver import WebDriver
from locator.invest_locator import InvestLocator as loc


class InvestPage:
    """投资页面"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_user_amount(self):
        """获取用户投资前的余额"""
        return self.driver.find_element(*loc.invest_amount_ele).get_attribute('data-amount')

    def input_invest_money(self, money):
        """输入投资金额"""
        self.driver.find_element(*loc.invest_amount_ele).send_keys(money)

    def click_invest(self):
        """点击投资"""
        self.driver.find_element(*loc.invest_btn_ele).click()

    def get_invest_info(self):
        """获取投资成功提示信息"""
        time.sleep(1)
        return self.driver.find_element(*loc.invest_success).text

    def click_invest_success(self):
        """点击投资成功更多信息"""
        time.sleep(1)
        self.driver.find_element(*loc.click_success_info).click()

    def get_btn_error_info(self):
        """获取按钮上的提示信息"""
        return self.driver.find_element(*loc.invest_btn_ele).text

    def get_window_error_info(self):
        """获取弹框的错误信息"""
        time.sleep(1)
        return self.driver.find_element(*loc.invest_error_info).text

    def page_refresh(self):
        """刷新页面"""
        self.driver.refresh()
