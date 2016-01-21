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
#  Time: 11:35

import logging

__author__ = 'Administrator'


class Config(object):
    version = "1.0.0"
    logging_level = logging.DEBUG
    logging_file = "D:\\log.txt"
    agent_port = 8001
    check_module_path = "F:\\sourceReading\\Bichon\\com\\check\\agent\\module"  # 服务器检测模块
    install_module_path = "F:\\sourceReading\\Bichon\\com\\check\\agent\\module"  # 系统安装模块
    uploadTempDir = "F:\\sourceReading\\Bichon\\com\\check\\agent\\module"  # 文件上传目录（web）
    redisHost = "127.0.0.1"
    redisPort = "6379"
    softServer = "http://127.0.0.1/"  # 软件下载服务器地址
    softSavePath = "F:\\sourceReading\\Bichon\\com"  # 软件下载地址
    softInstallPath = "/usr/local"
    # 软件服务器列表
    soft_java = "jdk-8u45-linux-x64.gz"
    soft_maven = "maven-linux-x64.gz"
    soft_tomcat = "tomcat7.0.tar.gz"




    # 软件安装配置
    mysqlRoot = "B8S7nVEvTCv4zxRa"



    # 网卡名字
    eht = "eth1"
