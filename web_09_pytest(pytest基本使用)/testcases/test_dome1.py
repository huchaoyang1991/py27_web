"""
============================
Author:柠檬班-木森
Time:2020/5/14   21:11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
# 方式一：直接类上面打标记
@pytest.mark.webtest

# 方式二：通过类属性pytestmark
class TestClass(object):
    pytestmark = [pytest.mark.webtest, pytest.mark.slowtest]


"""

import pytest


# @pytest.mark.musen
# @pytest.mark.class_
class TestDome1:
    pytestmark = [pytest.mark.class_, pytest.mark.musen]

    def test_demo1_01(self):
        assert 1 == 100

    def test_demo1_02(self):
        assert 100 == 100
