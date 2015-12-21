#! /usr/bin/env python
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
#  Time: 11:24


__author__ = 'Administrator'
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer


def is_even(n):
    return n % 2 == 0


def list():
    return ["is_even"]


server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on port 8000..."
server.register_function(is_even, "is_even")
server.register_function(list, "list")
server.serve_forever()
