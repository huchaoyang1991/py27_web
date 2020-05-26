"""
============================
Author:柠檬班-木森
Time:2020/5/12   21:44
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from common.base_page import BasePage
from locator.login_locator import LoginLocator as loc
from selenium.webdriver.remote.webdriver import WebDriver
from common.handle_config import conf
import time


class LoginPage(BasePage):
    """登录页面"""
    # 登录的url地址
    url = conf.get('env', 'base_url') + conf.get('url', 'login_url')

    # url = 'http://120.78.128.25:8765/Index/login.html'

    def __init__(self, driver):
        """
        :param driver: webdriver对象
        :type driver: WebDriver
        """
        super().__init__(driver)
        # 打开登录页面
        self.driver.get(self.url)
        self.driver.implicitly_wait(15)

    def login(self, user, pwd):
        """输入账号密码点击登录"""
        self.input_text(loc.mobile_loc, user, '登录_账号输入')
        # 输入密码
        self.input_text(loc.pwd_loc, pwd, '登录_密码输入')
        # 点击登录
        self.click_element(loc.login_loc, '登录_点击元素')

    def get_error_info(self):
        """获取登录失败的提示信息"""
        return self.get_element_text(loc.error_info, '登录_失败提示信息')

    def get_alert_error_info(self):
        """获取页面弹窗的错误提示信息"""
        ele = self.wait_element_visibility(loc.alert_error_info, '登录_页面弹窗错误提示')
        return ele.text

    def page_refresh(self):
        """刷新页面"""
        self.driver.get(url=self.url)

    def click_re_mobile(self):
        """取消记住手机号"""
        self.click_element(loc.re_mobile, '登录_点击取消记住手机号')

# class LoginPage:
#     """登录页面"""
#     # 账号输入框
#     mobile_loc = (By.XPATH, '//input[@placeholder="手机号"]')
#     # 密码输入框
#     pwd_loc = (By.XPATH, '//input[@placeholder="密码"]')
#     # 点击按钮
#     login_loc = (By.XPATH, "//button[text()='登录']")
#     # 失败的提示内容
#     error_info = (By.XPATH, "//div[@class='form-error-info']")
#     # 失败的弹框
#     alert_error_info = (By.XPATH, '//div[@class="layui-layer-content"]')
#     # 登录的url地址
#     url = 'http://120.78.128.25:8765/Index/login.html'
#
#     def __init__(self, driver):
#         self.driver = driver
#         # 打开登录页面
#         self.driver.get(self.url)
#         self.driver.implicitly_wait(15)
#
#     def login(self, user, pwd):
#         """输入账号密码点击登录"""
#         self.driver.find_element(*self.mobile_loc).send_keys(user)
#         # 输入密码
#         self.driver.find_element(*self.pwd_loc).send_keys(pwd)
#         # 点击登录
#         self.driver.find_element(*self.login_loc).click()
#
#     def get_error_info(self):
#         """获取登录失败的提示信息"""
#         return self.driver.find_element(*self.error_info).text
#
#     def get_alert_error_info(self):
#         """获取页面弹窗的错误提示信息"""
#         return self.driver.find_element(*self.alert_error_info).text
