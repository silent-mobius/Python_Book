#!/usr/bin/env python3

########################################################################
#
#
#
#
########################################################################

import os
import sys
import datetime
from zipfile import ZipFile

today = datetime.date.today()


def get_all_files_into_zip(dirs):

    paths=[]



    for root, directories, files  in os.walk(dirs)