# !/usr/local/bin/python3.6
#  -*- coding:utf-8 -*-


#  -*- @Author  : 我爱你 -*-
#  -*- @Software: PyCharm -*-
#  -*- @Time    : 2018/9/6 09:03 -*-

''''''
'''加密相关的工具方法'''

import hashlib, base64


'''字符串 Md5 加密'''
def md5Str(targetStr):
    '''字符串 Md5 加密'''

    if isinstance(targetStr, str):
        # 字符串不为 None ，进行加密， 否则返回空
        if targetStr is not None:
            hash_M = hashlib.md5()
            hash_M.update(targetStr.encode(encoding='utf-8'))
            return hash_M.hexdigest()

        return ''

    # 不是字符串的返回原数据
    return targetStr


'''base64 加密字符串'''
def base64Str(targetStr):
    '''base64 加密字符串'''

    if isinstance(targetStr, str):
        # 字符串不为 None ，进行加密， 否则返回空
        if targetStr is not None:
            encodeStr = base64.b64encode(targetStr.encode('utf-8'))
            return encodeStr

        return ''

    return targetStr