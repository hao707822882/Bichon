# _*_ coding:utf-8 _*_

from web.broker.BrokerService import BrokerService

__author__ = 'Administrator'


class CpuService(object):
    def __init__(self):
        pass

    '''获取cpu状态信息'''

    def getCpuStatue(self, hostKey):
        broker = BrokerService.getBroker(hostKey)
        return broker.getCpuInfo()

    def kill(self, hostKey, pid):
        broker = BrokerService.getBroker(hostKey)
        return broker.shell("kill -9 " + pid)

