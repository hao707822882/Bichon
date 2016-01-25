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
#  Date: 2016/1/19
#  Time: 14:38

import  SimpleXMLRPCServer,SocketServer
from com.Config import Config
import time,thread
from com.check.agent.module.monitoring.cpu.CpuModule import CpuModule
from com.check.agent.module.monitoring.disk.DiskModule import DiskModule
from com.check.agent.module.monitoring.mem.MemModule import MemModule
from com.check.agent.module.monitoring.net.NetModule import NetModule
from com.check.agent.module.execing.ExecModule import ExecModule
from com.check.agent.module.monitoring.process.CheckModule import CheckModule
from com.check.agent.module.monitoring.process.ProcessModule import ProcessModule
from com.check.agent.module.service.File import FileModule


from com.common.BaseLoggingObj import BaseLoggingObj



class RPCThreading(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
    pass

class Agent(BaseLoggingObj, object):
    def __init__(self):
        BaseLoggingObj.__init__(self)
        self.cpu = CpuModule()
        self.disk = DiskModule()
        self.mem = MemModule()
        self.net = NetModule()
        self.ec = ExecModule()
        self.check = CheckModule()
        self.process = ProcessModule()
        self.file = FileModule()
        self.agent = RPCThreading(("0.0.0.0", Config.agent_port))
        self.registerCpu()
        self.registerDisk()
        self.registerExec()
        self.registerMem()
        self.registerNet()
        self.registerProcess()
        self.registerCheck()
        self.registerFile()
        self.logging.info("客户端程序启动。。。")
        self.agent.serve_forever()

    '''cpu信息'''

    def registerCpu(self):
        self.agent.register_function(self.cpu.getCpuInfo, "getCpuInfo")

    '''disk'''

    def registerDisk(self):
        self.agent.register_function(self.disk.getDiskInfo, "getDiskInfo")
        self.agent.register_function(self.disk.getPathDetail, "getPathDetail")

    '''mem'''

    def registerMem(self):
        self.agent.register_function(self.mem.getMemInfo, "getMemInfo")

    '''net'''

    def registerNet(self):
        self.agent.register_function(self.net.getNetInfo, "getNetInfo")

    '''ec'''

    def registerExec(self):
        self.agent.register_function(self.ec.execCmd, "execCmd")

    '''process'''
    def registerProcess(self):
        self.agent.register_function(self.process.getPids, "getPids")
        self.agent.register_function(self.process.processInfo, "getProcessInfo")
        self.agent.register_function(self.process.getCusProcessInfo, "getCusProcessInfo")
        self.agent.register_function(self.process.iptableList, "iptableList")
    '''check'''
    def registerCheck(self):
        self.agent.register_function(self.check.portCheck, "portCheck")
        self.agent.register_function(self.check.processCheck, "processCheck")
        self.agent.register_function(self.check.urlCheck, "urlCheck")

    '''file'''
    def registerFile(self):
        self.agent.register_function(self.file.readFile, "readFile")
        self.agent.register_function(self.file.overwriteFile, "overwriteFile")
        self.agent.register_function(self.file.downloadFile, "downloadFile")

