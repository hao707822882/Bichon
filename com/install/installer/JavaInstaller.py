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
from com.install.absInstaller import AbsInstaller
from com.common.execCommand.ExecUtil import ExecUtil
from com.Config import Config

__author__ = 'Administrator'


class JavaInstaller(BaseLoggingObj, AbsInstaller, object):
    def install(self):
        downloadPath = Config.softDownloadPath + os.path.sep + self.name
        downloadServerPath = Config.softServer + "/" + Config.soft_java
        installPath = Config.softInstallDir + os.path.sep + "jdk1.8.0_45"  # 安装路径
        down_rt = ExecUtil.execCommand("wget -O " + downloadPath + " " + downloadServerPath)
        if not down_rt:
            raise NameError("jdk下载失败")
        tar_rt = ExecUtil.execCommand("tar zxvf " + downloadPath + " -C " + Config.softInstallDir)
        if not tar_rt:
            raise NameError("tar 解压失败")
        f = open("/etc/profile", 'a')
        f.write('export JAVA_HOME=' + installPath)
        f.write("export PATH=$JAVA_HOME/bin:$PATH")
        f.close()
        source_rt = ExecUtil.execCommand("source /etc/profile")
        if not source_rt:
            raise NameError("source 环境变量失败")

    def __init__(self, config=Config):
        BaseLoggingObj.__init__(self, config)
        AbsInstaller.__init__(self)
        self.name = "jdk1.8.64.tar.gz"
        self.logging.info("add JavaInstaller module!")


JavaInstaller().install()
