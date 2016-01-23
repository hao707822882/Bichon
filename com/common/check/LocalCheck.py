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
#  Time: 15:59
import commands
import httplib

__author__ = 'Administrator'


class LocalCheck(object):
    @staticmethod
    def psCheck(what):
        rt = commands.getstatusoutput("ps -ef | grep " + what.encode("utf-8"))
        rt_Array = rt[1].replace("\r\n", "\n").split("\n")
        return rt_Array

    @staticmethod
    def portCheck(port):
        rt = commands.getstatusoutput("netstat -anp | grep " + port)
        rt_Array = rt[1].replace("\r\n", "\n").split("\n")
        return rt_Array

    @staticmethod
    def httpCheck(host, port, resource="/"):
        conn = httplib.HTTPConnection(host.encode("utf-8"), int(port))
        req = conn.request('GET', resource.encode("utf-8"))
        response = conn.getresponse()
        if response.status in [200, 301]:
            return True
        else:
            return False



