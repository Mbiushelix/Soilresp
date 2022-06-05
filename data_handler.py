# -*- coding: utf-8 -*-
"""
Created on Tue May 10 19:39:03 2022

@author: Yudhish
"""

def data_extract(file):
    time = []
    co2 = []
    temp = []
    rh = []
    
    with open(file) as f: 
        data = f.readlines()
        
    for line in data:
        line = line.strip()
        line = line.split(";")
        time.append(line[0])
        co2.append(line[1])
        temp.append(line[2])
        rh.append(line[3])
        
    return time, co2, temp, rh