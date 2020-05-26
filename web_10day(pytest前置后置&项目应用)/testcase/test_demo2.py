"""
============================
Author:柠檬班-木森
Time:2020/5/16   9:35
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""

pytest编写用例，不要使用ddt,不兼容
ddt数据驱动的使用:


pytest中使用pytest.mark.parametrize来实现数据驱动，给用例传参



注意点：用例编写
要么按照unittest的规则来写，数据驱动，前置后置都用unittest中的
要么按照pytest的规则来写，数据驱动，前置后置都用pytest中的

"""
import ddt
import unittest
import pytest


# --------------------unittest中的数据驱动实现--------------------------
# @ddt.ddt
# class TestClass(unittest.TestCase):
#
#     def setUp(self):
#         print("--用例的前置条件--")
#
#     @ddt.data(11, 22, 333, 444, 55)
#     def test_01(self, case):
#         assert case < 100
#
#     def tearDown(self):
#         print("--用例执行的后置条件--")

# ------------------错误示范：不要混用---------------------------
# @ddt.ddt
# class TestLogin:
#     @ddt.data(11,22,33)
#     def test_02(self, case):
#         assert case < 100

# ---------------pytets中数据驱动的实现--------------------------------

@pytest.mark.parametrize('case',[11,22,33,44,155])
def test_03(case):
    assert case < 100

#
# error_case_data = [
#     {'mobile': "", "pwd": "python1", "expected": "请输入手机号"},
#     {'mobile': "1868472055a", "pwd": "python1", "expected": "请输入正确的手机号"},
#     {'mobile': "18684720553", "pwd": "", "expected": "请输入密码"}
# ]
#
#
# # 读取excel数据
# @pytest.mark.parametrize('musen', error_case_data)
# def test_dome_04(musen):
#     print(musen)
#     print('--------------用例执行-------------')
#     assert True


# -----------------------pytest.mark.parametrize:不兼容unittest中的前置后置------------------------------

# -------------错误示范：不要混用-------------------
# class TestClass(unittest.TestCase):
#
#     def setUp(self):
#         print("--用例的前置条件--")
#
#     @pytest.mark.parametrize('case',[11, 22, 333, 444, 55])
#     def test_01(self, case):
#         print('--------用例执行----------')
#         assert case < 100
#
#     def tearDown(self):
#         print("--用例执行的后置条件--")
