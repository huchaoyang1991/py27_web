"""
============================
Author:柠檬班-木森
Time:2020/5/12   21:58
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from locator.index_locator import IndexLocator as loc
from selenium.webdriver.remote.webdriver import WebDriver


class IndexPage:
    """首页"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_my_user_info(self):
        """获取我的账户信息"""
        try:
            self.driver.find_element(*loc.user_info)
        except:
            return '登录失败'
        else:
            return '登录成功'

    def click_quit(self):
        """点击退出登录"""
        self.driver.find_element(*loc.quit_btn).click()

    def click_bid(self):
        """点击抢投标"""
        self.driver.find_element(*loc.bid_btn_ele).click()
