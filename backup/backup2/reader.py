# Dependencies
from netCDF4 import Dataset as dt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as bm

# Important Informations
# WRF is using NETCDF3_64BIT_OFFSET file format
# NETCDF3 is not the most updated version of the file format

# Choose the dataset file name
filestr = 'Files/met_em.d02.2016-07-31_15_00_00.nc'
ncfile = dt(filestr, 'r')


#'PSFC', 'RH', 'VV', 'UU', 'TT'

# Get the file format
#print(ncfile.file_format)

# Variables 
#TTROP0 = ncfile.variables['TTROP']
#TT = ncfile.variables['TT'][:]
#npTT = np.array(TTROP, dtype=np.float32)
VV = ncfile.variables['VV'][:]
npVV = np.array(VV, dtype=np.float32)
UUdesc = ncfile.variables['UU'].description
#print(npVV.shape)
#a = npVV.squeeze()
#print(a.shape)


VV = ncfile.variables['PSFC']
print(VV)

print(VV.units)
print(VV.description)
#print(TTROP0)
#
#x_dim = ncfile.dimensions['west_east']
#y_dim = ncfile.dimensions['south_north']
#print(x_dim, y_dim)
#print(ncfile.dimensions.keys())
#print(ncfile.variables.keys())
#print(ncfile.variables['TTROP'].units)
#m = bm(projection="robin", lon_0 = 0, resolution = "c")
# Methods
# print(ncfile.variables.keys()) # returns all of the variable keys
# ncfile.dimensions.keys() return all of the variable keys

# f.close()
#plt.figure(figsize=(12, 15))
#ssa -12, -38

#map = bm(projection='aeqd', lon_0 = 10, lat_0 = 50)

#map.drawmapboundary(fill_color='aqua')
#map.fillcontinents(color='coral',lake_color='aqua')
#map.drawcoastlines()
#map.bluemarble()
#plt.show()
#map.drawmapboundary(fill_color='aqua')
#map.fillcontinents(color='coral', lake_color='aqua')
#map.drawcoastlines(color='gray')
#m.bluemarble()
#m.fillcontinents()
## Setup output
# plt.figure(figsize=(12, 12))
