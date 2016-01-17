# _*_ coding:utf-8 _*_


from com.common.BaseLoggingObj import BaseLoggingObj
from web.broker.Brokers import Broker

__author__ = 'Administrator'


class InstallService(BaseLoggingObj, object):
    def __init__(self):
        pass

    def installMysql(self, hostKey):
        broker = Broker.getBroker(hostKey)
        broker.installMysql()

    def installNginx(self, hostKey):
        broker = Broker.getBroker(hostKey)
        broker.installNginx()
