# _*_ coding:utf-8 _*_

from web.broker.Brokers import Broker

__author__ = 'Administrator'


class CpuService(object):
    def __init__(self):
        pass

    '''获取cpu状态信息'''

    def getCpuStatue(self, hostKey):
        broker = Broker.getBroker(hostKey)
        return broker.getPtitionInfo()

    def kill(self, hostKey, pid):
        broker = Broker.getBroker(hostKey)
        return broker.shell("kill -9 " + pid)
