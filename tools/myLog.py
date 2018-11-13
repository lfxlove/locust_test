# !/usr/local/bin/python3.6
#  -*- coding:utf-8 -*-


#  -*- @Author  : 我爱你 -*-
#  -*- @Software: PyCharm -*-
#  -*- @Time    : 2018/9/5 13:44 -*-


import logging, os, sys, time
from datetime import datetime

obj_dir = os.path.dirname(os.path.dirname(__file__))

class MyLog():
    '''自定义日志输出，记录在文件'''

    '''初始化'''
    def __init__(self, loggerName = 'root', filename='log.log', filemode='a', format="[%(asctime)s]: %(levelname)s:%(name)s:%(message)s",datefmt='%Y-%m-%d %I:%M:%S', level=logging.INFO, **kwargs):

        filename = os.path.join(obj_dir, 'log_file', filename)
        print('filename--->'+ filename)
        logging.basicConfig(filename=filename, filemode=filemode, format=format, datefmt=datefmt, level=level, **kwargs)
        self.logger = logging.getLogger(loggerName)
        self.logger.setLevel(level=level)


    '''debug'''
    def debug(self, msg, print_is = False, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)
        if print_is:
            self.__print('DEBUG', msg)

    '''info'''
    def info(self, msg, print_is = False, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)
        if print_is:
            self.__print('INFO', msg)


    '''waring'''
    def waring(self, msg, print_is = False, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)
        if print_is:
            self.__print('WARING', msg)


    '''error'''
    def error(self, msg, print_is = False, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)
        if print_is:
            self.__print('ERROR', msg)


    '''critical'''
    def critical(self, msg, print_is = False, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)
        if print_is:
            self.__print('ERROR', msg)



    '''调用Python的print函数'''
    def __print(self, level, msg):
        '''调用Python的print函数'''

        print('[{}]: {}: {}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), level, msg))


# 基类原始的 也是logging模块默认的
rootLog = MyLog()

# 自定义的
cuslog = MyLog(loggerName='CUSTOM_LOG')

'''还有其他的，还可以继续创建，'''