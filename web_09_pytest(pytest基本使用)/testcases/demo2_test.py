"""
============================
Author:柠檬班-木森
Time:2020/5/14   21:12
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
在用例方法上使用@pytest.mark.skip，可以跳过该用例的执行

@pytest.mark.xfail:标记 预期不会通过的用例

自定义标记：
1、注册标记：在启动文件同级别目录下创建一个 pytest.ini的配置文件
2、在pytest.init 添加一个 pytest的配置块
3、在pytest的配置块下面加一个markers的配置项
4、在markers的配置项中去注册标记

5、给对应的用例打标记：@pytest.mark.注册的标记名称



"""

import pytest


# @pytest.mark.xfail(reason='已知的不通过用例')
def test_demo2_01():
    assert 99 == 999


@pytest.mark.skip
def test_demo2_02():
    assert 99 == 99


@pytest.mark.musen
def test_demo2_03():
    assert 9 == 9


@pytest.mark.musen
def test_demo2_04():
    assert 999 == 999


@pytest.mark.yuze
@pytest.mark.musen
def test_demo2_05():
    assert 999 == 999


def test_demo2_06():
    assert 999 == 999


@pytest.mark.yuze
def test_demo2_07():
    assert 999 == 999


@pytest.mark.yuze
def test_demo2_08():
    assert 999 == 999
