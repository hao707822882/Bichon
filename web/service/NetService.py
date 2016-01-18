# _*_ coding:utf-8 _*_
from web.broker.Brokers import Broker

__author__ = 'Administrator'


class NetService(object):
    def __init__(self):
        pass

    '''获取net详细信息'''

    def getNetInfo(self, hostKey):
        broker = Broker.getBroker(hostKey)
        return broker.getNetInfo()
