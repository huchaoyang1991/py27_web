"""
============================
Author:柠檬班-木森
Time:2020/5/16   10:17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
pytest中的前置后置
- 用例级别    前后置条件

- 用例类级别    前后置条件

- 用例模块(文件)级别    前后置条件

- 会话级别(程序)    前后置条件

"""

import pytest


class TestCase01:
    @pytest.mark.parametrize('case', [11, 22])
    def test_demo_01(self, case, case_fixture, class_fixture):
        print("测试用例————01执行")
        assert True

    def test_demo_02(self, case_fixture):
        print("测试用例————02执行")
        assert True

    def test_demo_03(self, case_fixture):
        print("测试用例————02执行")
        assert True


@pytest.mark.usefixtures("class_fixture", "case_fixture")
class TestCase02:
    @pytest.mark.parametrize('case', [11, 22])
    def test_demo_01(self, case):
        print("测试用例————01执行")
        assert True

    def test_demo_02(self):
        print("测试用例————02执行")
        assert True

    def test_demo_03(self):
        print("测试用例————03执行")
        assert True


class TestCase03:
    @pytest.mark.parametrize('case', [11, 22])
    def test_demo_01(self, case):
        print("测试用例————01执行")
        assert True

    def test_demo_02(self, case02_fixture):
        print("测试用例————02执行")
        assert True

    def test_demo_03(self, case03_fixture):
        print("测试用例————03执行")
        assert True

# -----------------------------unittest中的前置后置-----------------------------------
# import unittest

# class TestClass(unittest.TestCase):
#     def test_01(self):
#         print('--------用例执行----------')
#         assert True
#
#     def setUp(self):
#         print("--用例的前置条件--")
#
#     def tearDown(self):
#         print("--用例执行的后置条件--")
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         print("用例类执行之前会执行")
#         pass
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print("用例类执行之后会执行")
#         pass
