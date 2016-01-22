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
#  Date: 2016/1/20
#  Time: 18:14

from web.service.task.MysqlTask import MysqlTask
from web.service.task.NginxTask import NginxTask
from web.service.task.UrlTask import UrlTask
from web.dao.BichonDao import BichonDao
from web.service.TimerTaskService import TimerTaskService
from web.service.CheckService import CheckService

__author__ = 'Administrator'

import logging
import time

logging.basicConfig()


class TaskHelper(object):
    def __init__(self):
        self.dao = BichonDao()
        self.timerTaskService = TimerTaskService()
        self.initState = False
        try:
            self.initTasks()
        except Exception,e:
            print "monitor task init error you can not get monitoring data"

    def initTasks(self):
        if self.initState:
            return
        '''初始化所有存储在数据库中的任务'''
        self.initState = True
        data = self.dao.selectServiceWithServer()
        if len(data) == 1:
            for service in data[0]:
                if service["execType"] == "mysql":
                    mysqlTask = MysqlTask(service["serverId"],service["port"], service["host"])
                    self.timerTaskService.addJob(service["lab"], str(service["serverId"])+":"+service["host"] +":"+service["lab"],
                                                 mysqlTask.check, "*/5", "*", "*")
                elif service["execType"] == "nginx":
                    nginxTask = NginxTask(service["serverId"],service["port"], service["host"])
                    self.timerTaskService.addJob(service["lab"], str(service["serverId"])+":"+service["host"]+":"+service["lab"],
                                                 nginxTask.check, "*/5", "*", "*")
                elif service["execType"] == "url":
                    urlTask = UrlTask(service["serverId"],service["port"].encode("utf-8"), service["host"].encode("utf-8"),
                                      service["url"].encode("utf-8"), service["lab"].encode("utf-8"))
                    # urlTask = UrlTask("80", "www.baidu.com", "/", "baiduService")
                    self.timerTaskService.addJob(service["lab"], str(service["serverId"])+":"+service["host"]+":"+service["lab"],
                                                 urlTask.check, "*/5", "*", "*")



    def addTask(self, execType, serverId, port, host, lab, url):
        if execType== "mysql":
            mysqlTask = MysqlTask(serverId,port,host)
            self.timerTaskService.addJob(lab, serverId+":"+host +":"+lab,
                                         mysqlTask.check, "*/5", "*", "*")
        if execType== "nginx":
            nginxTask = NginxTask(serverId,port,host)
            self.timerTaskService.addJob(lab, serverId+":"+host+":"+lab,
                                     nginxTask.check, "*/5", "*", "*")
        if execType== "url":
            urlTask = UrlTask(serverId,port, host,url, lab)
            # urlTask = UrlTask("80", "www.baidu.com", "/", "baiduService")
            self.timerTaskService.addJob(lab, serverId+":"+host+":"+lab,urlTask.check, "*/5", "*", "*")
