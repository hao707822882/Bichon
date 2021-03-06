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
'''
{'ServiceModule': {'path': 'F:\\sourceReading\\Bichon\\com\\check\\agent\\module\\monitoring\\service\\ServiceModule.py', 'package': 'com.check.agent.module.monitoring.service.ServiceModule'}, 'MemModule': {'path': 'F:\\sourceReading\\Bichon\\com\\check\\agent\\module\\monitoring\\mem\\MemModule.py', 'package': 'com.check.agent.module.monitoring.mem.MemModule'}, 'CpuModule': {'path': 'F:\\sourceReading\\Bichon\\com\\check\\agent\\module\\monitoring\\cpu\\CpuModule.py', 'package': 'com.check.agent.module.monitoring.cpu.CpuModule'}, 'NetModule': {'path': 'F:\\sourceReading\\Bichon\\com\\check\\agent\\module\\monitoring\\net\\NetModule.py', 'package': 'com.check.agent.module.monitoring.net.NetModule'}, 'DiskModule': {'path': 'F:\\sourceReading\\Bichon\\com\\check\\agent\\module\\monitoring\\disk\\DiskModule.py', 'package': 'com.check.agent.module.monitoring.disk.DiskModule'}}
'''

from com.common.fileSystem.FileSystemUtil import FileSystemUtil
from com.common.BaseLoggingObj import BaseLoggingObj
from com.Config import Config
import os

__author__ = 'Administrator'


class ModuleScanner(BaseLoggingObj, object):
    def __init__(self, config=Config):
        BaseLoggingObj.__init__(self, config=config)
        self.moduleMap = {}

    def scan(self, path):
        parentPath = path
        fileList = FileSystemUtil.list(path)
        for path in fileList:
            if path.find(".") == 0:
                continue
            nowPath = parentPath + os.sep + path
            print(nowPath)
            if FileSystemUtil.isFile(nowPath):
                if FileSystemUtil.houZhui(nowPath)[1] == ".py" or FileSystemUtil.houZhui(nowPath)[1] == ".pyc":
                    if nowPath.find("__init__") > 0:
                        continue
                    mudulStr_array = nowPath.split(".")
                    if len(mudulStr_array) == 2:
                        str = mudulStr_array[0]
                        com_index = str.find("com")
                        modul_str = str[com_index:].replace("\\\\", ".").replace("/", ".").replace("\\", ".")
                        nowPath = nowPath.replace("\\\\", os.sep).replace("/", os.sep).replace("\\", os.sep)
                        mu = modul_str.split(".")
                        mu_length = len(mu)
                        mu_name = mu[mu_length - 1]
                        module = {"path": nowPath, "package": modul_str}
                        self.moduleMap.setdefault(mu_name, module)
            else:
                self.scan(nowPath)
