# _*_ coding:utf-8 _*_
from web.broker.BrokerService import BrokerService
from com.Config import Config

__author__ = 'Administrator'


class NetService(object):
    def __init__(self):
        self.before = {}
        pass

    '''获取net详细信息'''

    def getNetInfo(self, hostKey):
        broker = BrokerService.getBroker(hostKey)
        return broker.getNetInfo()

    '''
    {
    "data": {
      "Loopback Pseudo-Interface 1": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "\u672c\u5730\u8fde\u63a5 2": [
        29258726,
        276679541,
        230171,
        275475,
        0,
        0,
        0,
        0
      ]
    },
    "time": 1453348072.861
  }
    '''

    def getOutSpeed(self, host, data):
        beforeData = self.before.get(host)
        nowTime = data["time"]
        nowData = {}
        self.before[host] = data
        if beforeData is not None:
            beforeTime = beforeData["time"]
            beforeData = beforeData["data"]
            for beforeKey in beforeData:
                if beforeKey.encode("utf-8") == Config.eht:
                    beforeData = beforeData[beforeKey]
                    break
        else:
            return 0

        data = data["data"]
        for nowKey in data:
            if nowKey.encode("utf-8") == Config.eht:
                nowData = data[beforeKey]
                break
        if nowData is not None:
            allUp = nowData[0] - beforeData[0]
            time = nowTime - beforeTime
            return allUp / 1024 / time
