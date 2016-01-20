# _*_ coding:utf-8 _*_
import random

__author__ = 'Administrator'
from apscheduler.schedulers.background import BackgroundScheduler

import time




class TimeScheduler(object):
    def __init__(self):
        self.tasks = {}
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    '''
        task是一个函数
    '''

    def addJob(self, name, id, task, second, hour, day_of_week):
        oldTask = self.tasks.get(id)
        if oldTask is None:
            self.tasks.setdefault(name, id)
            self.scheduler.add_job(task, 'cron', second=second, hour=hour, day_of_week=day_of_week, id=id)

    def clean(self):
        self.scheduler.remove_all_jobs()
