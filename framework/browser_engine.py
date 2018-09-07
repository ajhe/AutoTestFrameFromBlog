# coding=utf-8

import ConfigParser
import os
import time
from framework.logger import Logger
from selenium import webdriver

logger = Logger(logger='BrowserEngine').getlog()

class BrowserEngine(object):

    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    chrome_driver_path = root_path + '/tools/chromedriver.exe'
    firefox_driver_path = root_path + '/tools/geckodriver.exe'

    def __init__(self, driver):
        self.driver = driver

    #read this config file(config.ini) return use which driver
    def open_browser(self):
        config = ConfigParser.ConfigParser()
        #config file path
        config_file_path = self.root_path + '/config/config.ini'

        #read config file
        config.read(config_file_path)
        browser = config.get('browserType', 'browserName')
        logger.info("You had select %s browser" % browser)
        url = config.get('testServer', 'URL')
        logger.info("The test server url is:%s" % url)

        if browser == 'Firefox':
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser")
            time.sleep(2)
            logger.info("Waiting 2 seconds")
        elif browser == 'Chrome':
            driver = webdriver.Chrome()
            logger.info("Starting chrome browser")
            time.sleep(2)
            logger.info("Waiting 2 seconds")
        elif browser == 'IE':
            driver = webdriver.Ie()
            logger.info("Starting IE browser")
            time.sleep(2)
            logger.info("Waiting 2 seconds")

        driver.get(url)
        logger.info("Open url:%s" % url)
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser")
        self.driver.quit()



