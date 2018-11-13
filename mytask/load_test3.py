# !/usr/local/bin/python3.6
#  -*- coding:utf-8 -*-


#  -*- @Author  : 我爱你 -*-
#  -*- @Software: PyCharm -*-
#  -*- @Time    : 2018/8/30 15:10 -*-


from locust import HttpLocust, TaskSet, task
import json
import queue

class task_set1(TaskSet):
    pass

class BossBehavior(TaskSet):

    user_info = {}

    @classmethod
    def get_user_info(cls, response):
        r = response.json()
        return r


    def on_start(self):
        user = self.locust.users[0]
        url = '/rest/security/admin/designer/login'

        with self.client.post(url=url, data = user, name='登录', catch_response=True) as response:

            if response.status_code != 200:
                print('登录接口请求失败')
            else:
                res_dict = json.loads(response.text)
                if res_dict['status'] != 1:
                    print('登录失败')
                else:
                    self.user_info = res_dict['list'][0]



    @task
    def shop_list(self):
        url = '/rest/o2o/store/list'

        token = self.user_info['tgt']
        headers = {'accesstoken': token}

        with self.client.post(url= url, headers = headers, data={'status': 1}, name='门店列表') as response:

            pass





class User(HttpLocust):

    task_set = BossBehavior
    host = 'http://partner.test.d2cmall.com'
    min_wait = 1000
    max_wait = 3000
    users = [{'userName':'18000000060', 'password':'11111111'}]


