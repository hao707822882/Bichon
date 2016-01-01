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
#  Time: 11:40


__author__ = 'Administrator'

# !/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

根据函数名称动态调用

根据约定大于编码，包名以com开头，包内要有__init__.py



"""


class DymUtil(object):
    @staticmethod
    def getattr(source, name):
        return getattr(source, name)

    @staticmethod
    def getModuleFromFile(mudelPath, name):
        return __import__("com.common.agent.module.monitoring.cpu.CpuModule", fromlist=[mudelPath])


obj = DymUtil.getModuleFromFile("F:\\sourceReading\\Bichon\\com\\common\\agent\\module\\monitoring\\cpu\\CpuModule.py",
                                "CpuModule")

aClass = getattr(obj, "CpuModule")

print(aClass().getCpuInfo())
