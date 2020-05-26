"""
============================
Author:柠檬班-木森
Time:2020/5/12   21:58
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from common.base_page import BasePage
from locator.index_locator import IndexLocator as loc


class IndexPage(BasePage):
    """首页"""

    def get_my_user_info(self):
        """获取我的账户信息"""
        try:
            self.get_element(loc.user_info, '首页_定位我的账户')
        except:
            return '登录失败'
        else:
            return '登录成功'

    def click_quit(self):
        """点击退出登录"""
        self.click_element(loc.quit_btn, '首页_退出登录')

    def click_bid(self):
        """点击抢投标"""
        self.click_element(loc.bid_btn_ele, '首页_点击抢投标')
