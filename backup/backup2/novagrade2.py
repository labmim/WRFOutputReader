#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:26:12 2016

@author: eowfenth
"""

#Nova Grade 2 Deslocada

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

dataset = netCDF4.Dataset('Files/wrfout_d02_2016-11-01.nc')

xlat = dataset.variables['XLAT'][:,:,:]# 10
xlong = dataset.variables['XLONG'][:,:,:] # 12

print(np.amax(xlat))
print(np.amin(xlat))

print(np.amax(xlong))
print(np.amin(xlong))
#print(dataset)

from mpl_toolkits.basemap import Basemap

# setup lambert conformal basemap.
# lat_1 is first standard parallel.
# lat_2 is second standard parallel (defaults to lat_1).
# lon_0,lat_0 is central point.
# rsphere=(6378137.00,6356752.3142) specifies WGS4 ellipsoid
# area_thresh=1000 means don't plot coastline features less
# than 1000 km^2 in area.
plt.figure(figsize=(18,9))
m = Basemap(#width=12000000,height=9000000,
            rsphere=(6378137.00,6356752.3142),\
            resolution='h',area_thresh=0.1,projection='merc',\
            llcrnrlon=-39.0917, llcrnrlat=-13.4526,
            urcrnrlon=-37.7282, urcrnrlat=-12.2176)
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-80.,81.,20.))
m.drawmeridians(np.arange(-180.,181.,20.))
m.drawmapboundary(fill_color='aqua')
# draw tissot's indicatrix to show distortion.
ax = plt.gca()
plt.title("Available Lat-Lons - Mercator Projection")

lons = xlong[:1, :,:].squeeze()
lats = xlat[:1, :, :].squeeze()
x,y = m(lons, lats)
m.plot(x, y, 'bo', markersize=3, color='white')
plt.savefig('nova-grade-2.png', bbox_inches='tight')
plt.show()
plt.close()

print("Central Latitude:", dataset.CEN_LAT)
print("Central Longitude:", dataset.CEN_LON)

dataset.close()

print(datetime.utcdate())