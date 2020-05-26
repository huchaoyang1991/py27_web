"""
============================
Author:柠檬班-木森
Time:2020/5/12   20:40
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import time
import unittest
from selenium import webdriver
from ddt import ddt, data

"""
'18684720553，python'
"""
error_case_data = [
    {'mobile': "", "pwd": "python1", "expected": "请输入手机号"},
    {'mobile': "1868472055a", "pwd": "python1", "expected": "请输入正确的手机号"},
    {'mobile': "18684720553", "pwd": "", "expected": "请输入密码"}
]


@ddt
class TestLogin(unittest.TestCase):
    """测试登录"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        # 打开登录页面
        self.driver.get('http://120.78.128.25:8765/Index/login.html')
        self.driver.implicitly_wait(15)

    def test_login_pass(self):
        """正常登录的用例"""
        # 输入账号
        self.driver.find_element_by_xpath('//input[@placeholder="手机号"]').send_keys('18684720553')
        # 输入密码
        self.driver.find_element_by_xpath('//input[@placeholder="密码"]').send_keys('python')
        # 点击登录
        self.driver.find_element_by_xpath("//button[text()='登录']").click()
        # 断言用例执行是否通过
        # 判断是否进入到了首页，如果进入到了登录之后的页面，那么用例执行通过
        try:
            self.driver.find_element_by_xpath("//a[contains(text(),'我的帐户')]")
        except:
            raise AssertionError('正常登录用例执行未通过')

    @data(*error_case_data)
    def test_login_error_case(self, case):
        # 输入手机号码
        self.driver.find_element_by_xpath('//input[@placeholder="手机号"]').send_keys(case['mobile'])
        # 输入密码
        self.driver.find_element_by_xpath('//input[@placeholder="密码"]').send_keys(case['pwd'])
        # 点击登录
        self.driver.find_element_by_xpath("//button[text()='登录']").click()
        # 断言用例执行是否通过
        # 预期结果
        expected = case['expected']
        result = self.driver.find_element_by_xpath("//div[@class='form-error-info']").text
        # 断言
        self.assertEqual(expected, result)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
