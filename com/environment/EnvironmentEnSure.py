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
#  Time: 14:53
'''
    检测
'''

from com.common.BaseLoggingObj import BaseLoggingObj
from com.Config import Config
import os

__author__ = 'Administrator'


class EnvironmentUtil(BaseLoggingObj, object):
    def __init__(self, config=Config):
        BaseLoggingObj.__init__(self, config=config)
        self.logging.info("Environment check start")

    def dirCheck(self):
        needCheck = [Config.check_module_path, Config.install_module_path]
        autoCreate = [Config.softDownloadPath, Config.uploadTempDir]
        for path in needCheck:
            rt = os.path.exists(path)
            if not rt:
                raise NameError(path + "没有配置")

        for path in autoCreate:
            rt = os.path.exists(path)
            if not rt:
                os.makedirs(path)
