#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 12:17:49 2017

@author: Nícolas 'eowfenth' Deçordi dos Reis
@version: 1.0.0
@description:
    '''
    This script generate the images of wind from wrf output.
    '''
"""

# Depedencies

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections, axes, transforms
import matplotlib as mpl
import netCDF4
from os import listdir
from datetime import datetime, timedelta
from mpl_toolkits.basemap import Basemap, cm
from matplotlib import ticker

dataset = netCDF4.Dataset('../wrfout_d02_2016-10-14_00_00_00')

xlat = dataset.variables['XLAT'][:,:,:]# 10
xlong = dataset.variables['XLONG'][:,:,:] # 12
temp = dataset.variables['T2'][:,:,:]

print("Highest Temperature:", np.amax(temp))
print("Lowest Temperature:", np.amin(temp))

print("Highest Latitude:", np.amax(xlat))
hlat, llat = np.amax(xlat), np.amin(xlat)
print("Lowest Latitude:",np.amin(xlat))


print("Highest Longitude:",np.amax(xlong))
hlong, llong = np.amax(xlong), np.amin(xlong)
print("Lowest Longitude:",np.amin(xlong))

print("Central Latitude:", dataset.CEN_LAT)
print("Central Longitude:", dataset.CEN_LON)

print("Start Date:", dataset.START_DATE)
print("Simulation Start Date", dataset.SIMULATION_START_DATE)
print("Julian Day:", dataset.JULDAY, "Julian Year:", dataset.JULYR)
print("Map Projection:", dataset.MAP_PROJ_CHAR)

lat = []; lon = []
lon = xlong[:1, :,:].squeeze()
lat = xlat[:1, :, :].squeeze()