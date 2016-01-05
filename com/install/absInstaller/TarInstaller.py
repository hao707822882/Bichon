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
#  Date: 2016/1/5
#  Time: 16:53

from com.install.absInstaller.AbsInstaller import AbsInstaller
from abc import ABCMeta, abstractmethod

__author__ = 'Administrator'


class TarInstaller(AbsInstaller, object):
    __metaclass__ = ABCMeta

    def __init__(self):
        AbsInstaller.__init__(self)

    @abstractmethod
    def downloadTar(self):
        pass

    @abstractmethod
    def make(self):
        pass

    @abstractmethod
    def unTar(self):
        pass

    @abstractmethod
    def writeConfig(self):
        pass

    def install(self):
        pass
