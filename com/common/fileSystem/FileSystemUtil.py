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
#  Date: 2016/1/1
#  Time: 15:34


import os

__author__ = 'Administrator'


class FileSystemUtil(object):
    def __init__(self):
        pass

    @staticmethod
    def list(path):
        return os.listdir(path)

    @staticmethod
    def isDir(path):
        return os.path.isdir(path)

    @staticmethod
    def isFile(path):
        return os.path.isfile(path)

    @staticmethod
    def houZhui(path):
        return os.path.splitext(path)

    @staticmethod
    def isModuleFile(path):
        if os.path.isfile(path):
            if "py" == os.path.split(path):
                return True
            else:
                return False
        else:
            return False
