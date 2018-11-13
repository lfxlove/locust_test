# !/usr/local/bin/python3.6
#  -*- coding:utf-8 -*-


#  -*- @Author  : 我爱你 -*-
#  -*- @Software: PyCharm -*-
#  -*- @Time    : 2018/9/6 09:14 -*-

import json

'''
json转换 Python数据类型
jsonStr： json格式字符串
'''
def jsonToPythonData(jsonStr):
    '''json转换 Python数据类型'''

    data =  json.loads(jsonStr)
    return data


'''
Python类型数据转换 json格式字符串
data： Python 数据类型
'''
def pythonDataToJson(data):
    '''Python类型数据转换 json格式字符串'''

    json_str = json.dumps(data)
    return json_str