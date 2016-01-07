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
#  Time: 18:01
import pexpect

from com.common.execCommand.ExecUtil import ExecUtil
from com.common.BaseLoggingObj import BaseLoggingObj
from com.install.absInstaller.YumInstaller import YumInstaller
from com.Config import Config

'''
    yum安装：Is this ok [y/N]:
'''

__author__ = 'Administrator'


class NFSInstaller(BaseLoggingObj, YumInstaller, object):
    def yumInstall(self):
        child = pexpect.spawnu('yum groupinstall " NFS file server"')
        child.expect('(?i)Is this ok [y/N]:')
        child.sendline('y')
        child.expect('Complete!')
        child.close()
        self.writeConfig()
        ExecUtil.execCommand("/etc/init.d/rpcbind start  ")
        ExecUtil.execCommand("/etc/init.d/nfs start")
        ExecUtil.execCommand("chkconfig nfs on")
        ExecUtil.execCommand("chkconfig rpcbind on")

    def __init__(self, config=Config):
        BaseLoggingObj.__init__(self, config)
        YumInstaller.__init__(self)

    def writeConfig(self):
        pass

    def what(self):
        return "nfs"