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
#  Time: 18:02

from com.common.BaseLoggingObj import BaseLoggingObj
from com.install.installer.AbsInstaller import AbsInstaller
from com.Config import Config

__author__ = 'Administrator'


class TomcatInstaller(BaseLoggingObj, AbsInstaller, object):
    def install(self):
        print("��װjava")

    def __init__(self, config=Config):
        BaseLoggingObj.__init__(self, config)
        AbsInstaller.__init__(self)
