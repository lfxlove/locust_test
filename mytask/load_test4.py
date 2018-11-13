# !/usr/local/bin/python3.6
#  -*- coding:utf-8 -*-


#  -*- @Author  : 我爱你 -*-
#  -*- @Software: PyCharm -*-
#  -*- @Time    : 2018/8/30 16:33 -*-

import queue
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    def on_start(self):
        try:
            user, psw = self.locust.q.get()
            print(user, psw)
        except:
            print('完了')


    @task
    def lo(self):
        print('xxxxxxxxxx')
        pass


class User(HttpLocust):
    host = 'https://www.baidu.com'
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000
    q = queue.Queue()
    q.put(('user1', '1111111'))
    q.put(('user2', '2222222'))
    q.put(('user3', '3333333'))
    pass

