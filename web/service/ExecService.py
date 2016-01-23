# _*_ coding:utf-8 _*_
from web.broker.BrokerService import BrokerService
__author__ = 'Administrator'


class ExecService(object):
    def __init__(self):
        pass

    def runShell(self, hostKey, cmd):
        broker = BrokerService.getBroker(hostKey)
        return broker.execCmd(cmd)