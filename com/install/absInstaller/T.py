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
#  Date: 2016/1/5
#  Time: 17:01

from com.install.absInstaller.TarInstaller import TarInstaller

__author__ = 'Administrator'


class T(TarInstaller, object):
    def writeConfig(self, path):
        f = open(path, "w")


    def install(self):
        self.downloadTar()
        self.unTar()
        self.make()
        self.writeConfig()

    def make(self):
        print("make")

    def downloadTar(self):
        print("down")

    def unTar(self):
        print("untar")

    def __init__(self):
        TarInstaller.__init__(self)
