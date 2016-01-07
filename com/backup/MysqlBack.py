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
from com.Config import Config

from com.common.BaseLoggingObj import BaseLoggingObj
from com.common.execCommand.ExecUtil import ExecUtil
from com.backup.AbsBacker import AbsBacker

__author__ = 'Administrator'


class MySqlBack(BaseLoggingObj, AbsBacker, object):
    def back(self, user, pwd, db, savePath):
        ExecUtil.execCommand(
            " mysqldump -u" + user + " -p" + pwd + " -B --skip-lock-tables  " + db + " |gzip  > " + savePath + "/" + db + "`/bin/date +%F`.back.gz")

    def __init__(self, config=Config):
        BaseLoggingObj.__init__(self, config=config)
        AbsBacker.__init__(self)
