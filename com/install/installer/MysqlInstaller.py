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


class MysqlInstaller(BaseLoggingObj, YumInstaller, object):
    def yumInstall(self):
        child = pexpect.spawnu('yum install mysql*')
        child.expect('(?i)Is this ok [y/N]:')
        child.sendline('y')
        child.expect('Complete!')
        child.close()
        self.writeConfig()
        ExecUtil.execCommand("service mysqld restart")
        ExecUtil.execCommand("mysqladmin -u root password " + Config.mysqlRoot)
        ExecUtil.execCommand("mysql -uroot -p" + Config.mysqlRoot + "-e select version()")

    def __init__(self, config=Config):
        BaseLoggingObj.__init__(self, config)
        YumInstaller.__init__(self)

    def writeConfig(self):
        f = open("/etc/my.cnf", 'w')
        f.write("[mysqld]")
        f.write("character-set-server=utf8")
        f.write("default-character-set=utf8")
        f.write("datadir=/var/lib/mysql")
        f.write("socket=/var/lib/mysql/mysql.sock")
        f.write("user=mysql")
        f.write("symbolic-links=0")
        f.write("[mysqld_safe]")
        f.write("character-set-server=utf8")
        f.write("log-error=/var/log/mysqld.log")
        f.write("pid-file=/var/run/mysqld/mysqld.pid")
        f.close()

    def what(self):
        return "mysql"