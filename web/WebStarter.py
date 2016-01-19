#! /usr/bin/env python
# --coding:utf-8--
# coding: utf-8
# ━━━━━━神兽出没━━━━━━
#  　　　┏┓　　　┏┓
#  　　┏┛┻━━━┛┻┓
#  　　┃　　　　　　　┃
#  　　┃　　　━　　　┃
#  　　┃　┳┛　┗┳　┃
#  　　┃　　　　　　　┃
#  　　┃　　　┻　　　┃
#  　　┃　　　　　　　┃
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
from web.service.ProcessService import ProcessService
from web.service.FileSystemService import FileSystemService

app = Flask(__name__)

dao = BichonDao()
cpu = CpuService()
disk = FileSystemService()
process = ProcessService()


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
    services = dao.selectService(serverId)
    return jsonify(data=services[0], pages=len(services))


# 增添新服务
@app.route('/service/dele')
def delService(serverId=1):
    services = dao.selectService(serverId)
    return jsonify(data=services[0], pages=len(services))


# 获取服务状态
@app.route('/service/statue')
def serviceStatue(serverId=1):
    request.values.get("host")
    return


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

# 内存总的使用率
def memInfo():
    request.values.get("host")

    return


# 程序内存占用
def processMemInfo():
    request.values.get("host")
    request.values.get("path")
    return


'''net'''

# 网络信息
def netInfo():
    request.values.get("host")
    return


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
    data =  json.loads(process.getPids(host))
    return jsonify(data=data, error=False, msg="")


@app.route('/processes/detail')
def processesDetail():
    host = request.values.get("host")
    pid = request.values.get("pid")
    jsondata = json.loads(process.getProcessInfo(host, int(pid)))
    return jsonify(data=jsondata, error=False, msg="")


'''install管理'''


def install():
    whcihInstall = request.values.get("install")
    return


@app.route("/test")
def test():
    print
    print request.values.get("b")
    print request.values.get("a")


if __name__ == '__main__':
    app.run(debug=True)
