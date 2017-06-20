#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:42:23 2016

@author: eowfenth
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections, axes, transforms
import matplotlib as mpl
import netCDF4
from os import listdir
from datetime import datetime, timedelta
from mpl_toolkits.basemap import Basemap, cm
from matplotlib import ticker


dataset = netCDF4.Dataset('wrfout_d03_2016-12-13_00_00_00')

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

u10 = dataset.variables['U10'][:]
v10 = dataset.variables['V10'][:]


for i in range(0, 97):
    u = u10[i:i+1,:,:].squeeze()
    v = v10[i:i+1,:,:].squeeze()
    
    fig = plt.figure(figsize=(18,9))
    fig.suptitle('This is wind')
    m = Basemap(rsphere=(6378137.00,6356752.3142),\
                resolution='h',area_thresh=0.1,projection='merc',\
                llcrnrlon= llong, llcrnrlat= llat,
                urcrnrlon= hlong, urcrnrlat= hlat)    
    #m.fillcontinents(lake_color='aqua')
    #m.drawcoastlines()
    x,y = m(lon, lat)
    
    yy = np.arange(0, y.shape[0], 3)
    xx = np.arange(0, x.shape[1], 3)
    speed = np.sqrt(u*u + v*v)
    points = np.meshgrid(yy, xx) 
 
    m.contourf(x, y, np.sqrt(u*u + v*v), alpha = 0.4, cmap = 'Blues') 
    #m.barbs(x[points], y[points], u[points], v[points])
    cs = m.pcolormesh(x,y,np.squeeze(speed), alpha = 0.4, cmap = 'Blues')
    #plt.figure(1)
    #plt.grid(True)
#    m.colorbar()
    #cbar = m.colorbar(cmap = mpl.cm.cool, location='right', pad="5%")
    #cbar = m.colorbar(cs, location='right', pad="5%")
    #cmap = plt.get_cmap('jet_r')
    #cmap_r = reverse_colourmap(cmap)
    cNorm = mpl.colors.Normalize(vmin=0, vmax=12)
    cs.set_norm(cNorm)
    plt.colorbar(norm=cNorm, shrink=0.5)
    widths = np.linspace(0, 2, xx.size)
#    m.quiver(x[points], y[points], 
#    u[points], v[points], speed[points],
#    cmap=plt.cm.autumn)
    #Q = m.quiver(x, y, u, v, scale_units='xy', linewidths=widths)
        #cmap=plt.cm.gray, scale=700)
    Q = m.quiver(x[points], y[points], u[points], v[points], scale_units='xy', width= 0.004)
    qk = plt.quiverkey(Q, 1.03, 1.02, 1, r'$1 \frac{m}{s}$',
                   fontproperties={'weight': 'bold', 'size': 18}, labelpos='N')
    #m.plot(x, y, 'bo', markersize=1, color='black')
    #m.contourf(x, y, np.sqrt(u*u + v*v), alpha = 0.4) 
    m.drawcoastlines(color = '0.15')
    hora = i - 3
    plt.title("Velocidade do Vento a 10 metros " + (str(hora)) + ":00 Local", y=1.04)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    #plt.title("Wind - Hour " + str(i))
    
    plt.show()
    #plt.savefig('updated/test' + str(i) + '.png', bbox_inches='tight')
    plt.close()