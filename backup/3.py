#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 20:22:08 2016

@author: eowfenth
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:10:55 2016

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
import matplotlib as mpl

dataset = netCDF4.Dataset('Files/wrfout_d01_2016-10-06_00_00_00')

xlat = dataset.variables['XLAT'][:,:,:]# 10
xlong = dataset.variables['XLONG'][:,:,:] # 12
temp = dataset.variables['Q2'][:,:,:]
ust = dataset.variables['RAINC'][:,:,:]
variable = "T2"
var = dataset.variables[variable][:,:,:].squeeze()
print("Highest Temperature:", np.amax(temp))
print("Lowest Temperature:", np.amin(temp))

print("Highest Latitude:", np.amax(xlat))
hlat, llat = np.amax(xlat), np.amin(xlat)
print("Lowest Latitude:",np.amin(xlat))
print(hlat, llat)

print("Highest Longitude:",np.amax(xlong))
hlong, llong = np.amax(xlong), np.amin(xlong)
print("Lowest Longitude:",np.amin(xlong))
print(hlong, llong)

print("Central Latitude:", dataset.CEN_LAT)
print("Central Longitude:", dataset.CEN_LON)

print("Start Date:", dataset.START_DATE)
print("Simulation Start Date", dataset.SIMULATION_START_DATE)
print("Julian Day:", dataset.JULDAY, "Julian Year:", dataset.JULYR)
print("Map Projection:", dataset.MAP_PROJ_CHAR)

temperature = []; lat = []; lon = []
lon = xlong[:1, :,:].squeeze()
lat = xlat[:1, :, :].squeeze()
temperature = temp[:,:,:].squeeze()


#


#plt.figure(figsize=(18,9))
#m = Basemap(rsphere=(6378137.00,6356752.3142),\
#            resolution='h',area_thresh=0.1,projection='merc',\
#            llcrnrlon=-38.8517, llcrnrlat=-13.2526,
#            urcrnrlon=-38.1598, urcrnrlat=-12.6176)
#
#m.drawcoastlines()
#m.fillcontinents(color='coral',lake_color='aqua')
## draw parallels and meridians.
#m.drawparallels(np.arange(-80.,81.,20.))
#m.drawmeridians(np.arange(-180.,181.,20.))
#m.drawmapboundary(fill_color='aqua')
## draw tissot's indicatrix to show distortion.
#ax = plt.gca()
#plt.title("Available Lat-Lons - Mercator Projection")


#x,y = m(lon, lat)
#m.plot(x, y, 'bo', markersize=1, color='black')

#cs = m.pcolor(x,y,np.squeeze(temperature), vmin=20, vmax=30)
#cbar = m.colorbar(cs, location='right')

lab = "LabMiM/LMAC (UFBA)"
model = "WRF V3"
analysis = dataset.START_DATE
forecast = "11/01/2017 (Quarta-feira) Horário: 8HL"
title = model + " — " + lab + "\n" + analysis + "\n" + forecast
for i in range(0, 97):
    plt.figure(figsize=(18,9))
    m = Basemap( #rsphere=(6378137.00,6356752.3142),\
                resolution='h',area_thresh=0.1,projection='merc',\
#                llcrnrlon=-38.8517, llcrnrlat=-13.2526,
#                urcrnrlon=-38.1598, urcrnrlat=-12.6176)
                llcrnrlon= llong, llcrnrlat= llat,
                urcrnrlon= hlong, urcrnrlat= hlat)    
    #m.fillcontinents(lake_color='aqua')
    m.drawcoastlines()
    x,y = m(lon, lat)
    #m.plot(x, y, 'bo', markersize=1, color='black')
    fix = var[i:i+1,:,:]
    m.contourf(x, y, np.squeeze(fix), alpha = 0.4, cmap = 'jet')
    cs = m.pcolor(x,y,np.squeeze(fix), alpha = 0.4,cmap = 'jet')#, vmin=(291 - 273.15), vmax=(304  - 273.15))
    cbar = m.colorbar(cs, location='right')
    #plt.title("Umidade - Hora " + str(i - 3) + "h00 Local")
    plt.suptitle(title, fontsize = 12, ha = 'left', x = 0.3)
    #plt.suptitle("HOOO", fontsize = 10)
    
