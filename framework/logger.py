# coding=utf-8

import time
import os
import logging

class Logger(object):
    """
    define a log class
    """

    def __init__(self, logger):
        """
        构造函数，定义日志格式，日志级别，指定保存日志的文件路径
        调用文件将日志存入指定文件
        :param logger:
        """
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #get log file path
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_folder_path = root_dir + '/logs/'
        now_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        log_file_path = log_folder_path + now_time + '.log'

        #creat a file handler
        fh = logging.FileHandler(log_file_path)
        #set file handler level
        fh.setLevel(logging.INFO)

        #creat a control handler
        ch = logging.StreamHandler()
        #set control handler level
        ch.setLevel(logging.INFO)

        #define handler output format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #set file handler and control handler format
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #add handler to logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        """
        return logger
        :return:
        """
        return self.logger
