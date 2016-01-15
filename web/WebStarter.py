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


from flask import Flask
from flask import abort, render_template, flash, app, jsonify, redirect
from web.dao.BichonDao import BichonDao

# dao = BichonDao()
app = Flask(__name__)


@app.route('/')
def index():
    return redirect("/static/index.html#/disk")


@app.route('/server/getAll')
def getAllServer():
    server = dao.selectServer()[0]
    return jsonify(data=dao.selectServer()[0], pages=len(server))


@app.route('/service/<int:serverId>')
def getAllService(serverId=1):
    services = dao.selectService(serverId)
    return jsonify(data=services[0], pages=len(services))


if __name__ == '__main__':
    app.run(debug=True)
