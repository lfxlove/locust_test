# !/usr/local/bin/python3.6
#  -*- coding:utf-8 -*-


#  -*- @Author  : 我爱你 -*-
#  -*- @Software: PyCharm -*-
#  -*- @Time    : 2018/9/5 17:37 -*-



'''个人信息 私有的，外部不许调用'''
class UserInfo():
    ''''''

    def __init__(self, token='', member = {}):
        self._member = member
        self._token = token


    '''用户信息'''
    @property
    def member(self):
        return self._member


    @member.setter
    def member(self, member_info):
        self._member=member_info

        if isinstance(member_info, dict) and member_info['tgt'] is not None:
            # 设置 token 用户令牌
            self.token=member_info.get('tgt', '')


    '''用户登录令牌'''
    @property
    def token(self):
        return self._token


    @token.setter
    def token(self, token):
        self._token=token


    '''清空个人信息'''
    def clearinfo(self):
        self._token=None
        self._member = None

#
#
# '''单例'''
# userInfo = _UserInfo()









