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
#  Time: 11:11


__author__ = 'Administrator'
from com.common.BaseLoggingObj import BaseLoggingObj
from com.Config import Config
from abc import ABCMeta, abstractmethod

'''
    agents is an arrary
        struct like [{host,port},{host,port}]
'''


class AbsBroker(BaseLoggingObj):
    __metaclass__ = ABCMeta

    def __init__(self, config=Config):
        self.name = "bichon broker server"
        self.version = Config.version
        self.agents = {}
        self.exportList = []
        self.errorAgents = []
        self.logging.info("broker start over ......")
        BaseLoggingObj.__init__(self, config)

    @abstractmethod
    def initAgent(self):
        pass
