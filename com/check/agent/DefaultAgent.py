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
from com.common.BaseLoggingObj import BaseLoggingObj
from com.common.BaseLoggingObj import logger
from com.common.type.Type import Type
from com.common.dymFun.Dym import DymUtil
from com.check.agent.ModuleScanner import ModuleScanner

from com.Config import Config


class DefaultAgent(AbsAgent, BaseLoggingObj):
    @logger
    def regisFunc(self):
        self.findModule()
        keys = self.moduleMap.keys()
        for key in keys:
            item = self.moduleMap[key]
            if type(item) != type(Type.map):
                continue
            module = DymUtil.getModuleFromFile(item["path"], item["package"])
            clazz = DymUtil.getattr(module, key)
            target = clazz()
            export = target.list()
            if export is None:
                continue
            func_collection = export["items"]
            for each_func in func_collection:
                self.server.register_function(DymUtil.getattr(target, each_func["function"]), each_func["function"])
            self.listArray.append(export)
            print(export)
        self.server.register_function(self.list, "list")

    '''导出当前服务器需要的检测'''

    def list(self):
        return self.listArray

    def __init__(self, config=Config):
        self.muScanner = ModuleScanner(config)
        self.listArray = []
        BaseLoggingObj.__init__(self, config=config)
        AbsAgent.__init__(self, config=config)

    def findModule(self):
        self.muScanner.scan(Config.module_path)
        self.moduleMap = ModuleScanner.moduleMap

