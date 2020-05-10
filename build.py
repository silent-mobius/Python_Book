#!/usr/bin/env python3

########################################################################
#
#
#
#
########################################################################

import os
import os.path
import re
import sys
import subprocess
import datetime
from zipfile import ZipFile

try:
    import pypdf
except ImportError:
    print("[-] no python library: ")
    print('[+] Trying to install the library')
    os.system('pip3 install pypdf')
#folders = os.listdir()

def folder_list(path):
    folder_list=[]
    for file_ in path:
        if file_.startswith(('0','1','2','9')):
            folder_list.append(file_)
            
    return folder_list


def create_md_file(folders,dest_file):

    for folder in folders:
        os.chdir(folder)
        with open('README.md')


'''
for i in n:
     ...:     os.chdir(i)
     ...:     with open('README.md') as infile:
     ...:         d = infile.readlines()
     ...:         
     ...:     os.chdir('../')
     ...:     with open('tmp.txt','a') as nfile:
     ...:          nfile.writelines(d)
'''