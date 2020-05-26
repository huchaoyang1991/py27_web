"""
============================
Author:柠檬班-木森
Time:2020/5/21   21:26
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from selenium.webdriver.common.by import By


class UserLocator:
    """用户页面的元素定位"""
    # 用户余额
    user_amount_ele = (By.XPATH, '//li[@class="color_sub"]')
