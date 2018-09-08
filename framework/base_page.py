# coding=utf-8

import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from framework.logger import Logger
import os

mylog = Logger(logger='BasePage').getlog()

class BasePage(object):
    """
    定义一个页面基类，对selenium的常见操作进行封装
    """

    def __init__(self, driver):
        """
        构造函数
        :param driver:
        """
        self.driver = driver

    #退出浏览器
    def quit_browser(self):
        self.driver.quit()
        mylog.info("Quit the browser")

    #浏览器前进操作
    def forward(self):
        self.driver.forward()
        mylog.info("Click forward on current page")

    #浏览器后退操作
    def back(self):
        self.driver.back()
        mylog.info("Click back on current page")

    #获取当前URL地址
    def get_page_url(self):
        mylog.info("Current page URL is : " % self.driver.current_url)
        return self.driver.current_url

    #获取当前窗口标题（title）
    def get_page_title(self):
        mylog.info("Current page title is : " % self.driver.title)
        return self.driver.title

    #设置等待时间
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        mylog.info("wait for %d seconds" % seconds)

    #关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            mylog.info("Closing and quit the browser")
        except NameError as e:
            mylog.info("Failed to quit the browser with %s" % e)

    #保存截图
    def get_window_img(self):
        """
        这里我们把保存截图的路径写死，也就是说统一保存至根目录下的screenshots文件夹
        :return:
        """
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screenshot_folder_path = root_dir + '/screenshots/'
        now_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        screenshot_file_path = screenshot_folder_path + now_time +'.png'
        try:
            self.driver.get_screenshot_as_file(screenshot_file_path)
            mylog.info("Had take screenshot and save to folder : /screenshots/")
        except NameError as e:
            mylog.info("Failed to take screenshot! %s" % e)

    #定位元素方法
    def find_element(self, selector):
        """
        这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
        submit_btn = "id=>su"
        login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
        如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return:
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                mylog.info("Had find the element \' %s \' successful "
                           "by %s via value: %s" %(element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                mylog.error("NoSuchElementException: %s" % e)
                self.get_window_img()
        elif selector_by == 'n' or selector_by == 'name':
            try:
                element = self.driver.find_element_by_name(selector_value)
                mylog.info("Had find the element \' %s \' successful "
                           "by %s via value %s" %(element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                mylog.error("NoSuchElementException: %s" % e)
                self.get_window_img()
        elif selector_by == 'c' or selector_by == 'class_name':
            try:
                element = self.driver.find_element_by_class_name(selector_value)
                mylog.info("Had find the element \' %s \' successful "
                           "by %s via value %s" %(element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                mylog.error("NoSuchElementException: %s" % e)
                self.get_window_img()
        elif selector_by == 'l' or selector_by == 'link_text':
            try:
                element = self.driver.find_element_by_link_text(selector_value)
                mylog.info("Had find the element \' %s \' successful "
                           "by %s via value %s" %(element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                mylog.error("NoSuchElementException: %s" % e)
                self.get_window_img()
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            try:
                element = self.driver.find_element_by_partial_link_text(selector_value)
                mylog.info("Had find the element \' %s \' successful "
                           "by %s via value %s" %(element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                mylog.error("NoSuchElementException: %s" % e)
                self.get_window_img()
        elif selector_by == 't' or selector_by == 'tag_name':
            try:
                element = self.driver.find_element_by_tag_name(selector_value)
                mylog.info("Had find the element \' %s \' successful "
                           "by %s via value %s" %(element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                mylog.error("NoSuchElementException: %s" % e)
                self.get_window_img()
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                mylog.info("Had find the element \' %s \' successful "
                           "by %s via value %s" %(element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                mylog.error("NoSuchElementException: %s" % e)
                self.get_window_img()
        else:
            raise NameError("please enter a valid type of targeting elements.")

        return element

    #输入文本框
    def type(self, selector, text):
        el = self.find_element(selector)
        try:
            el.clear()
            el.send_keys(text)
            mylog.info("Had type \' %s \' in inputBox" % text)
        except AttributeError as a:
            mylog.error(format(a))
            self.get_window_img()
        except NameError as e:
            mylog.error("Failed to type in input box with %s " % e)
            self.get_window_img()
        except BaseException as msg:
            mylog.error("Failed to type in input box with %s " % msg)
            self.get_window_img()

    #清空文本框
    def clear(self, selector):

        el = self.find_element(selector)

        try:
            el.clear()
            mylog.info("Clear text in input box before typing.")
        except NameError as e:
            mylog.error("Failed to clear input box with %s " % e)
            self.get_window_img()

    #点击元素
    def click(self, selector):

        el = self.find_element(selector)

        try:
            el.click()
            mylog.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            mylog.error("Failed to clcik the element with %s " % e)
            self.get_window_img()

    #刷新界面
    def refresh(self):
        self.driver.refresh()
        mylog.info("Refresh the current page.")

    #在浏览器新开一个标签页（tab）
    def open_tab(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        self.wait(2)
        mylog.info("Waiting for 2 seconds, Open a new tab.")

    #获取当前浏览器版本号
    def get_browser_version(self):
        version = self.driver.capabilities['version']
        mylog.info("The browser version is %s." % version)
        return version

    #获取定位元素的文字内容（text）
    def get_element_text(self, selector):
        el = self.find_element(selector)
        try:
            element_text = el.text
            mylog.info("The element text is %s." % element_text)
            return element_text
        except NameError as e:
            mylog.info("Failed to get the text with: %s" % e)
        except Exception as msg:
            mylog.info("Failed to get the text with: %s" % msg)

    #获取元素大小size
    def get_element_size(self, selector):
        el = self.find_element(selector)
        try:
            element_size = el.size
            mylog.info("The element size is %s" % element_size)
            return element_size
        except NameError as e:
            mylog.info("Failed to get the size with: %s" % e)
        except Exception as msg:
            mylog.info("Failed to get the size with: %s" % msg)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        mylog.info("sleep for %d seconds" % seconds)









