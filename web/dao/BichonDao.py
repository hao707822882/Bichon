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
    initDB = "CREATE DATABASE  IF NOT EXISTS bichon DEFAULT CHARACTER SET utf8"
    '''使用数据库'''
    useDB = "USE bichon"
    '''服务器表'''
    serverTB = "CREATE TABLE `server` (`id` INT(11) NOT NULL AUTO_INCREMENT,`host` VARCHAR(50) COLLATE utf8_bin NOT NULL COMMENT 'ip',`lab` VARCHAR(50) COLLATE utf8_bin NOT NULL COMMENT '标记服务器类别',PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin"
    '''每台服务器检测的服务'''
    serviceTB = "CREATE TABLE `service` (`id` INT(11) NOT NULL AUTO_INCREMENT,`execType` VARCHAR(30) COLLATE utf8_bin NOT NULL COMMENT '服务的检测类型',`execCommand` VARCHAR(200) COLLATE utf8_bin DEFAULT NULL COMMENT '执行命令需要的参数',`port` VARCHAR(10) COLLATE utf8_bin DEFAULT NULL COMMENT '端口',`host` VARCHAR(100) COLLATE utf8_bin DEFAULT NULL COMMENT 'url',`url` VARCHAR(100) COLLATE utf8_bin DEFAULT NULL COMMENT 'url',`serverId` INT(11) NOT NULL COMMENT '所属服务器ID',`lab` VARCHAR(30) NOT NULL COMMENT '描述',PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin"

    selectServerSql = "SELECT * FROM server"

    addServerSql = "INSERT INTO `server` (HOST,lab) VALUES('{0}','{1}')"

    deleteServerSql = "DELETE FROM service WHERE id={0}"

    addServiceSql = "INSERT INTO `service` (serverId,execType,execCommand,present) VALUES('{0}','{1}','{2}','{3}')"

    selectServiceSql = "SELECT * FROM service WHERE serverId={0}"

    selectServiceWithServerSql = "SELECT * FROM service,server WHERE service.serverId = server.id"

    deleteServiceSql = "DELETE FROM service WHERE id={0}"

    deleteServiceByServerIdSql = "DELETE FROM service WHERE serverId={0}"

    def __init__(self):
        BaseLoggingObj.__init__(self)
        self.sqlHelp = SqlHelper()
        self.logging.info("构建BichonDao")

    def init(self):
        self.sqlHelp.insert(BichonDao.initDB)
        self.sqlHelp.db = "bichon"
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

    def selectServiceWithServer(self):
        return self.sqlHelp.select(BichonDao.selectServiceWithServerSql)

    def deleteService(self, serviceId):
        sql = BichonDao.deleteServiceSql.format(serviceId)
        self.sqlHelp.delete(sql)

    def deleteAllService(self, serverId):
        sql = BichonDao.deleteServiceByServerIdSql.format(serverId)
        self.sqlHelp.delete(sql)
