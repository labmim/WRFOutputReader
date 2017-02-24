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

dataset = netCDF4.Dataset('Files/wrfout_d03_2016-11-24_00_00_00.nc')

# Temperature -
temperature = dataset.variables['T2']
#print("Temperature dimensions", temperature.dimensions)
#print("Temperature units:", temperature.units)
temperature_array = temperature[:]#.squeeze()

# Height - 
height = dataset.variables['HGT']
#print("Height dimensions", height.dimensions)
#print("Height units:", height.units)
height_array = height[:].squeeze()

times_array = dataset.variables['Times'][:]

date_array = np.array([])
for times in times_array:
    #print(times[:4])
    #print(times[5:7])
    #print(times[8:10])
    #print(times[11:])
    #print(type(b''.join(times.tolist()).decode('UTF-8')))
    currentTime = b''.join(times.tolist()).decode('UTF-8')
    date_array = np.append(date_array, currentTime)
    
print(dataset.variables.keys())
print(dataset.variables['HGT'])

#for slice in temperature_array:
#    sliced_temperature = np.append(sliced_temperature, slice[11:12,11:12])
#for slice in height_array[:]:
#    sliced_height = np.append(sliced_height, slice[11:12, 11:12])
print("Gathering data...")
print("-----")
sliced_temperature = np.array([])
sliced_height = np.array([])

day = {}
f1 = np.loadtxt('testet.dat')
print(f1)

sLat = 25
sLong = 14
sHour = 0

for hour in range(len(date_array)):
#    print(date_array[hour])
#    print(date_array[hour][:4])
#    print(date_array[hour][5:7])
#    print(date_array[hour][8:10])
#    print(date_array[hour][11:])
    #print("Reading from day", date_array[hour][0:10])
    #print("Moment:", date_array[hour][11:])
    sHour = hour
    for slice in temperature_array[hour: hour + 1,:,:]:
        sliced_temperature = np.append(sliced_temperature, slice[sLat:sLat+1, sLong:sLong+1])
    #for slice in height_array[hour: hour + 1,:,:]:
    #    sliced_height = np.append(sliced_height, slice[11:12, 11:12])
    

    if ((hour + 1) % 24 == 0):
        print("")
        print("Completing day", (hour + 1) // 24 )
        day[((hour + 1) // 24)] = sliced_temperature


    if (hour == len(date_array) - 1):
        
        print("Completing period from", date_array[0][0:10], "to", date_array[-1][0:10])
        print("-----")
        print("Plotting period...")
        limits = [0, 23]
        for d in day:
            plt.title('Temperature at 2 meters over day ' + str(d))
            plt.ylabel('Temperature in Celcius (C)')
            plt.xlabel('Time in Hour')
            plt.xlim(limits)
            plt.ylim([21,30])
            plt.plot(day[d] - 273.15)
            plt.savefig('day' + str(d) + '.png', bbox_inches='tight')
            plt.hold(True)
            plt.plot(f1, '--', color = 'm')
            plt.savefig('day' + str(d) + '-2.png', bbox_inches='tight')
            plt.show()
            plt.close()
            limits[0] += 24
            limits[1] += 24
        plt.title('Temperature at 2 meters over period')
        plt.ylabel('Temperature in Celcius (C)')
        plt.xlabel('Time in Hour')
        plt.xlim([0,96])
        plt.ylim([21,30])        
        plt.plot(day[d] - 273.15)
        plt.savefig('period.png', bbox_inches='tight')
        #plt.show()
        #plt.close()
        #plt.hold(True)
        #plt.plot(f1, '--', color = 'm')
        plt.savefig('period2.png', bbox_inches='tight')
        plt.show()
        plt.close()
        
#xlat = dataset.variables['XLAT'][:,:,:]# 10
#xlong = dataset.variables['XLONG'][:,:,:] # 12

#print(np.amax(xlat))
#print(np.amin(xlat))
#
#print(np.amax(xlong))
#print(np.amin(xlong))
#print(dataset)

#from mpl_toolkits.basemap import Basemap
#
## setup lambert conformal basemap.
## lat_1 is first standard parallel.
## lat_2 is second standard parallel (defaults to lat_1).
## lon_0,lat_0 is central point.
## rsphere=(6378137.00,6356752.3142) specifies WGS4 ellipsoid
## area_thresh=1000 means don't plot coastline features less
## than 1000 km^2 in area.
#plt.figure(figsize=(18,9))
#m = Basemap(#width=12000000,height=9000000,
#            rsphere=(6378137.00,6356752.3142),\
#            resolution='h',area_thresh=0.1,projection='merc',\
#            llcrnrlon=-39.3117, llcrnrlat=-13.6526,
#            urcrnrlon=-37.8082, urcrnrlat=-12.2176)
#m.drawcoastlines()
#m.fillcontinents(color='coral',lake_color='aqua')
## draw parallels and meridians.
#m.drawparallels(np.arange(-80.,81.,20.))
#m.drawmeridians(np.arange(-180.,181.,20.))
#m.drawmapboundary(fill_color='aqua')
## draw tissot's indicatrix to show distortion.
#ax = plt.gca()
#plt.title("Available Lat-Lons - Mercator Projection")
#
##lon1 = -38.537
##lat1 = -13.012
##lons = [lon1, -38.491, -38.491]
##lats = [lat1, -13.012, -12.958]
#
#lons = xlong[:1, :,:].squeeze()
#lats = xlat[:1, :, :].squeeze()
#x,y = m(lons, lats)
#m.plot(x, y, 'bo', markersize=3, color='white')
#plt.savefig('lat-lons-grade-1.png', bbox_inches='tight')
#plt.show()
#plt.close()

dataset.close()

print(datetime.today().hour)