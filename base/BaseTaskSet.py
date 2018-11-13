# !/usr/local/bin/python3.6
#  -*- coding:utf-8 -*-


#  -*- @Author  : 我爱你 -*-
#  -*- @Software: PyCharm -*-
#  -*- @Time    : 2018/9/6 09:33 -*-

from locust import TaskSet
from tools.jsonTools import jsonToPythonData
from info import UserInfo
from tools.myLog import rootLog

'''
自定义的TaskSet基类
以后所有的taskset都继承这个类
'''
class BaseTaskSet(TaskSet):
    '''自定义的TaskSet基类'''

    '''用户信息'''
    @property
    def userInfo(self):
        if self.locust.userInfo is None:
            self.locust.userInfo = UserInfo()
        return self.locust.userInfo

    @userInfo.setter
    def userInfo(self, value):
        if isinstance(UserInfo, value) or value is None:
            self.locust.userInfo = value


    '''
    TaskSet 原始的 on_start
    这个函数在其他task执行之前，最先执行，而且只执行一次。可以把 on_start 函数看成是为其他接口准备条件的， 比如token
    '''
    def on_start(self):
        self.on_start_doOther()


    '''
    TaskSet 原始的 on_stop
    on_stop是结尾方法，会在结束时执行
    '''
    def on_stop(self):
        self.on_stop_doOther()

    '''
    子类中实现
    相当于  on_start
    '''
    def on_start_doOther(self):

        pass


    '''
    子类中实现
    相当于  on_stop
    '''
    def on_stop_doOther(self):
        pass


    '''***************************
    以下是对网络请求的相关操作的封装
    *****************************************'''

    '''headers 的操作'''
    def _migrateHeaders(self, headers):
        '''headers 的操作'''

        tem_headers = self.client.headers

        if tem_headers is None:
            tem_headers = {}

        # 如果还有其他的headers 合并到 self.client.headers
        if headers is not None:
            tem_headers.update(headers)


        # 判断 token， header 添加 token
        if (self.userInfo.token is not None) and (len(self.userInfo.token) > 0):
            tem_headers.update({'accesstoken': self.userInfo.token})

        return tem_headers

    '''
    对请求的data参数进行相关处理
    '''
    def _net_dataAction(self, data):

        pass


    '''
    对请求的params参数进行处理
    '''
    def _net_paramsAction(self, params):

        pass


    '''
    解析网络请求后的结果
    response： 网络请求结果
    '''
    def analysisResponse(self, response):

        json_data = response.text
        return jsonToPythonData(json_data)


    '''
    判断请求后的结果是否正确
    status： 接口数据 正确的标志（服务端返回的， 与 response.status_code 不同）
    '''
    def responseStatusJudge(self, response, status=1):
        '''判断请求后的结果是否正确'''

        if response.status_code != 200:
            rootLog.error('请求失败 status_code= '+ str(response.status_code) + ' Api = '+ response.request.url)
            return [False, '请求失败 status_code= '+ str(response.status_code) + ' Api = '+ response.request.url]

        # status_code == 200 开始解析数据
        resDict = self.analysisResponse(response)
        if resDict.get('status', 0) != status:

            rootLog.error(resDict.get('message', '没有key->message')  + ' Api = '+ response.request.url, print_is=True)
            return [False, resDict.get('message', '没有key->message')  + ' Api = '+ response.request.url]

        return [True, '']



    '''
    网络请求， 重新封装 self.client的请求， get请求的参数一般用params  post请求的参数用 data
    
    参数设置参考
    method, url,params = None, data = None, headers = None, cookies = None, files = None,
    auth = None, timeout = None, allow_redirects = True, proxies = None,
    hooks = None, stream = None, verify = None, cert = None, json = None
    '''
    def netWord(self, method, api , data = None, params = None, headers = None, name=None, catch_response=True, **kwargs):
        '''网络请求， 重新封装 self.client的请求'''

        # 请求的名字
        if name is None or len(name) == 0:
            name = api

        '''
        如果有需求， 
        可以在此处可进行参数的加密 header的设置等操作
        加密前，判断data 以及 params的数据类型
        '''
        tem_headers = self._migrateHeaders(headers)
        # 只有参数存在的时候，进一步的处理才有意义
        if data is not None:
            tem_data = self._net_dataAction(data)

        if params is not None:
            tem_params = self._net_paramsAction(params)

        # Python 字典 setdefault() 函数和get() 方法类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
        kwargs.setdefault('allow_redirects', True)
        with self.client.request(method, api, data = tem_data, params = tem_params, headers = tem_headers,
                            name=name, catch_response=catch_response, **kwargs) as response:
            judge_res = self.responseStatusJudge(response, status=1)

            # 请求结果的判断，以便标记
            if judge_res[0]:
                response.success()
                return self.analysisResponse(response)
            else:
                response.failure('失败' + judge_res[1])
                return {}


