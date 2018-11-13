# !/usr/local/bin/python3.6
#  -*- coding:utf-8 -*-


#  -*- @Author  : 我爱你 -*-
#  -*- @Software: PyCharm -*-
#  -*- @Time    : 2018/9/30 11:40 -*-

from locust import HttpLocust

'''
自定义的HttpLocust基类
以后所有的taskset都继承这个类
'''
class BaseHttpLocust(HttpLocust):


    userInfo = None
    '''用户信息的保存'''

    host = None
    """被测 host """

    min_wait = 1000
    """各个行为的最小间隔时间"""

    max_wait = 1500
    """各个行为之间 的最大间隔时间"""

    task_set = None
    """用户行为集合（TaskSet 子类）"""

    stop_timeout = 30*1000
    """超时时间"""

    weight = 10
    """权重"""


    def __init__(self):
        super().__init__()
