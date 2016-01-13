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
from flask import abort, render_template, flash, app, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("/static/index.html", items=["xxx", "xxx"])


@app.route('/all/getall')
def hello_world1():
    b = [{"value": 335, "name": ""}, {"value": 310, "name": "xxx"}, {"value": 234, "name": "xxxx"},
         {"value": 135, "name": "xxxxx"}, {"value": 1548, "name": "xxxxxx"}]
    return jsonify(result=b)


if __name__ == '__main__':
    app.run(debug=True)
