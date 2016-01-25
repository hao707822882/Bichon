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
        info=[]
        try:
            child = pexpect.spawnu('yum install mysql*'.decode("utf-8"))
            child.expect(['(?i)Is this ok [y/N]: '.decode("utf-8"), pexpect.EOF, pexpect.TIMEOUT])
            child.sendline('y')
            child.expect('Complete!')
            child.close()
            install=self.getInfo("yum install mysql*",True,"yum install mysql* ok")
            info.append(install)
        except Exception , e:
            install=self.getInfo("yum install mysql*",False,"yum install mysql* false")
            info.append(install)
            return info
        try:
            self.writeConfig()
            install=self.getInfo("write config",True,"write config ok")
            info.append(install)
        except Exception , e:
            install=self.getInfo("write config",False,"write config false")
            info.append(install)
            return info


        rt=ExecUtil.execCommand("service mysqld restart")
        if rt[0]==0:
            install=self.getInfo("service mysqld restart",True,rt[1])
            info.append(install)
        else:
            install=self.getInfo("service mysqld restart",False,rt[1])
            info.append(install)
            return info

        rt=ExecUtil.execCommand("mysqladmin -u root password " + Config.mysqlRoot)
        if rt[0]==0:
            install=self.getInfo("mysqladmin -u root password "+Config.mysqlRoot,True,rt[1])
            info.append(install)
        else:
            install=self.getInfo("mysqladmin -u root password "+Config.mysqlRoot,False,rt[1])
            info.append(install)
            return info

        rt=ExecUtil.execCommand("mysql -uroot -p" + Config.mysqlRoot + "-e select version()")
        if rt[0]==0:
            install=self.getInfo("mysql -uroot -p" + Config.mysqlRoot + "-e select version()",True,rt[1])
            info.append(install)
        else:
            install=self.getInfo("mysql -uroot -p" + Config.mysqlRoot + "-e select version()",False,rt[1])
            info.append(install)
            return info

        return info



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