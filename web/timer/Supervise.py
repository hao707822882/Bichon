# _*_ coding:utf-8 _*_

from com.timeTask.TimeScheduler import TimeScheduler
from web.dao.BichonDao import BichonDao

__author__ = 'Administrator'


class Supervise(object):
    hostServicesMap = {}
    hostServiceStatue = {}
    '''
       （1）全局共享变量--记录各个服务的检测状态，结构{"host":[{serviceName:状态},{serviceName:状态}]}
       （1）获取当前主机的服务列表
       （2）创建对应的task并添加到task中
    '''

    def __init__(self):
        self.dao = BichonDao()
        self.taskScheduler = TimeScheduler()
        servers = self.dao.selectServer()
        for server in servers:
            service = self.dao.selectService(server.id)
            Supervise.hostServicesMap.setdefault(server.host, service)
        self.initScheduler()

    '''之后实现'''

    def initScheduler(self):
        pass

    '''获取服务的检测状态'''

    @staticmethod
    def getServiceStatue(hostKey):
        return Supervise.hostServiceStatue.get(hostKey)
