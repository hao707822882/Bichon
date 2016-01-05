#! /usr/bin/env python
# --coding:utf-8--
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
#  Date: 2016/1/5
#  Time: 12:11


__author__ = 'Administrator'

from abc import ABCMeta, abstractmethod
from com.Config import Config
import redis
import threading


class RedisListenAbs(object):
    __metaclass__ = ABCMeta

    def __init__(self, topic):
        self.redis = redis.Redis(host=Config.redisHost)
        self.ps = self.redis.pubsub()
        self.ps.subscribe(topic)
        self.initDoingThread()

    @abstractmethod
    def doing(self, data):
        pass

    def do(self, doing):
        for item in self.ps.listen():
            if item['type'] == 'message':
                doing(item['data'])

    def initDoingThread(self):
        worker = threading.Thread(target=self.do, args=(self.doing,))
        worker.setDaemon(True)
        worker.start()
