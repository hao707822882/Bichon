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
        return json.dumps(pids, encoding="mbcs")

    def processInfo(self, pid):
        '''获取进程信息'''
        p = psutil.Process(pid=pid)
        ACCESS_DENIED = ''
        dta = p.as_dict(ad_value=ACCESS_DENIED)
        return json.dumps(dta, encoding="mbcs")

    def getCusProcessInfo(self, attrs=['pid', 'name', 'username', 'exe', 'memory_info', 'threads', 'cmdline']):
        '''获取具体属性值'''
        pids = json.loads(self.getPids())
        data = []
        for pid in pids:
            try:
                d = {}
                id = pid["pid"]
                p = psutil.Process(pid=id)
                ACCESS_DENIED = ''
                dta = p.as_dict(ad_value=ACCESS_DENIED,
                                attrs=attrs)
                d.setdefault("id", id)
                d.setdefault("data", dta)
                data.append(d)
            except Exception, e:
                self.logging.info("get process error %s", str(e))
        return json.dumps(data, encoding="mbcs")
