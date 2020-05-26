"""
============================
Author:柠檬班-木森
Time:2020/5/16   11:07
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from selenium import webdriver
import unittest
import pytest

# class TestLogin(unittest.TestCase):
#     """测试登录"""
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#
#     def test_login_pass(self):
#         """正常登录的用例"""
#         # 进行登录的操作
#         self.driver.get('http://www.bai.com')
#
#     def tearDown(self):
#         self.driver.quit()


# ----------------------------------pytest------------------------------------
"""
如果前置条件中要给用例传递数据怎么办

注意点：如果要在前置中传递数据，那么不能使用pytest.mark.userfixtures 这种方法给用例添加前置后置：

"""


@pytest.fixture()
def case_fixture():
    # 前置
    driver = webdriver.Chrome()
    expected = 200
    yield driver, expected
    # 后置
    driver.quit()


# @pytest.mark.usefixtures("case_fixture") 这个使用方法，只限于不需要将前置条件中的数据传给用例的情况下
class TestLogin02:
    """测试登录"""
    def test_login_pass(self, case_fixture):
        """正常登录的用例"""
        driver, expected = case_fixture
        driver.get("http://www.baidu.com")

# (<selenium.webdriver.chrome.webdriver.WebDriver (session="c164c3c0513750c15ff60d2f9de6432e")>, 200)
