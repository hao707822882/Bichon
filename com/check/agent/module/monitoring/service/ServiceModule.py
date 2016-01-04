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
from com.common.check.LocalCheck import LocalCheck

__author__ = 'Administrator'


class ServiceModule(BaseLoggingObj, object):
    def list(self):
        return {"type": "Service",
                "items": [{"name": "mysql", "function": "getMysqlInfo"},
                          {"name": "mysqls", "function": "getMysqlsInfo"},
                          {"name": "nginx", "function": "getNginxInfo"},
                          {"name": "nginxs", "function": "getNginxsInfo"}]}

    def __init__(self):
        BaseLoggingObj.__init__(self)
        self.logging.info("create ServiceModule !")

    '''
        检测多个Mysql服务状态
    '''

    def getMysqlsInfo(self, *ports):
        status = {}
        for port in ports:
            status.setdefault(port, self.getMysqlInfo(port=port))
        return status

    '''
        检测Mysql服务
    '''

    def getMysqlInfo(self, port=3306):
        if len(LocalCheck.psCheck("mysql")) > 1 and len(LocalCheck.portCheck(port)) > 0:
            return True
        else:
            return False

    '''
           检测nginx服务
    '''

    def getNginxInfo(self, port=3306):
        if len(LocalCheck.psCheck("nginx")) > 1 and len(LocalCheck.portCheck(port)) > 0:
            return True
        else:
            return False

    '''
        检测nginx多端口
    '''

    def getNginxsInfo(self, *ports):
        status = {}
        for port in ports:
            status.setdefault(port, self.getNginxInfo(port=port))
