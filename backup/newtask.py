#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:10:55 2016

@author: eowfenth
"""

from matplotlib import collections, axes, transforms
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

import numpy as np
import netCDF4
from os import listdir
from datetime import datetime, timedelta

dataset = netCDF4.Dataset('Files/wrfout_d02_2016-11-01.nc')


print("Reading file...\n")

print("Central Latitude:", dataset.CEN_LAT)
print("Central Longitude:", dataset.CEN_LON)

print("Start Date:", dataset.START_DATE)
print("Simulation Start Date", dataset.SIMULATION_START_DATE)
print("Julian Day:", dataset.JULDAY, "Julian Year:", dataset.JULYR)
print("Map Projection:", dataset.MAP_PROJ_CHAR)

strDate = dataset.SIMULATION_START_DATE
currentYear = strDate[:4]
currentMonth = strDate[5:7]
currentDay = strDate[8:10]
currentHour = strDate[11:13]
currentMinute = strDate[14:16]
currentSeconds = strDate[17:]

times_array = dataset.variables['Times'][:]
date_array = np.array([])
i = 0
timeList = []
juliand = int(dataset.JULDAY)
for times in times_array:
    #print(times[:4])
    #print(times[5:7])
    #print(times[8:10])
    #print(times[11:])
    #print(type(b''.join(times.tolist()).decode('UTF-8')))
    currentTime = b''.join(times.tolist()).decode('UTF-8')
    print(currentTime)
    strDate = currentTime
    currentYear = strDate[:4]
    currentMonth = strDate[5:7]
    currentDay = strDate[8:10]
    currentHour = strDate[11:13]
    currentMinute = strDate[14:16]
    currentSeconds = strDate[17:]
    currentDay, currentMonth, currentYear
    #timeList.append([currentYear, currentMonth, currentDay, currentHour, currentMinute, currentSeconds])
    if (len(timeList) % 24 == 0):
        juliand += 1
        timeList.append([currentYear, currentMonth, currentDay, currentHour, currentMinute, currentSeconds, juliand])
        print(juliand)
    else:
        timeList.append([currentYear, currentMonth, currentDay, currentHour, currentMinute, currentSeconds, juliand])
        print(juliand)
    date_array = np.append(date_array, currentTime)

    np.savetxt('test.dat', timeList, fmt='%s')

#print(dataset)
dataset.close()