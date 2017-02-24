#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 23:17:54 2016

@author: eowfenth
"""
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Read file
filename='target_day_20140422.dat'
f = open(filename, 'r')
contents = f.readlines()

forecast_dict = {}
for line in range(1, len(contents)):
    line_split = contents[line].split(' ')
    try:
        forecast_dict[line_split[0], line_split[1]][line_split[2]] = {'MaxT':float(line_split[3]),
                                                                      'MinT':float(line_split[4][:-1])}
    except:
        forecast_dict[line_split[0], line_split[1]] = {}
        forecast_dict[line_split[0], line_split[1]][line_split[2]] = {'MaxT':float(line_split[3]),
                                                                      'MinT':float(line_split[4][:-1])}
                                   
# Get keys of forecast_dict (lats and longs):
keys = forecast_dict.keys()
# Circle through all the keys to get the values for the 2nd day maximum temperature and the
# corresponding Lat and Longs
day_out = '3'       # 0-7
temp = 'MaxT'  # MaxT or MinT
temperature = []; lat = []; lon = []
for key in keys:
    temperature.append(float(forecast_dict[key][day_out][temp]))
    lat.append(float(key[0]))
    lon.append(float(key[1]))
# Now that those are collected, let's see what the Temperature as a function of Latitude is:
plt.scatter(temperature,lat)

m = Basemap(projection='merc',llcrnrlat=20,urcrnrlat=50,\
llcrnrlon=-130,urcrnrlon=-60,lat_ts=20,resolution='i')
m.drawcoastlines()
m.drawcountries()
# draw parallels and meridians.
parallels = np.arange(-90.,91.,5.)
# Label the meridians and parallels
m.drawparallels(parallels,labels=[True,False,False,False])
# Draw Meridians and Labels
meridians = np.arange(-180.,181.,10.)
m.drawmeridians(meridians,labels=[True,False,False,True])
m.drawmapboundary(fill_color='white')
plt.title("Forecast {0} days out".format(day_out))
# Define a colormap
jet = plt.cm.get_cmap('jet')
# Transform points into Map's projection
x,y = m(lon, lat)
# Color the transformed points!
sc = plt.scatter(x,y, c=temperature, vmin=0, vmax =35, cmap=jet, s=20, edgecolors='none')
# And let's include that colorbar
cbar = plt.colorbar(sc, shrink = .5)
cbar.set_label(temp)
plt.show()