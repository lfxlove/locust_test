# !/usr/local/bin/python3.6
#  -*- coding:utf-8 -*-


#  -*- @Author  : 我爱你 -*-
#  -*- @Software: PyCharm -*-
#  -*- @Time    : 2018/8/30 08:55 -*-

from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    def on_start(self):
        ''''''
        print('start')

    @task
    def baidu_index(self):
        with self.client.get('/', catch_response = True) as response:
            if response.status_code != 200:
                response.failure('Failed!')

            else:
                response.success()


class UserOne(HttpLocust):
    task_set = UserBehavior
    weight = 1
    min_wait = 1000
    max_wait = 3000
    stop_timeout = 5
    host = "https://www.baidu.com"


class UserTwo(HttpLocust):
    weight = 2
    task_set = UserBehavior
    host = 'https://www.baidu.com'

