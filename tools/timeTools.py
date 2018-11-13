# !/usr/local/bin/python3.6
#  -*- coding:utf-8 -*-


#  -*- @Author  : 我爱你 -*-
#  -*- @Software: PyCharm -*-
#  -*- @Time    : 2018/9/6 09:02 -*-

''''''
'''时间转换相关的工具方法'''

import time, datetime

'''
获取当前时间转换为指定的格式

date_format： 时间格式
'''

def getNowTime(date_format='%Y-%m-%d %H:%M:%S'):
    now = int(time.time())
    timeArray = time.localtime(now)
    formatTime = time.strftime(date_format, timeArray)
    return formatTime


'''
获取当前时间的时间戳
'''

def getNowTimeStamp():

    # 默认情况下python的时间戳是以秒为单位输出的float
    return int(time.time())

'''
时间字符串->时间戳  

timeStr: 时间字符串(eg:2013-10-10 23:40:00)
date_format: 原时间格式
'''

def timeStrtotimeStamp(timeStr, date_format='%Y-%m-%d %H:%M:%S'):
    '''时间字符串->时间戳'''

    timeArray = time.strptime(timeStr, date_format)
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


'''
时间字符串->时间戳 

timeStr: 时间字符串(eg:2013-10-10 23:40:00)
from_fmt: 原时间格式
to_fmt：即将转换成的格式
'''

def changeTimeStyle(timeStr, from_fmt='%Y-%m-%d %H:%M:%S', to_fmt='%Y/%m/%d %H:%M:%S'):
    # 原时间字符串转为数组
    timeArray = time.strptime(timeStr, from_fmt)

    # 转换为其他的时间格式
    otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
    return otherStyleTime


'''
时间戳转换为指定格式的日期

timeStamp: 时间戳
date_format：指定的时间格式
'''

def timeStampToFormatTime(timeStamp, date_format='%Y-%m-%d %H:%M:%S'):
    '''时间戳转换为指定格式的日期'''

    timeArray = time.localtime(timeStamp)
    formatTime = time.strftime(date_format, timeArray)
    return formatTime
