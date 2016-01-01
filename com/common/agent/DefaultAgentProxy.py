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
#  Date: 2015/12/21
#  Time: 18:19

from com.common.agent.AbsAgentProxy import AgentProxy
from com.common.BaseLoggingObj import BaseLoggingObj
from com.common.BaseLoggingObj import logger
from com.Config import Config

__author__ = 'Administrator'


class DefaultAgentProxy(AgentProxy, BaseLoggingObj):
    def __init__(self, config=Config):
        BaseLoggingObj.__init__(self, config=config)
        self.logging.info("init DefaultAgent from file %s", __file__);

    @logger
    def list(self):
        return ["cpu", "net"]

    @logger
    def cpu(self):
        return {"cores": [{"sys": "0.1", "us": "30"}, {"sys": "0.1", "us": "30"}, {"sys": "0.1", "us": "30"},
                          {"sys": "0.1", "us": "30"}]}

    @logger
    def net(self):
        return {"eth": [{"in": "100k", "out": "500"}, {"in": "100k", "out": "500"}, {"in": "100k", "out": "500"},
                        {"in": "100k", "out": "500"}]}
