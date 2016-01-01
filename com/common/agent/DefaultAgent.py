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
#  Time: 10:22


__author__ = 'Administrator'

from com.common.rpc.AbsAgent import AbsAgent
from com.common.agent.DefaultAgentProxy import DefaultAgentProxy
from com.common.BaseLoggingObj import BaseLoggingObj
from com.common.BaseLoggingObj import logger
from com.Config import Config


class DefaultAgent(AbsAgent, BaseLoggingObj):
    @logger
    def regisFunc(self):
        agentProxy = DefaultAgentProxy()
        self.server.register_function(agentProxy.list, "list")
        self.server.register_function(agentProxy.cpu, "cpu")
        self.server.register_function(agentProxy.net, "net")

    def __init__(self, config=Config):
        BaseLoggingObj.__init__(self, config=config)
        AbsAgent.__init__(self, config=config)


agent = DefaultAgent()
