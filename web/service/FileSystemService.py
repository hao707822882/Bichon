# _*_ coding:utf-8 _*_

from web.broker.Brokers import Broker

__author__ = 'Administrator'


class FileSystemService(object):
    def __init__(self):
        pass

    def partitionInfo(self, hostKey):
        broker = Broker.getBroker(hostKey)
        return broker.getPtitionInfo()

    def ls(self, hostKey, path):
        broker = Broker.getBroker(hostKey)
        return broker.ls(path)

    def rm(self, hostKey, path):
        broker = Broker.getBroker(hostKey)
        return broker.rm(path)

    def cp(self, hostKey, path):
        broker = Broker.getBroker(hostKey)
        return broker.cp(path)
