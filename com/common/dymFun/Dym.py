#! /usr/bin/env python
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
#  Date: 2015/12/21
#  Time: 11:40


__author__ = 'Administrator'

# !/usr/bin/python
# coding: UTF-8
"""
@author: CaiKnife

根据函数名称动态调用
"""


def do_foo():
    print "foo!"


def do_bar():
    print "bar!"


class Print():
    def do_foo(self):
        print "foo!"

    def do_bar(self):
        print "bar!"

    @staticmethod
    def static_foo():
        print "static foo!"

    @staticmethod
    def static_bar():
        print "static bar!"


def main():
    obj = Print()

    func_name = "do_foo"
    static_name = "static_foo"
    # eval(func_name)()
    # getattr(obj, func_name)()
    getattr(Print, static_name)()
    #
    # func_name = "do_bar"
    # static_name = "static_bar"
    # eval(func_name)()
    # getattr(obj, func_name)()
    # getattr(Print, static_name)()


if __name__ == '__main__':
    main()
