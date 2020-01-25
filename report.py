#!/usr/bin/env python3

import os 
import sys
import platform


def report_print(var):
    line="======="
    print(line*5)
    print(var)
    
def gen_data():
    tmp = []
    tmp.append(platform.platform())
    tmp.append(platform.dist())
    tmp.append(platform.node())
    tmp.append(platform.machine())
    return tmp
    

data = gen_data()

for i in data:
    report_print(i)