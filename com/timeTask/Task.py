# _*_ coding:utf-8 _*_
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time
import os
from multiprocessing import Process

__author__ = 'Administrator'


class Task(object):
    def __init__(self, taskFunc,se):
        self.func = taskFunc

    def run(self):
        scheduler = BlockingScheduler()
        scheduler.add_job(self.func, 'cron', second='*/1', hour='*')
        scheduler.start()
