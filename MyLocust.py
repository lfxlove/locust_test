# !/usr/local/bin/python3.6
#  -*- coding:utf-8 -*-


#  -*- @Author  : 我爱你 -*-
#  -*- @Software: PyCharm -*-
#  -*- @Time    : 2018/9/6 11:24 -*-

import queue
# from locust import HttpLocust
from base import BaseHttpLocust
from mytask import test_1, load_test2, load_test3, load_test4, load_test1


class UserOne(BaseHttpLocust):
    task_set = load_test1.UserBehavior
    weight = 1
    min_wait = 1000
    max_wait = 3000
    stop_timeout = 5
    host = "https://www.baidu.com"


class UserTwo(BaseHttpLocust):
    weight = 2
    task_set = load_test1.UserBehavior
    host = 'https://www.baidu.com'


class User(BaseHttpLocust):
    task_set = load_test2.UserBehavior
    min_wait = 1000
    max_wait = 3000
    host = 'http://partner.mytask.d2cmall.com'
    stop_timeout = 5


class User3(BaseHttpLocust):

    task_set = load_test3.BossBehavior
    host = 'http://partner.mytask.d2cmall.com'
    min_wait = 1000
    max_wait = 3000
    users = [{'userName':'18000000060', 'password':'11111111'}]


class User4(BaseHttpLocust):
    host = 'https://www.baidu.com'
    task_set = load_test4.UserBehavior
    min_wait = 1000
    max_wait = 3000
    q = queue.Queue()
    q.put(('user1', '1111111'))
    q.put(('user2', '2222222'))
    q.put(('user3', '3333333'))



class User_test(BaseHttpLocust):

    task_set = test_1.UserBehavior
    host = 'http://partner.test.d2cmall.com'
    min_wait = 1000
    max_wait = 5000
    stop_timeout = 20

