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
#  Date: 2015/12/22
#  Time: 11:28


__author__ = 'Administrator'

from com.common.BaseLoggingObj import BaseLoggingObj
from com.Config import Config
from com.common.dymFun.Dym import DymUtil
from com.common.type.Type import Type


class BrokerProxy(BaseLoggingObj):
    def __init__(self, proxy, host, config=Config):
        BaseLoggingObj.__init__(self, config)
        self.target = proxy
        self.command = {}
        self.host = host
        self.isError = False
        self.export = {}
        self.__init()

    def __init(self):
        if self.target is not None:
            try:
                actionList = DymUtil.getattr(self.target, "list")()
                self.export.setdefault(self.host, actionList)
                if len(actionList) >= 1:
                    for action in actionList:
                        if type(action["items"]) is type(Type.array):
                            for func_item in action["items"]:
                                self.command.setdefault(func_item["function"],
                                                        DymUtil.getattr(self.target, func_item["function"]))
            except Exception, e:
                print(e)
                self.isError = True
                self.logging.error("Broker proxy init error ")

    def do(self, actionName):
        return self.command[actionName]()
