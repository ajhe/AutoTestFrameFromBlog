# coding=utf-8

import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.logger import Logger
from pageobjects.baidu_homepage import HomePage

# mylog = Logger(logger='BaiduSerach').getlog()

class BaiduSerach(unittest.TestCase):
    """
    继承unittest框架的TestCase模块
    """

    '''
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browser = BrowserEngine(self)
        self.driver = browser.open_browser()

    def tearDown(self):
        """
        测试固件的tearDown()的代码，主要是测试结束后的工作
        :return:
        """
        self.driver.quit()
    '''

    @classmethod
    def setUpClass(cls):
        """支持多个test，才关闭浏览器"""

        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """支持多个test，才关闭浏览器"""
        cls.driver.quit()



    def test_baidu_search(self):
        """
        test开头，是unittest框架的测试用例，记得测试用例必须test开头
        :return:
        """
        '''
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(2)
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        '''
        homepage = HomePage(self.driver)
        homepage.type_input_box("selenium")
        homepage.click_search_submit_btn()
        time.sleep(2)
        homepage.get_window_img()
        try:
            assert 'selenium' in self.driver.title
            print ("Test pass")
            # mylog.info("Test pass")
        except Exception as e:
            print("Test Fail", format(e))
            # mylog.info("Test Fail", format(e))

    def test_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_input_box('Python')
        homepage.click_search_submit_btn()
        time.sleep(2)
        homepage.get_window_img()

if __name__ == '__main__':
    unittest.main()