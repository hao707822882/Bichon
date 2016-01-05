# _*_ coding:utf-8 _*_

from com.common.execCommand.ExecUtil import ExecUtil

__author__ = 'Administrator'


class IptablesSecurity(object):
    def __init__(self):
        pass

    def initIptable(self):
        self.dropAll()

    def dropAll(self):
        ExecUtil.execCommandList(
            ["iptables -P INPUT DROP", "iptables -P FORWARD DROP", "iptables -P OUTPUT DROP", "service iptables save "])

    def openDefault(self):
        re = []
        re.append(self.openSSH())
        re.append(self.openWeb())
        return re

    def openSSH(self):
        return ExecUtil.execCommandList(["iptables -A INPUT -p tcp --dport 22 -j ACCEPT",
                                         "iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT"])

    def openWeb(self):
        return ExecUtil.execCommandList(["iptables -A INPUT -p tcp --dport 80 -j ACCEPT",
                                         "iptables -A OUTPUT -p tcp --sport 80 -j ACCEPT"])

    def openByPort(self, port):
        return ExecUtil.execCommandList(["iptables -A INPUT -p tcp --dport " + port + " -j ACCEPT",
                                         "iptables -A OUTPUT -p tcp --sport " + port + " -j ACCEPT"])

    def limitIp(self, ip, port):
        return ExecUtil.execCommandList(["iptables -A INPUT -s " + ip + " -p tcp --dport " + port + " -j DROP"])
