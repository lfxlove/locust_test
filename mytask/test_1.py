# !/usr/local/bin/python3.6
#  -*- coding:utf-8 -*-


#  -*- @Author  : 我爱你 -*-
#  -*- @Software: PyCharm -*-
#  -*- @Time    : 2018/9/6 10:33 -*-

from locust import HttpLocust, task
from base import BaseTaskSet
from tools.myLog import rootLog

class UserBehavior(BaseTaskSet):

    def on_start_doOther(self):
        ''''''
        '''首先执行登录事件 ，保存token 以及用户信息'''
        url = '/rest/security/admin/designer/login'
        data = {'userName': '18000000060', 'password': '11111111'}

        res = self.netWord('post', api=url, data=data)
        list = res.get('list', [])
        if len(list) > 0:
            self.userInfo.member = list[0]
            rootLog.debug('登录成功 token ---->' + self.userInfo.token, print_is=True)


    def on_stop_doOther(self):
        pass


    @task
    def brand_list(self):
        '''品牌列表'''

        url = '/rest/shop/designer/list'
        data = {'p': 1}
        self.netWord('post', api=url, data=data)

        rootLog.info('品牌列表'+ '结束', print_is=True)


    @task
    def store_list(self):
        '''门店列表'''

        url = '/rest/o2o/store/list'
        data = {'status': 1, 'p':1}
        res = self.netWord('post', api=url, data=data)

        rootLog.info('门店列表'+ '结束', print_is=True)

    @task
    def buy_prodect_list(self):
        '''采购商品列表'''

        url = '/rest/order/requisitionitem/list'
        data = [('status', 1), ('p', 1), ('types',1), ('types',2), ('types',4) ]
        res = self.netWord('post', api=url, data=data)
        rootLog.info('采购商品列表' + '结束', print_is=True)


    @task
    def back_product_list(self):
        '''退货商品列表'''

        url = '/rest/order/requisitionitem/list'
        data = [('p', 1), ('types', 3), ('types', 5), ('types', 6)]
        res = self.netWord('post', api=url, data=data)
        rootLog.info('退货商品列表'+'结束', print_is=True)



