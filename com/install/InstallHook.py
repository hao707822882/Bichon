#! /usr/bin/env python
# --coding:utf-8--
# coding: utf-8
# ���������������޳�û������������
#  ��������������������
#  ���������ߩ��������ߩ�
#  ����������������������
#  ����������������������
#  ���������ש������ס���
#  ����������������������
#  �������������ߡ�������
#  ����������������������
#  ����������������������
#  ���������������������ޱ���, ����BUG!
#  ������������������Code is far away from bug with the animal protecting
#  ��������������������������
#  �������������������������ǩ�
#  ����������������������������
#  �������������������ש�����
#  �������������ϩϡ����ϩ�
#  �������������ߩ������ߩ�
#  �������������о������թ�����������
#  Module Desc:clover
#  User: z.mm | 2428922347@qq.com
#  Date: 2016/1/4
#  Time: 17:45
from com.common.BaseLoggingObj import BaseLoggingObj
from com.common.moduleScanner.ModuleScanner import ModuleScanner
from com.Config import Config

'''
    ����hook���еİ�װ����
'''
__author__ = 'Administrator'


class InstallHooker(BaseLoggingObj, object):
    installMap = {}

    def __init__(self, config=Config):
        BaseLoggingObj.__init__(self, config=config)
        self.logging.info("add InstallHooker module!")
        self.config = config
        self.module = {}

    def findInstallModuleAndInstall(self, name, version):
        ModuleScanner().scan()

    def initModule(self):
        ms = ModuleScanner();
        self.module = ms.scan(self.config.install_module_path)
