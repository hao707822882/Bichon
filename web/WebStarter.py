#! /usr/bin/env python
# --coding:utf-8--
# coding: utf-8
# ━━━━━━神兽出没━━━━━━
#  　　 ┏┓　  ┏┓
#  　　┏┛┻━━━┛┻┓
#  　　┃　　　　　 ┃
#  　　┃　　　━　　┃
#  　　┃　┳┛　┗┳   ┃
#  　　┃　　　　　 ┃
#  　　┃　　　┻　　┃
#  　　┃　　　　　 ┃
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
#  Date: 2016/1/7
#  Time: 11:48


import json
from flask import Flask
from flask import abort, render_template, flash, app, jsonify, redirect, request
from web.dao.BichonDao import BichonDao
from web.service.CpuService import CpuService
from web.service.ExecService import ExecService
from web.service.ProcessService import ProcessService
from web.service.FileSystemService import FileSystemService
from web.service.MemService import MemService
from web.service.CheckService import CheckService
from web.service.NetService import NetService
from com.Config import Config
from web.service.task.TaskHelper import TaskHelper
from web.service.IptableService import IptableService
import socket


app = Flask(__name__)


@app.route('/')
def index():
    return redirect("/static/index.html#/disk")


'''server'''


@app.route('/server/getAll')
def getAllServer():
    server = dao.selectServer()[0]
    return jsonify(data=dao.selectServer()[0], pages=len(server))


'''service'''

# 获取当前服务器的所有服务
@app.route('/service/<int:serverId>')
def getAllService(serverId=1):
    services = dao.selectService(serverId)
    return jsonify(data=services[0], pages=len(services))


# 增添新服务
@app.route('/service/add')
def addService(serverId=1):
    serverId = request.values.get("serverId")
    execType = request.values.get("execType")
    execCommand = request.values.get("execCommand")
    host = request.values.get("host")
    port = request.values.get("port")
    url = request.values.get("url")
    lab = request.values.get("lab")
    services = dao.addService(serverId,execType,execCommand,host,port,url,lab)
    taskHelper.addTask(execType,serverId,port,host,lab,url)
    return jsonify(data=True)


# 增添新服务
@app.route('/service/dele/<int:serviceId>')
def delService(serviceId):
    dao.deleteServiceById(serviceId)
    return jsonify(data=True)


# 获取服务状态
@app.route('/service/statue')
def serviceStatue():
    serverId = request.values.get("serverId")
    data={}
    for (k, v) in CheckService.checkStatue.items():
        d=k.split(":")
        if d[0]==serverId:
            data[k]=v
    return jsonify(data=data)


'''file system'''


# 分区信息
@app.route('/fileSystem/partitonInfo')
def partitonInfo():
    '''获取host'''
    host = request.values.get("host")
    return disk.partitionInfo(host)


# 获取文件目录信息
@app.route('/fileSystem/pathInfo')
def pathInfo():
    host = request.values.get("host")
    path = request.values.get("path")
    return disk.ls(host, path)


'''mem'''


@app.route('/mem/memInfo')
# 内存总的使用率
def memInfo():
    host = request.values.get("host")
    data = json.loads(mem.getCpuStatue(host))
    return jsonify(data=data, error=False, msg="")


# 程序内存占用
def processMemInfo():
    request.values.get("host")
    request.values.get("path")
    return


'''net'''


@app.route('/net/netInfo')
# 网络信息
def netInfo():
    host = request.values.get("host").encode("utf-8")
    data = json.loads(net.getNetInfo(host))
    data = net.getOutSpeed(host, data)
    return jsonify(data=data, error=False, msg="")


'''CPU'''

# cpu总体信息
@app.route('/cpu/Info')
def cpuInfo():
    host = request.values.get("host")
    data = cpu.getCpuStatue(host)

    return jsonify(data=data, error=False, msg="")


# 程序占用cpu信息
def processCpuInfo():
    request.values.get("host")
    return


'''process'''


@app.route('/processes')
def processes():
    host = request.values.get("host")
    data = json.loads(process.getPids(host))
    return jsonify(data=data, error=False, msg="")


@app.route('/processes/detail')
def processesDetail():
    host = request.values.get("host")
    pid = request.values.get("pid")
    jsondata = json.loads(process.getProcessInfo(host, int(pid)))
    return jsonify(data=jsondata, error=False, msg="")


@app.route('/allProcesses/detail')
def allprocessesCustDetail():
    host = request.values.get("host")
    jsondata = json.loads(process.getCusProcessInfo(host))
    return jsonify(data=jsondata, error=False, msg="")


'''install管理'''

@app.route('/install/check')
def checkInstallStatue():
    host = request.values.get("host")
    data=check.checkSoftInstallStatus(host)
    return jsonify(data=data, error=False, msg="")


@app.route('/iptable/statue')
def iptableStatus():
    host = request.values.get("host")
    data=check.checkServiceRunning(host,"iptables")
    return jsonify(data=data, error=False, msg="")

@app.route('/iptable/list')
def iptableList():
    host = request.values.get("host")
    data=iptable.iptableList(host)
    return jsonify(data=data, error=False, msg="")

@app.route('/iptable/delete')
def iptableDelete():
    host = request.values.get("host")
    chain = request.values.get("chain")
    index = request.values.get("index")
    data=iptable.iptableDelete(host,chain,index)
    return jsonify(data=data, error=False, msg="")

@app.route('/iptable/add')
def iptableAdd():
    host = request.values.get("host")
    type = request.values.get("type")
    data = request.values.get("data")
    if type=="ip":
        rt=execService.runShell(host,"iptables -A INPUT -s "+data+" -p tcp -j DROP")
    else:
        rt=execService.runShell(host,"iptables -A INPUT -p tcp --dport "+data+" -j DROP")
    if rt[0]==0:
        return jsonify(error=False, msg="")
    else:
        return jsonify(error=True, msg="")


@app.route("/cmd")
def execCmd():
    host = request.values.get("host")
    cmd = request.values.get("cmd")
    d=execService.runShell(host,cmd)
    data={}
    data["msg"]=d[1]
    if d[0]==0:
        data["statue"]=True
    else:
        data["statue"]=False
    return jsonify(data=data, error=False, msg="")


if __name__ == '__main__':
    dao = BichonDao()
    cpu = CpuService()
    mem = MemService()
    disk = FileSystemService()
    process = ProcessService()
    check = CheckService()
    net = NetService()
    iptable=IptableService()
    execService=ExecService()
    taskHelper = TaskHelper()

    app.run(debug=True)
