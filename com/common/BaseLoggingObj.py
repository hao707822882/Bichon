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
#  Time: 13:48


__author__ = 'Administrator'
import logging
from com.Config import Config


def logger(func):
    """装饰器, 用在func方法执行前后, 增加运行信息"""

    def wrapper(*argv):
        data = None
        if argv.__sizeof__ > 0:
            if argv[0].logging != None:
                logging.info("call function  %s input param %s", func.__name__, argv)
                data = func(*argv)
                logging.info("call function  %s input return %s", func.__name__, data)
        return data

    return wrapper


class BaseLoggingObj(object):
    '''
        config的默认参数是com.Config 可通过构造修改
    '''

    def __init__(self, config=Config):
        logging.basicConfig(level=config.logging_level,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=config.logging_file,
                            filemode='a')
        self.logging = logging
