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
#  Time: 18:02


import os

from com.common.BaseLoggingObj import BaseLoggingObj
from com.install.absInstaller.TarInstaller import TarInstaller
from com.common.execCommand.ExecUtil import ExecUtil
from com.Config import Config

__author__ = 'Administrator'


class JavaInstaller(BaseLoggingObj, TarInstaller, object):
    def __init__(self, config=Config):
        BaseLoggingObj.__init__(self, config)
        TarInstaller.__init__(self, )
        self.name = "jdk1.8.64.tar.gz"

    def what(self):
        return "java"

    def __init__(self, config=Config):
        BaseLoggingObj.__init__(self, config)
        TarInstaller.__init__(self)
        self.downloadPath = Config.softServer + "/" + Config.soft_java
        self.downloadSavePath = Config.softSavePath + "/" + Config.soft_java
        self.installPath = Config.softInstallPath
        self.logging.info("add JavaInstaller module!")

    def downloadTar(self):
        down_rt = ExecUtil.execCommand("wget -O " + self.downloadSavePath + " " + self.downloadPath)

    def writeConfig(self):
        f = open("/etc/profile", 'a')
        f.write('export JAVA_HOME=' + self.installPath + "/java")
        f.write("export PATH=$JAVA_HOME/bin:$PATH")
        f.close()
        source_rt = ExecUtil.execCommand("source /etc/profile")

    def make(self):
        tar_rt = ExecUtil.execCommand("tar zxvf " + self.downloadSavePath + " -C " + self.installPath)

    def unTar(self):
        pass
