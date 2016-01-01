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
import psutil

__author__ = 'Administrator'

export = [{"cpu��Ϣ": "getCpuInfo"}]


class CpuModule(BaseLoggingObj, object):
    def __init__(self):
        BaseLoggingObj.__init__(self)
        logger("CpuModule added !")

    '''
        ��ȡcpu��Ϣ
    '''

    def getCpuInfo(self):
        return psutil.cpu_times(percpu=True)
