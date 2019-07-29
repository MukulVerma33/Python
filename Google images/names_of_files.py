# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:40:38 2019

@author: Mukul
"""

from os import listdir
from os.path import isfile, join
mypath = 'D:\wrkshp\Google images\downloads\Car'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)