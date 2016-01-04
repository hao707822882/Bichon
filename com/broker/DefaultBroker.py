#! /usr/bin/env python
# --coding:utf-8--
# coding: utf-8
# ���������������޳�û������������
#  ��������������������
#  ���������ߩ��������ߩ�
#  ����������������������
#  ����������������������
#  ���������ש������ס���
#  ����������������������
#  �������������ߡ�������
#  ����������������������
#  ����������������������
#  ���������������������ޱ���, ����BUG!
#  ������������������Code is far away from bug with the animal protecting
#  ��������������������������
#  �������������������������ǩ�
#  ����������������������������
#  �������������������ש�����
#  �������������ϩϡ����ϩ�
#  �������������ߩ������ߩ�
#  �������������о������թ�����������
#  Module Desc:clover
#  User: z.mm | 2428922347@qq.com
#  Date: 2015/12/22
#  Time: 11:49


__author__ = 'Administrator'

import xmlrpclib

from com.common.BaseLoggingObj import BaseLoggingObj
from com.common.BaseLoggingObj import logger
from com.broker.BrokerProxy import BrokerProxy
from com.common.rpc.AbsBroker import AbsBroker
from com.Config import Config


class DefaultBroker(AbsBroker, BaseLoggingObj):
    def __init__(self, config=Config):
        BaseLoggingObj.__init__(self, config=config)
        AbsBroker.__init__(self, config=config)

    @logger
    def initAgent(self, agentsHost):
        if len(agentsHost) <= 0:
            return
        for agent in agentsHost:
            host = agent['host']
            port = agent['port']
            proxy = xmlrpclib.ServerProxy("http://%s:%s/" % (host, port))
            brokerProxy = BrokerProxy(proxy, host)
            if brokerProxy.isError:
                self.errorAgents.append(agent)
            else:
                self.agents.setdefault(host, brokerProxy)

    @logger
    def action(self, host, actionName):
        brokerProxy = self.agents[host]
        if brokerProxy is not None:
            return brokerProxy.do(actionName)
        else:
            return False

    def listExport(self):
        for agent in self.agents:
            exp = self.agents[agent].export
            print(exp)
            self.exportList.append(exp)
        return self.exportList


d = DefaultBroker()
d.initAgent([{"host": "127.0.0.1", "port": 8000}])
print d.action("127.0.0.1", "getMemInfo")
print(d.listExport())
