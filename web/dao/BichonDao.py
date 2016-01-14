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
#  Date: 2016/1/14
#  Time: 15:03

from com.mysql.helper.SqlHelper import SqlHelper
from com.common.BaseLoggingObj import BaseLoggingObj

__author__ = 'Administrator'


class BichonDao(BaseLoggingObj, object):
    '''创建数据库'''
    initDB = "CREATE DATABASE  IF NOT EXISTS Bichon DEFAULT CHARACTER SET utf8"
    '''使用数据库'''
    useDB = "USE Bichon"
    '''服务器表'''
    serverTB = "CREATE TABLE `server` (`id` int(11) NOT NULL AUTO_INCREMENT,`host` varchar(50) COLLATE utf8_bin NOT NULL COMMENT 'ip',`lab` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '标记服务器类别',PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin"
    '''每台服务器检测的服务'''
    serviceTB = "CREATE TABLE `service` (`id` int(11) NOT NULL AUTO_INCREMENT,`execType` varchar(30) COLLATE utf8_bin NOT NULL COMMENT '服务的检测类型',`execCommand` varchar(200) COLLATE utf8_bin DEFAULT NULL COMMENT '执行命令需要的参数',`serverId` int(11) NOT NULL COMMENT '所属服务器ID',PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin"

    selectServerSql = "SELECT * FROM SERVER"

    addServerSql = "INSERT INTO `server` (HOST,lab) VALUES('{0}','{1}')"

    deleteServerSql = "DELETE FROM SERVER WHERE id={0}"

    addServiceSql = "INSERT INTO `service` (serverId,execType,execCommand,present) VALUES('{0}','{1}','{2}','{3}')"

    selectServiceSql = "SELECT * FROM service WHERE serverId={0}"

    deleteServiceSql = "DELETE FROM service WHERE id={0}"

    deleteServiceByServerIdSql = "DELETE FROM service WHERE serverId={0}"

    def __init__(self):
        BaseLoggingObj.__init__(self)
        self.sqlHelp = SqlHelper()
        self.logging.info("构建BichonDao")

    def init(self):
        self.sqlHelp.insert(BichonDao.initDB)
        self.sqlHelp.db = "Bichon"
        self.sqlHelp.insert(BichonDao.serverTB)
        self.sqlHelp.insert(BichonDao.serviceTB)

    def selectServer(self):
        return self.sqlHelp.select(BichonDao.selectServerSql)

    def addServer(self, host, lab):
        sql = BichonDao.addServerSql.format(host, lab)
        self.sqlHelp.insert(sql)

    def deleteServerById(self, id):
        sql = BichonDao.deleteServerSql.format(id)
        self.sqlHelp.delete(sql)

    def addService(self, serverId, execType, execCommand, addServiceSql):
        sql = BichonDao.addServiceSql.format(serverId, execType, execCommand, addServiceSql)
        self.sqlHelp.insert(sql)

    def selectService(self, serverId):
        sql = BichonDao.selectServiceSql.format(serverId)
        return self.sqlHelp.select(sql)

    def deleteService(self, serviceId):
        sql = BichonDao.deleteServiceSql.format(serviceId)
        self.sqlHelp.delete(sql)

    def deleteAllService(self, serverId):
        sql = BichonDao.deleteServiceByServerIdSql.format(serverId)
        self.sqlHelp.delete(sql)

