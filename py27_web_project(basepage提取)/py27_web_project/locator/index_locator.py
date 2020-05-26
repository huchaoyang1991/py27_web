"""
============================
Author:柠檬班-木森
Time:2020/5/19   20:26
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

from selenium.webdriver.common.by import By


class IndexLocator:
    """首页的元素定位"""
    # 用户信息
    user_info = (By.XPATH, "//a[contains(text(),'我的帐户')]")
    # 退出登录
    quit_btn = (By.XPATH, "//a[text()='退出']")
    # 项目抢投标的节点
    bid_btn_ele = (By.XPATH,"(//a[text()='抢投标'])[1]")

