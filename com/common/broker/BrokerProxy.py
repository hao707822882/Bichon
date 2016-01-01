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
#  Time: 11:28


__author__ = 'Administrator'

from com.common.BaseLoggingObj import BaseLoggingObj
from com.Config import Config
from com.common.dymFun.Dym import DymUtil


class BrokerProxy(BaseLoggingObj):
    def __init__(self, proxy, config=Config):
        BaseLoggingObj.__init__(self, config)
        self.target = proxy
        self.command = {}
        self.isError = False
        self.__init()

    def __init(self):
        if self.target is not None:
            try:
                actionList = DymUtil.getattr(self.target, "list")()
                if len(actionList) >= 1:
                    for action in actionList:
                        self.command.setdefault(action, DymUtil.getattr(self.target, action))
            except Exception, e:
                self.isError = True
                self.logging.error("Broker proxy init error ")

    def do(self, actionName):
        return self.command[actionName]()
