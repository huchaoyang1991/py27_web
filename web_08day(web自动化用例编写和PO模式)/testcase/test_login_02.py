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
from web_08day.page.page_login import LoginPage
from web_08day.page.page_index import IndexPage

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
        self.login_page = LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)

    def test_login_pass(self):
        """正常登录的用例"""
        # 进行登录的操作
        self.login_page.login('18684720553', 'python')
        # 获取登录之后的用户信息
        res = self.index_page.get_my_user_info()
        # 断言用例执行是否通过
        self.assertEqual('登录成功', res)

    @data(*error_case_data)
    def test_login_error_case(self, case):
        # 执行登录操作
        self.login_page.login(case['mobile'], case['pwd'])
        # 获取实际提示结果
        result = self.login_page.get_error_info()
        # 断言
        self.assertEqual(case['expected'], result)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
