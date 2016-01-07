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
#  Time: 14:01

import commands

__author__ = 'Administrator'


class ExecUtil(object):
    @staticmethod
    def execCommandList(commandList):
        result = []
        for comm in commandList:
            rt = ExecUtil.execCommand(comm)
            if rt[0] is 0:
                result.append(rt)
            else:
                result.append(rt)
                break
        return result

    @staticmethod
    def execCommand(command):
        return commands.getstatusoutput(command)
