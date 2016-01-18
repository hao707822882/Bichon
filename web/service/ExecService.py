# _*_ coding:utf-8 _*_
from web.broker.Brokers import Broker

__author__ = 'Administrator'


class ExecService(object):
    def __init__(self):
        pass

    def runShell(self, hostKey, cmd):
        broker = Broker.getBroker(hostKey)
        return broker.runShell(cmd)
