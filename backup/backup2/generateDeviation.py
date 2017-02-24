#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 21:37:06 2017

@author: eowfenth
@version: 1.0.0

It shows deviations based in given points.

"""
# 0. Load the dependencies

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections, axes, transforms
import matplotlib as mpl
import netCDF4
from os import listdir
from datetime import datetime, timedelta
from mpl_toolkits.basemap import Basemap, cm
from matplotlib import ticker
import statistics as stats


# 0. Open the file and generate the variables

dataset = netCDF4.Dataset('../wrfout_d03_2016-12-13_00_00_00')

print(dataset.variables.keys())


#xlat = dataset.variables['XLAT'][:,:,:]# 10
#xlong = dataset.variables['XLONG'][:,:,:] # 12
#temp = dataset.variables['T2'][:,:,:]
#
#print("Highest Temperature:", np.amax(temp))
#print("Lowest Temperature:", np.amin(temp))
#
#print("Highest Latitude:", np.amax(xlat))
#hlat, llat = np.amax(xlat), np.amin(xlat)
#print("Lowest Latitude:",np.amin(xlat))
#print(hlat, llat)
#
#print("Highest Longitude:",np.amax(xlong))
#hlong, llong = np.amax(xlong), np.amin(xlong)
#print("Lowest Longitude:",np.amin(xlong))
#print(hlong, llong)
#
#print("Central Latitude:", dataset.CEN_LAT)
#print("Central Longitude:", dataset.CEN_LON)
#
#print("Start Date:", dataset.START_DATE)
#print("Simulation Start Date", dataset.SIMULATION_START_DATE)
#print("Julian Day:", dataset.JULDAY, "Julian Year:", dataset.JULYR)
#print("Map Projection:", dataset.MAP_PROJ_CHAR)
#
#temperature = []; lat = []; lon = []
#lon = xlong[:1, :,:].squeeze()
#lat = xlat[:1, :, :].squeeze()
#temperature = temp[:,:,:].squeeze()
#
#
#interestedValues = np.array([])
#
#meanLat = np.array([])
#meanLon = np.array([])
##for i in range(0, 97):
## 1. Get the list of coordenates
#
#plt.figure(figsize=(18, 9))
#m = Basemap(rsphere=(6378137.00,6356752.3142),\
#            resolution='h',area_thresh=0.1,projection='merc',\
##                llcrnrlon=-38.8517, llcrnrlat=-13.2526,
##                urcrnrlon=-38.1598, urcrnrlat=-12.6176)
#            llcrnrlon= llong, llcrnrlat= llat,
#            urcrnrlon= hlong, urcrnrlat= hlat)    
#
#m.drawcoastlines()
#x,y = m(lon, lat)
#ulons = xlong[:1, :,24:25].squeeze()[0]
#vlats = xlat[:1, 15:16, :].squeeze()[0]
###-38.5025 -13.0076
#meanLat = np.append(meanLat, [vlats])
#meanLon = np.append(meanLon, [ulons])
#u, v = m(ulons, vlats)
#m.plot(u, v, 'bo', markersize=4, color='white')
#
#ulons = xlong[:1, :,25:26].squeeze()[0]
#vlats = xlat[:1, 15:16, :].squeeze()[0]
###-38.5025 -13.0076
#meanLat = np.append(meanLat, [vlats])
#meanLon = np.append(meanLon, [ulons])
#u, v = m(ulons, vlats)
#m.plot(u, v, 'bo', markersize=4, color='white')
#
#ulons = xlong[:1, :,24:25].squeeze()[0]
#vlats = xlat[:1, 16:17, :].squeeze()[0]
###-38.5025 -13.0076
#meanLat = np.append(meanLat, [vlats])
#meanLon = np.append(meanLon, [ulons])
#u, v = m(ulons, vlats)
#m.plot(u, v, 'bo', markersize=4, color='white')
#
#ulons = xlong[:1, :,25:26].squeeze()[0]
#vlats = xlat[:1, 16:17, :].squeeze()[0]
###-38.5025 -13.0076
#meanLat = np.append(meanLat, [vlats])
#meanLon = np.append(meanLon, [ulons])
#u, v = m(ulons, vlats)
#m.plot(u, v, 'bo', markersize=4, color='white')
#
## 2. Get the mean value.
#
#print(np.mean(meanLat))
#print(np.mean(meanLon))
#
#u, v = m(np.mean(meanLon), np.mean(meanLat))
#m.plot(u, v, 'bo', markersize=4, color='k')
#plt.show()
## 3. Get the deviation. 
#
##np.std() #ddof = 1 (Mesmo valor do matlab)
#
## 4. Mark the value in the graph.
#
## 5. Redo over time.
# #   dataset.close()
#    
#tempo = [1,2,3,5,6,7,8,9,10]
#for index in range(97):
##    print(period[index])
##    print(currentDay[period[index]][0][0:1])
##    print(currentDay[period[index]][1][0:1])
##    choseTemperature = np.append(choseTemperature, currentDay[period[index]][1][0:1])
##   print(choseTemperature)
#    plt.figure()
#    plt.errorbar(tempo, meanLat,yerr=0.2)
#    #plt.plot(meanLat)
#    plt.ylabel('Temperature in Kelvin (K)')
#    plt.xlabel('Time in Hour (hh:mm:ss)')
#    #plt.xticks([0,1,2,3,4,5,6,7], 97, rotation = 'vertical')
#    plt.show()
#
#    
    
