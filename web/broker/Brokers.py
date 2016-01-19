# _*_ coding:utf-8 _*_

import xmlrpclib

from com.Config import Config
from web.dao.BichonDao import BichonDao

__author__ = 'Administrator'


class Brokers(object):
    agentMap = {}

    def __init__(self):
        self.bichondao = BichonDao()
        self.initAllServer()

    def getBroker(self, key):
        broker = Brokers.agentMap.get(key)
        if broker is None:
            broker = xmlrpclib.ServerProxy('http://' + key + ':' + str(Config.agent_port))
            Brokers.agentMap.setdefault(key, broker)
        return broker

    def getAllServer(self):
        return self.bichondao.selectServer()

    def initAllServer(self):
        servers = self.getAllServer()
        if len(servers) >= 1:
            for server in servers[0]:
                self.getBroker(server['host'])
