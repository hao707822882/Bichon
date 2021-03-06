#! /usr/bin/env python
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
#  Time: 11:34


__author__ = 'Administrator'

from SimpleXMLRPCServer import SimpleXMLRPCServer
from com.common.BaseLoggingObj import BaseLoggingObj
from com.Config import Config
from abc import ABCMeta, abstractmethod

'''
    bichon server rpc client

'''


class AbsAgent(BaseLoggingObj):
    __metaclass__ = ABCMeta

    @abstractmethod
    def regisFunc(self):
        pass

    def __init__(self, config=Config):
        self.name = "bichon agent rpc server"
        self.version = Config.version
        self.server = SimpleXMLRPCServer(("localhost", config.agent_port))
        self.regisFunc()
        self.server.serve_forever()
        self.logging.info("agent start over ......")
