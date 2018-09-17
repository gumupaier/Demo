# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 下午11:34
# @Author  : Henson
# @Email   : henson_wu@foxmail.com
# @File    : helper.py
# @Software: PyCharm
__author__ = 'henson'

from uuid import uuid4
import time

def generate_id():
    return str(uuid4())

def get_time():
    return int(time.time())