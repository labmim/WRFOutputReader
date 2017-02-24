# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 13:25:42 2016

@author: eowfenth
"""

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize = (12,12))
m = Basemap(projection='ortho', lat_0=-12,lon_0=-38.,resolution = 'h', area_thresh = 1.0)
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.
#m = Basemap(width=12000000,height=9000000,projection='ortho',
#            resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
# draw a land-sea mask for a map background.
# lakes=True means plot inland lakes with ocean color.
#m.drawlsmask(land_color='coral',ocean_color='aqua',lakes=True)
#plt.show()
    # lower-left corner
    #llcrnrlon = -40, llcrnrlat = -14,
    # upper-right corner
    #urcrnrlon= -36, urcrnrlat= -11)   
#m.drawmapboundary(fill_color='red')
#m.drawcoastlines(color="black")
#m.fillcontinents(color='coral',lake_color='aqua')
#m.drawparallels(np.arange(10,90,20))
#m.drawmeridians(np.arange(-180,180,30))
m.drawcountries()
#m.drawstates()
#m.fillcontinents('coral')
#m.drawmapboundary()

#lon = -38.360
#lat = -12.75
#txt = 'Salvador'
#x,y = m(lon, lat)
#m.plot(x, y, 'bo', markersize=24, color='black')
#plt.text(txt)
plt.show()