# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 13:14:25 2016

@author: eowfenth
"""

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
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
            urcrnrlon=-38.0282, urcrnrlat=-12.4176)
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-80.,81.,20.))
m.drawmeridians(np.arange(-180.,181.,20.))
m.drawmapboundary(fill_color='aqua')
# draw tissot's indicatrix to show distortion.
ax = plt.gca()
#for y in np.linspace(m.ymax/20,19*m.ymax/20,9):
#    for x in np.linspace(m.xmax/20,19*m.xmax/20,12):
#        lon, lat = m(x,y,inverse=True)
#        poly = m.tissot(lon,lat,1.5,100,\
#                        facecolor='green',zorder=10,alpha=0.5)
plt.title("Mercator Projection")

lon1 = -38.537
lat1 = -13.012
lons = [lon1, -38.491, -38.491]
lats = [lat1, -13.012, -12.958]
x,y = m(lons, lats)
m.plot(x, y, 'bo', markersize=6)


plt.show()

#lat -12.4176
#lat -13.4526
#long -38.0282
#long -39.0917
