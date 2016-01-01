#! /usr/bin/env python
# --coding:utf-8--
# coding: utf-8
# ━━━━━━神兽出没━━━━━━
#  　　　┏┓　　　┏┓
#  　　┏┛┻━━━┛┻┓
#  　　┃　　　　　　　┃
#  　　┃　　　━　　　┃
#  　　┃　┳┛　┗┳　┃
#  　　┃　　　　　　　┃
#  　　┃　　　┻　　　┃
#  　　┃　　　　　　　┃
#  　　┗━┓　　　┏━┛
#  　　　　┃　　　┃神兽保佑, 永无BUG!
#  　　　　┃　　　┃Code is far away from bug with the animal protecting
#  　　　　┃　　　┗━━━┓
#  　　　　┃　　　　　　　┣┓
#  　　　　┃　　　　　　　┏┛
#  　　　　┗┓┓┏━┳┓┏┛
#  　　　　　┃┫┫　┃┫┫
#  　　　　　┗┻┛　┗┻┛
#  ━━━━━━感觉萌萌哒━━━━━━
#  Module Desc:clover
#  User: z.mm | 2428922347@qq.com
#  Date: 2015/12/22
#  Time: 11:49


__author__ = 'Administrator'

from com.common.BaseLoggingObj import BaseLoggingObj
from com.common.BaseLoggingObj import logger
from com.common.broker.BrokerProxy import BrokerProxy
from com.common.rpc.AbsBroker import AbsBroker
from com.Config import Config
import xmlrpclib


class DefaultBroker(AbsBroker, BaseLoggingObj):
    def __init__(self, agents=[], config=Config):
        BaseLoggingObj.__init__(self, config=config)
        AbsBroker.__init__(self, agents=agents, config=config)

    @logger
    def initAgent(self, agents=[]):
        if len(agents) <= 0:
            return
        for agent in agents:
            host = agent['host']
            port = agent['port']
            proxy = xmlrpclib.ServerProxy("http://%s:%s/" % (host, port))
            brokerProxy = BrokerProxy(proxy)
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
