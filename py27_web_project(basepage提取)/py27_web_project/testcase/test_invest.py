"""
============================
Author:柠檬班-木森
Time:2020/5/21   20:04
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import time
from decimal import Decimal

import pytest
from selenium.webdriver import Chrome

from common.handle_config import conf
from common.handle_logging import log
from data.case_data import InvestData
from page.page_index import IndexPage
from page.page_invest import InvestPage
from page.page_login import LoginPage
from page.page_user import UserPage

"""
投资功能的实现：
# 分析投资用例执行的过程：涉及到了那些页面的操作？
1、登录页面---->输账号，密码点击登录
2、首页页面  ----> 选中项目，点击抢投标（待封装）   ---ok
3、投资的项目页面：
    - 获取账户可用余额（待封装）    ---ok
    - 输入投资金额（待封装）    -Ok
    - 点击投资（待封装）      --OK    
    
    - 投资成功，获取投标成功的信息（待封装） --ok
    - 投资成功，点击查看并激活（待封装）   --ok
    
    - 投资失败，获取按钮上的提示信息（待封装）  --ok
    - 投资失败，获取弹框的错误信息（待封装）   --ok
    
4、用户页面
    - 获取可用余额（待封装）  --ok
    
    
    
前置条件：
1、打开浏览器，访问登录页面
2、需要登录  （账户要有钱，需要有投资的项目）
3、选定项目，点击抢投标

执行用例
 操作步骤   
 1、输入投资的金额
 2、点击投资（如果输入的不是10的整数倍，点击时没有任何效果的）
 校验结果：
 情况一：输入的金额不是10的整数倍，点击按钮上会出现提示：  校验点按钮上的提示信息是否和预期一致
 情况二：输入的数据不符合要求（0,负数，超出最大可投金额，空格），弹框提示对应的错误： 校验弹框的提示信息是否和预期一致
 情况三：投资成功，成功的弹框提示： 
 校验：1、是否弹出投资成功，
      2、校验投资之前和投资之后的余额变化的值是否和投资金额一致
           - 投资之前要去获取账户余额  （可以在输入框标签种获取）
           - 投资之后再去获取账户余额  （点击成功信息查看按钮，会进入用户页面，获取投资之后的余额）
           - 相减，再断言
 
后置条件
关闭浏览器

"""


# Alt+ Enter
@pytest.fixture(scope='class')
def invest_fixture():
    # 前置条件
    driver = Chrome()
    driver.implicitly_wait(15)
    # 创建登录页面
    login_page = LoginPage(driver)
    # 登录
    login_page.login(user=conf.get('test_data', 'mobile'), pwd=conf.get('test_data', 'pwd'))
    # 创建首页对象
    index_page = IndexPage(driver)
    # 点击抢标
    index_page.click_bid()
    # 创建投资页面
    invest_page = InvestPage(driver)
    # 创建用户页面
    user_page = UserPage(driver)
    yield invest_page, user_page
    # 后置条件
    driver.quit()


class TestInvest:
    @pytest.mark.parametrize('case', InvestData.error_data)
    def test_invest_error(self, case, invest_fixture):
        """投资失败，按钮上出现提示的用例"""
        invest_page = invest_fixture[0]
        # 输入投资金额
        invest_page.input_invest_money(case['money'])
        # 获取按钮的提示信息
        res = invest_page.get_btn_error_info()
        try:
            assert case['expected'] == res
        except AssertionError as e:
            log.error("用例--{}---执行未通过".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}---执行通过".format(case['title']))

    @pytest.mark.parametrize('case', InvestData.error_popup_data)
    def test_invest_error_window(self, case, invest_fixture):
        """投资失败，弹框上出现提示信息的用例"""
        # 用例：投资金额为0
        invest_page = invest_fixture[0]
        # 输入投资金额
        invest_page.input_invest_money(case['money'])
        # 点击投资
        invest_page.click_invest()
        # 获取页面弹框的提示
        res = invest_page.get_window_error_info()
        # 手动关闭弹框
        invest_page.click_close_error_popup()
        try:
            assert case['expected'] == res
        except AssertionError as e:
            log.error("用例--{}---执行未通过".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}---执行通过".format(case['title']))

    @pytest.mark.parametrize('case', InvestData.success_data)
    def test_invest_success(self, case, invest_fixture):
        """投资成功的用例"""
        # 用例：投资金额为200
        invest_page, user_page = invest_fixture
        # 获取用户的余额（投资前）
        start_amount = invest_page.get_user_amount()
        # 输入投资金额
        invest_page.input_invest_money(case['money'])
        # 点击投资
        invest_page.click_invest()
        # 获取页面弹框的提示成功的信息
        res = invest_page.get_invest_info()
        # 点击查看投资成功的信息，跳转到用户页面
        invest_page.click_invest_success()
        # 获取用户页面的用户余额(投资后)
        end_amount = user_page.get_user_amount()
        try:
            assert case["expected"] == res
            assert Decimal(start_amount) - Decimal(end_amount) == Decimal(case['money'])
        except AssertionError as e:
            log.error("用例--{}---执行未通过".format('投资金额为0'))
            log.exception(e)
            time.sleep(10)
            raise e
        else:
            log.info("用例--{}---执行通过".format('投资金额为0'))
