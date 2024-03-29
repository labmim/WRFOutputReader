from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

map = Basemap(projection='poly', 
              lon_0=0.0, lat_0=0,             
              llcrnrlon=-80.,llcrnrlat=-40,urcrnrlon=80.,urcrnrlat=40.)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

map.drawparallels(np.arange(-12, -10, 0.2), linewidth=2, labels=[1,0,0,1], color='r', zorder=0 )
plt.show()