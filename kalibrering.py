# -*- coding: utf-8 -*-
"""
Created on Tue May 10 19:50:34 2022

@author: Yudhish
"""

# from data_handler import data_extract

# data_kal_1 = data_extract("kalibreringsdata_sensor1.txt")[1]
# data_kal_2 = data_extract("kalibreringsdata_sensor2.txt")[1]
# data_kal_1 = [float(x) for x in data_kal_1]
# data_kal_2 = [float(x) for x in data_kal_2]
# average1 = sum(data_kal_1)/len(data_kal_1)
# average2 = sum(data_kal_2)/len(data_kal_2)

# kf1 = 1000-average1
# kf2 = 1000-average2

# def kalib_num():
#     return kf1,kf2


def calibrate(data):
    time, co2, temp, rh = data
    co2_calibration_number =  1000 - float(co2[0])
    rh_calibration_number = 40 - float(rh[0])
    co2 = [float(value) + co2_calibration_number for value in co2]
    rh = [float(value) + rh_calibration_number for value in rh]
    temp = [float(value) for value in temp]
    return time, co2, temp, rh