from web.broker.BrokerService import BrokerService


class IptableService(object):
    def __init__(self):
        pass


    def iptableList(self,hostKey):
        broker = BrokerService.getBroker(hostKey)
        return broker.iptableList()

    def iptableDelete(self,hostKey,chain,index):
        broker = BrokerService.getBroker(hostKey)
        data=broker.execCmd("iptables -D "+chain+" "+index)
        if data[0]==0:
            return True
        else:
            return False
