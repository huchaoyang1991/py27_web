"""
============================
Author:柠檬班-木森
Time:2020/5/12   21:58
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


class IndexPage:
    """首页"""

    def __init__(self, driver):
        self.driver = driver

    def get_my_user_info(self):
        """获取我的账户信息"""
        try:
            self.driver.find_element_by_xpath("//a[contains(text(),'我的帐户')]")
        except:
            return '登录失败'
        else:
            return '登录成功'
