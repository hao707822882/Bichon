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
#  Date: 2016/1/1
#  Time: 15:06

import psutil

from com.common.BaseLoggingObj import BaseLoggingObj
import json
import time

__author__ = 'Administrator'


class ProcessModule(BaseLoggingObj, object):
    def __init__(self):
        BaseLoggingObj.__init__(self)
        self.logging.info("create NetModule")

    def getPids(self):
        '''获取进程列表'''
        pids = []
        for proc in psutil.process_iter():
            try:
                process = {}
                process.setdefault("pid", proc.pid)
                process.setdefault("name", proc.name())
                pids.append(process)
            except Exception, e:
                self.logging.info("get process error %s", str(e))
        return json.dumps(pids, encoding="utf-8")

    def processInfo(self, pid):
        '''获取进程信息'''
        p = psutil.Process(pid=pid)
        ACCESS_DENIED = ''
        dta = p.as_dict(ad_value=ACCESS_DENIED)
        return json.dumps(dta, encoding="utf-8")


    def getCusProcessInfoInternal(self, attrs=['pid', 'name', 'username', 'exe', 'cpu_percent', 'memory_info', 'threads', 'cmdline']):
        '''获取具体属性值'''
        data = []
        for p in psutil.process_iter():
            try:
                d = p.as_dict(attrs)
                data.append(d)
            except psutil.NoSuchProcess:
                pass
        return data

    def getCusProcessInfo(self, attrs=['pid', 'name', 'username', 'exe', 'cpu_percent', 'memory_info', 'threads', 'cmdline']):
        self.getCusProcessInfoInternal(attrs=attrs)
        time.sleep(1)
        data=self.getCusProcessInfoInternal(attrs=attrs)
        return json.dumps(data, encoding="utf-8")

