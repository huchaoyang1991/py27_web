"""
============================
Author:柠檬班-木森
Time:2020/5/12   21:44
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


class LoginPage:
    """登录页面"""

    def __init__(self, driver):
        self.driver = driver
        # 打开登录页面
        self.driver.get('http://120.78.128.25:8765/Index/login.html')
        self.driver.implicitly_wait(15)

    def login(self, user, pwd):
        """输入账号密码点击登录"""
        self.driver.find_element_by_xpath('//input[@placeholder="手机号"]').send_keys(user)
        # 输入密码
        self.driver.find_element_by_xpath('//input[@placeholder="密码"]').send_keys(pwd)
        # 点击登录
        self.driver.find_element_by_xpath("//button[text()='登录']").click()

    def get_error_info(self):
        """获取登录失败的提示信息"""
        return self.driver.find_element_by_xpath("//div[@class='form-error-info']").text

    def get_alert_error_info(self):
        """获取页面弹窗的错误提示信息"""
        return self.driver.find_element_by_xpath('//div[@class="layui-layer-content"]').text
