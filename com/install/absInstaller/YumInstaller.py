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
#  ━━━━━━感觉萌萌哒━━━━━━#  Module Desc:clover
#  Module Desc:clover
#  User: z.mm | 2428922347@qq.com
#  Date: 2016/1/5
#  Time: 16:53

from abc import ABCMeta, abstractmethod
from com.install.absInstaller.AbsInstaller import AbsInstaller

__author__ = 'Administrator'


class YumInstaller(AbsInstaller, object):
    def install(self):
        self.yumInstall()
        self.writeConfig()

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def yumInstall(self):
        pass

    @abstractmethod
    def writeConfig(self):
        pass
