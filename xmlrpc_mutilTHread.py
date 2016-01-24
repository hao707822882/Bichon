#! /usr/bin/env python
# --coding:utf-8--
# coding: utf-8
# server.py -
#
#  Copyright (C) 2007 Leo Chen (hide1713@gmail.com)
#
# $Locker:  $
# $Log: header.el,v $Revision 1.1  2001/02/01 20:15:57  lasse
# Author          : Leo Chen
# Created On      : Sat Jun 16 10:10:28 2007
# Last Modified By: Leo Chen
# Last Modified On: Sat Jun 16 10:10:38 2007
# Update Count    : 1
#
# HISTORY
#
#-*- coding: cp936 -*-
import  SimpleXMLRPCServer,SocketServer
import time,thread

#The server object
class Server:
    count=0
    def __init__(self):
        pass

    def ServeMe(self):
        mutex.acquire() #用mutex锁住数据
        Server.count+=1 #更改静态数据
        t=time.strftime("Serve at %I:%M:%S Id is ")+str(Server.count)
        print "Serve Id "+str(Server.count)
        mutex.release()#释放锁
        time.sleep(10)

        return t
#多线程实现
class RPCThreading(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
    pass
global mutex
mutex =thread.allocate_lock()
server_object = Server()
server = RPCThreading(("localhost", 8888))
server.register_instance(server_object)

#Go into the main listener loop
print "Listening"

server.serve_forever()

#  -*- Python -*-
#
# client.py -
#
#  Copyright (C) 2007 Leo Chen (hide1713@gmail.com)
#
# $Locker:  $
# $Log: header.el,v $Revision 1.1  2001/02/01 20:15:57  lasse
# Author          : Leo Chen
# Created On      : Sat Jun 16 10:10:56 2007
# Last Modified By: Leo Chen
# Last Modified On: Sat Jun 16 10:10:57 2007
# Update Count    : 1
#
# HISTORY
#
import xmlrpclib

server = xmlrpclib.ServerProxy("http://localhost:8888")

id = server.ServeMe()
print id