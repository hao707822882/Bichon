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
#  Date: 2015/12/21
#  Time: 18:19

from com.common.agent.AbsAgent import Agent
from com.common.BaseLoggingObj import BaseLoggingObj

__author__ = 'Administrator'


class DefaultAgent(Agent, BaseLoggingObj):
    def list(self):
        return ["cpu", "net"]

    def __init__(self):
        self.logging.info("init DefaultAgent from file %s", __file__);

    def cpu(self):
        return {"cores", [{"sys": "0.1", "us": "30"}, {"sys": "0.1", "us": "30"}, {"sys": "0.1", "us": "30"},
                          {"sys": "0.1", "us": "30"}]}

    def net(self):
        return {"eth", [{"in": "100k", "out": "500"}, {"in": "100k", "out": "500"}, {"in": "100k", "out": "500"},
                        {"in": "100k", "out": "500"}]}