#    ulons = xlong[:1, :,24:25].squeeze()[0]
#    vlats = xlat[:1, 14:15, :].squeeze()[0]
#    ##-38.5025 -13.0076
#    u, v = m(ulons, vlats)
#    m.plot(u, v, 'bo', markersize=4, color='white')
#    
#    ulons = xlong[:1, :,25:26].squeeze()[0]
#    vlats = xlat[:1, 14:15, :].squeeze()[0]
#    ##-38.5025 -13.0076
#    u, v = m(ulons, vlats)
#    m.plot(u, v, 'bo', markersize=4, color='white')
    
#    ulons = xlong[:1, :,24:25].squeeze()[0]
#    vlats = xlat[:1, 16:17, :].squeeze()[0]
#    ##-38.5025 -13.0076
#    u, v = m(ulons, vlats)
#    m.plot(u, v, 'bo', markersize=4, color='white')
    
    ulons = xlong[:1, :,25:26].squeeze()[0]
    vlats = xlat[:1, 15:16, :].squeeze()[0]
    ##-38.5025 -13.0076
    u, v = m(ulons, vlats)
    m.plot(u, v, 'bo', markersize=4, color='white')
    
#    ulons = xlong[:1, :,24:25].squeeze()[0]
#    vlats = xlat[:1, 14:15, :].squeeze()[0]
#    ##-38.5025 -13.0076
#    u, v = m(ulons, vlats)
#    m.plot(u, v, 'bo', markersize=4, color='white')
#    
#    ulons = xlong[:1, :,25:26].squeeze()[0]
#    vlats = xlat[:1, 14:15, :].squeeze()[0]
    ##-38.5025 -13.0076
    u, v = m(ulons, vlats)
    m.plot(u, v, 'bo', markersize=4, color='white')
    plt.show()
    #plt.savefig('temperatura/figdia-hour-' + str(i) + '.png', bbox_inches='tight')
    plt.close()

#plt.savefig('grade3-merc.png', bbox_inches='tight')
plt.show()
plt.close()

#plt.figure(figsize=(18,9))
#m = Basemap(width=70000,height=70000,
#            rsphere=(6378137.00,6356752.3142),\
#            resolution='h',area_thresh=0.1,projection='lcc',\
#            lat_1=-12.6176,lat_2=-13.2526,lat_0=-12.9132,lon_0=-38.5071)
#m.drawcoastlines()
#m.fillcontinents(color='coral',lake_color='aqua')
## draw parallels and meridians.
#m.drawparallels(np.arange(-80.,81.,20.))
#m.drawmeridians(np.arange(-180.,181.,20.))
#m.drawmapboundary(fill_color='aqua')
## draw tissot's indicatrix to show distortion.
#ax = plt.gca()
#plt.title("Available Lat-Lons - Lambert Conformal Projection")
#lons = xlong[:1, :,:].squeeze()
#lats = xlat[:1, :, :].squeeze()
#x,y = m(lons, lats)
#m.plot(x, y, 'bo', markersize=1, color='white')
#u,v = m(-38.5093, -13.0059)
#m.plot(u, v, 'bo', markersize=4, color='red') # 25, 15
#ulons = xlong[:1, :,25:26].squeeze()[0]
#vlats = xlat[:1, 14:15, :].squeeze()[0]
##-38.5025 -13.0076
#u, v = m(ulons, vlats)
#m.plot(u, v, 'bo', markersize=4, color='white')
#ulons = xlong[:1, :,24:25].squeeze()[0]
#vlats = xlat[:1, 14:15, :].squeeze()[0]
##-38.5025 -13.0076
#u, v = m(ulons, vlats)
#m.plot(u, v, 'bo', markersize=4, color='white')
#ulons = xlong[:1, :,25:26].squeeze()[0]
#vlats = xlat[:1, 15:16, :].squeeze()[0]
##-38.5025 -13.0076
#u, v = m(ulons, vlats)
#m.plot(u, v, 'bo', markersize=4, color='white')
#plt.savefig('grade3-lcc.png', bbox_inches='tight')
#plt.show()
#plt.close()

#
##
#
#
#
#
dataset.close()