# _*_ coding:utf-8 _*_

from com.common.check.LocalCheck import LocalCheck
from web.broker.BrokerService import BrokerService
from web.dao.BichonDao import BichonDao

from web.service.TimerTaskService import TimerTaskService

__author__ = 'Administrator'


class CheckService(object):
    checkStatue = {}

    def __init__(self):
        self.dao = BichonDao()
        self.timerTaskService = TimerTaskService()

    def processCheck(self, hostKey, processName):
        broker = BrokerService.getBroker(hostKey)
        return broker.processCheck(processName)

    def portCheck(self, hostKey, port):
        broker = BrokerService.getBroker(hostKey)
        return broker.portCheck(port)

    def urlCheck(self, host, port, resource):
        return LocalCheck.httpCheck(host, port, resource=resource)

    def check(self, host, name, port):
        '''mysql check'''
        psData = self.processCheck(host, name)
        portData = self.portCheck(host, port)
        if (len(portData) > 0) and (len(psData) > 0):
            return True
        else:
            return False

    def mysqlCheck(self, host, name="mysql", port="3306"):
        '''mysql check'''
        return self.check(host, name, port)

    def nginxCheck(self, host, port, name="nginx"):
        '''mysql check'''
        return self.check(host, name, port)
