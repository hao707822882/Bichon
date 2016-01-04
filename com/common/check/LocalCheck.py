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
#  Date: 2016/1/4
#  Time: 15:59
import commands
import httplib

__author__ = 'Administrator'


class LocalCheck(object):
    @staticmethod
    def psCheck(what):
        rt = commands.getstatusoutput("ps -ef | grep " + what)
        rt_Array = rt[1].replace("\r\n", "\n").split("\n")
        return rt_Array

    @staticmethod
    def portCheck(port):
        rt = commands.getstatusoutput("netstat -anp | grep " + port)
        rt_Array = rt[1].replace("\r\n", "\n").split("\n")
        return rt_Array

    @staticmethod
    def httpCheck(host, port, resource="/"):
        conn = httplib.HTTPConnection(host, port)
        req = conn.request('GET', resource)
        response = conn.getresponse()
        if response.status in [200, 301]:
            return True
        else:
            return False


print LocalCheck.httpCheck("www.baidu.com", 80)
