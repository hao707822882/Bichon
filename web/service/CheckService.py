# _*_ coding:utf-8 _*_


from web.timer.Supervise import Supervise

__author__ = 'Administrator'


class CheckService(object):
    def __init__(self):
        pass

    def getCheckStatue(self, hostKey):
        return Supervise.getServiceStatue(hostKey)
