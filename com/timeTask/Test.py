# _*_ coding:utf-8 _*_
import signal

__author__ = 'Administrator'
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time
import os
from multiprocessing import Process

# coding=utf-8

def tick():
    print('Tick! The time is: %s' % datetime.now())


def tick1():
    print('Tick111111111! The time is: %s' % datetime.now())


class aa:
    task = []


scheduler = BackgroundScheduler()


def start(aa):
    scheduler.add_job(tick, 'cron', second='*/1', hour='*', id="xx")
    scheduler.start()


if __name__ == '__main__':

    start("")

    while True:
        try:
            time.sleep(5)
            print("xxx")
            scheduler.add_job(tick1, 'cron', second='*/1', hour='*')
            scheduler.remove_job("xx")
        except (KeyboardInterrupt, WindowsError):
            print("xxx")
