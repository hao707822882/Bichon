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

from com.common.BaseLoggingObj import BaseLoggingObj
from com.common.BaseLoggingObj import logger
import json
import psutil

__author__ = 'Administrator'


class DiskModule(BaseLoggingObj, object):
    def __init__(self):
        BaseLoggingObj.__init__(self)
        self.logging.info("DiskModule added")

    def list(self):
        return {"type": "disk", "items": [{"name": "存储信息", "function": "getDiskInfo"}]}

    def __getDiskPartitionInfo(self):
        return psutil.disk_partitions()

    def __getDiskPartitionUsageInfo(self, path):
        return psutil.disk_usage(path)

    def getDiskInfo(self):
        diskInfo = []
        partitions = self.__getDiskPartitionInfo()
        for partition in partitions:
            diskInfo.append({"partition": partition[0], "detail": self.__getDiskPartitionUsageInfo(partition[0])})
        return json.dumps(diskInfo)


DiskModule().getDiskInfo()