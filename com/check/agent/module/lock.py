# --coding:utf-8--
# coding: utf-8
import thread

global mutex

mutex = thread.allocate_lock()


def lock(func):
    """装饰器, 用在func方法执行前后, 增加运行信息"""
    def wrapper(*argv):
        data = None
        mutex.acquire()
        data = func(*argv)
        mutex.release()
        return data
    return wrapper
