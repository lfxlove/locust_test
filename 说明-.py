# !/usr/local/bin/python3.6
#  -*- coding:utf-8 -*-


#  -*- @Author  : 我爱你 -*-
#  -*- @Software: PyCharm -*-
#  -*- @Time    : 2018/9/6 14:09 -*-


'''以下是说明部分'''


'''

Taskset子类，该类主要用来定义每个虚拟用户的所有操作行为
@task(weight=num)装饰器去装饰为一个操作行为

HttpLocust子类，该类是用来模拟用户的类

taskset类中interrupt(reschedule=True)方法在顶层的taskset类(即被指定到Locust子类中的taskset)中不可用
reschedule为True时，从被嵌套的任务中出来立即执行新的任务，
如果为False从被嵌套的任务中出来会等待min_time-max_time之间的随机时间，然后再执行新的任务，这个方法主要用来跳出嵌套的任务集

'''


'''

终端运行指令
类的形式开启 locust
locust -f MyLocust.py User_test User4 

分布式相关的
使用master模式启动 （ 设置locust为master模式 ）
locust -f MyLocust.py User_test User4 --master

改变 master 端的ip 或者 端口
--master-bind-host=X.X.X.X
--master-bind-port=xxxx

在每个slave中执行(使用master机器的IP替换192.168.5.23)
locust -f MyLocust.py User_test User4 --slave --master-host=192.168.5.23
指定 master 端的 IP 和 端口号
--master-host=X.X.X.X
--master-port=xxxx  （Defaults to 5557.）

网页交互会在 master节点机器中运行
master机器作为主机 ，slave机器作为备机

'''