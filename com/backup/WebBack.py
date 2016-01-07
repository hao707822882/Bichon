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


class WebBack(BaseLoggingObj, AbsBacker, object):
    def back(self, savePath, parentPath, needBack):
        '''
            savePath:备份文件保存的路径
            parentPath:需要备份的父路径
            needBack:需要备份的父目录
        '''
        tr = ExecUtil.execCommand(" tar czvf " + savePath + " -C " + parentPath + " " + needBack)

    def __init__(self, config=Config):
        BaseLoggingObj.__init__(self, config=config)
        AbsBacker.__init__(self)
