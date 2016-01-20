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

logging.basicConfig()


class TaskHelper(object):
    def __init__(self):
        self.dao = BichonDao()
        self.timerTaskService = TimerTaskService()
        self.initState = False

    def initTasks(self):
        if self.initState:
            return
        '''初始化所有存储在数据库中的任务'''
        self.initState = True
        data = self.dao.selectServiceWithServer()
        if len(data) == 1:
            for service in data[0]:
                if service["execType"] == "mysql":
                    mysqlTask = MysqlTask(service["port"], service["host"])
                    self.timerTaskService.addJob(service["lab"], service["host"] + service["execCommand"],
                                                 mysqlTask.check, "*/1", "*", "*")
                elif service["execType"] == "nginx":
                    nginxTask = NginxTask(service["port"], service["host"])
                    self.timerTaskService.addJob(service["lab"], service["host"] + service["execCommand"],
                                                 nginxTask.check, "*/1", "*", "*")
                elif service["execType"] == "url":
                    urlTask = UrlTask(service["port"], service["host"], service["url"], service["lab"])
                    self.timerTaskService.addJob(service["lab"], service["host"] + service["lab"],
                                                 urlTask.check, "*/1", "*", "*")


timerTaskService = TimerTaskService()
urlTask = UrlTask("80", "www.baidu.com", "/", "baiduService")
# timerTaskService.addJob("baiduService", "www.baidu.com:baiduService", urlTask.check, "*/1", "*", "*")
urlTask1 = UrlTask("80", "school.iboom.tv", "/school/login.html", "schoolService")
timerTaskService.addJob("schoolService", "school.iboom.tv/school/login.htmlschoolService", urlTask1.check, "*/1", "*",
                        "*")

while True:
    print CheckService.checkStatue
