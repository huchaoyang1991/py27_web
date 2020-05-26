"""
============================
Author:柠檬班-木森
Time:2020/5/23   10:04
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import os
import time

from selenium.webdriver.remote.webdriver import WebDriver

from common.handle_logging import log

"""
1、显式等待（
    元素被加载，
    元素可见，
    元素可点击）
2、获取元素的文本
3、点击元素
4、获取元素的属性

5、文本输入

6、窗口拖动

7、滑动到元素可见

9、执行js代码



# 如果元素定位出错了要不要日志输出？
    日志输出可以封装的basepage的基础操作中
    
# 如果元素定位出错了，页面截图？
    错误截图一起封装


"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.handle_path import ERROR_IMG


class BasePage:
    """把页面一些常见的功能操作全部封装到这里"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_element_visibility(self, locator, img_info, timeout=15, poll_frequency=0.5):
        """
        等待元素可见
        :param locator: 定位表达式
        :param img_info: 错误截图文件名
        :param timeout: 等待超时时间
        :param poll_frequency: 等待轮询时间
        :return:
        """
        # 等待元素之前获取当前的时间
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception as e:
            # 输出日志
            log.error("元素--{}--等待可见超时".format(locator))
            log.exception(e)
            # 对当前页面进行截图
            self.save_scree_image(img_info)
            raise e
        else:
            # 元素等待出现之后，获取实际
            end_time = time.time()
            log.info("元素--{}--等待成功,等待时间{}秒".format(locator, end_time - start_time))
            return ele

    def wait_element_clickable(self, locator, img_info, timeout=15, poll_frequency=0.5):

        """
        等待元素可点击
        :param locator: 定位表达式
        :param img_info: 错误截图文件名
        :param timeout: 等待超时时间
        :param poll_frequency: 等待轮询时间
        :return:
        """
        # 等待元素之前获取当前的时间
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.element_to_be_clickable(locator)
            )
        except Exception as e:
            # 输出日志
            log.error("元素--{}--等待可点击超时".format(locator))
            log.exception(e)
            # 对当前页面进行截图
            self.save_scree_image(img_info)
            raise e
        else:
            # 元素等待出现之后，获取实际
            end_time = time.time()
            log.info("元素--{}--可点击等待成功,等待时间{}秒".format(locator, end_time - start_time))
            return ele

    def wait_element_presence(self, locator, img_info, timeout=15, poll_frequency=0.5):
        """
        等待元素被加载
        :param locator: 定位表达式
        :param img_info: 错误截图文件名
        :param timeout: 等待超时时间
        :param poll_frequency: 等待轮询时间
        :return:
        """
        # 等待元素之前获取当前的时间
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(locator)
            )
        except Exception as e:
            # 输出日志
            log.error("元素--{}--等待被加载超时".format(locator))
            log.exception(e)
            # 对当前页面进行截图
            self.save_scree_image(img_info)
            raise e
        else:
            # 元素等待出现之后，获取实际
            end_time = time.time()
            log.info("元素--{}--加载等待成功,等待时间{}秒".format(locator, end_time - start_time))
            return ele

    def get_element_text(self, locator, img_info):
        """
        获取元素的文本
        :param locator: 元素定位表达式
        :param img_info: 错误截图信息
        :return:
        """
        try:
            text = self.driver.find_element(*locator).text
        except Exception as e:
            # 输出日志
            log.error("元素--{}--获取文本失败".format(locator))
            log.exception(e)
            # 对当前页面进行截图
            self.save_scree_image(img_info)
            raise e
        else:
            log.info("元素--{}--获取文本成功".format(locator))
            return text

    def get_element_attribute(self, locator, attr_name, img_info):
        """
        获取元素的文本"
        :param locator: 元素定位表达式
        :param attr_name: 属性名字
        :param img_info: 错误截图信息
        :return:
        """
        try:
            ele = self.driver.find_element(*locator)
            attr_value = ele.get_attribute(attr_name)
        except Exception as e:
            # 输出日志
            log.error("获取元素--{}--属性失败".format(locator))
            log.exception(e)
            # 对当前页面进行截图
            self.save_scree_image(img_info)
            raise e
        else:
            log.info("获取元素--{}--属性成功".format(locator))
            return attr_value

    def click_element(self, locator, img_info):
        """
        点击元素
        :param locator: 元素定位表达式
        :param img_info: 错误截图信息
        :return:
        """
        try:
            self.driver.find_element(*locator).click()
        except Exception as e:
            # 输出日志
            log.error("点击元素--{}--失败".format(locator))
            log.exception(e)
            # 对当前页面进行截图
            self.save_scree_image(img_info)
            raise e
        else:
            log.info("元素--{}--点击成功".format(locator))

    def input_text(self, locator, text_value, img_info):
        """
        文本内容输入
        :param locator: 元素定位表达式
        :param text_value: 输入的文本内容
        :param img_info: 错误截图信息
        :return:
        """
        try:
            self.driver.find_element(*locator).send_keys(text_value)
        except Exception as e:
            # 输出日志
            log.error("输入文本--{}--失败".format(locator))
            log.exception(e)
            # 对当前页面进行截图
            start_time = time.time()
            filename = '{}_{}.png'.format(img_info, start_time)
            file_path = os.path.join(ERROR_IMG, filename)
            self.driver.save_screenshot(file_path)
            log.info("错误页面截图成功，图表保存的路径:{}".format(file_path))
            raise e
        else:
            log.info("文本内容输入--{}--成功".format(locator))

    def get_element(self, locator, img_info):
        """
        获取元素
        :param locator: 元素定位表达式
        :param img_info: 错误截图信息
        :return:
        """
        try:
            ele = self.driver.find_element(*locator)
        except Exception as e:
            # 输出日志
            log.error("获取元素--{}--失败".format(locator))
            log.exception(e)
            # 对当前页面进行截图
            self.save_scree_image(img_info)
            raise e
        else:
            log.info("元素--{}--获取成功".format(locator))
            return ele

    def save_scree_image(self, img_info):
        """
        对当前页面进行截图
        :param img_info: 错误截图信息
        :return:
        """
        start_time = time.time()
        filename = '{}_{}.png'.format(img_info, start_time)
        file_path = os.path.join(ERROR_IMG, filename)
        self.driver.save_screenshot(file_path)
        log.info("错误页面截图成功，图表保存的路径:{}".format(file_path))
