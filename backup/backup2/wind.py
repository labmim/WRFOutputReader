#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:14:05 2016

@author: eowfenth
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections, axes, transforms
import netCDF4
from os import listdir
from datetime import datetime, timedelta
from mpl_toolkits.basemap import Basemap
from matplotlib import ticker


dataset = netCDF4.Dataset('Files/wrfout_d03_2016-11-24_00_00_00.nc')

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


#m=Basemap(projection='cyl',llcrnrlat=30,urcrnrlat=80, llcrnrlon=-40,urcrnrlon=40,resolution='c')
plt.figure(figsize=(18,9))
m = Basemap(rsphere=(6378137.00,6356752.3142),\
            resolution='h',area_thresh=0.1,projection='merc',\
#                llcrnrlon=-38.8517, llcrnrlat=-13.2526,
#                urcrnrlon=-38.1598, urcrnrlat=-12.6176)
            llcrnrlon= llong, llcrnrlat= llat,
            urcrnrlon= hlong, urcrnrlat= hlat)
lons,lats = np.meshgrid(lon,lat)
X4,Y4= m(lon,lat)

u10 = dataset.variables['U10'][:]
v10 = dataset.variables['V10'][:]

varU=u10[0,:,:]
varV=v10[0,:,:]

speed=np.sqrt(varU*varU+varV*varV)

yy=np.arange(0,len(lat),3)
xx=np.arange(0,len(lon),3)

points=np.meshgrid(yy,xx)

m.quiver(X4[points],Y4[points],varU[points],varV[points],speed[points],cmap='jet',latlon=True)
plt.show()

# with all points for comparison
m.quiver(X4,Y4,varU,varV,speed,cmap='jet',latlon=True)
plt.show()