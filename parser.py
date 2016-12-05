#!/usr/bin/env python
# -*-coding:utf-8 -*-
import time

TIMEFORMAT='%Y-%m-%d %X'
def parse(input):
    if input == "what's the time":
        return time.strftime(TIMEFORMAT,time.localtime())
    elif input == "where are you":
        return "meituan"
    else:
        return input

