# !/usr/local/bin/python3.6
#  -*- coding:utf-8 -*-


#  -*- @Author  : 我爱你 -*-
#  -*- @Software: PyCharm -*-
#  -*- @Time    : 2018/8/30 11:50 -*-


from locust import HttpLocust, TaskSet, task
from random import randint
from locust.clients import HttpSession
from base import BaseTaskSet


class UserBehavior(BaseTaskSet):

    def on_start(self):
        pass

    def login_user(self):
        users = {'15355095064': '12345678', '15355096087': 'qwerdfg'}
        data = list(users.keys())

        username = data[randint(0, len(data)-1)]
        print(username)
        psw = users[username]
        return username, psw


    @task
    def login(self):
        username, psw = self.login_user()
        res = self.netWord('post', api='/rest/security/admin/designer/login', data = {'userName':username, 'password': psw})

        print(res)

        # with self.client.post('/rest/security/admin/designer/login', {'userName':username, 'password': psw}, catch_response=True, name='我爱你') as response:
        #     if response.status_code != 200:
        #         response.failure('失败'+username)
        #     else:
        #         response.success()



class User(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000
    host = 'http://partner.test.d2cmall.com'
    stop_timeout = 5



