"""
This function generates latitude and longitude coordinates array in a numpy array
It needs a netcdf file and its output is a numpy array.
"""
# Dependencies
import numpy as np
import json
from pprint import pprint

from settings import settings


print(settings)

# Code
#dataset = netCDF4.Dataset('../../Experiment/wrfout_d03_2017-01-05_00_00_00')

class Coordinates(object):
    def __init__(self, latitudes, longitudes, hlatitude, llatitude, hlongitude, llongitude):
        self.latitudes = latitudes
        self.hlatitude = hlatitude
        self.llatitude = llatitude
        self.longitudes = longitudes
        self.hlongitude = hlongitude
        self.llongitude = llongitude
            
def coordinates(dataset):
	xlat = dataset.variables['XLAT'][:,:,:]
	xlong = dataset.variables['XLONG'][:,:,:]
	temperature = []; lat = []; lon = []
	lon = xlong[:1, :,:].squeeze()
	lat = xlat[:1, :, :].squeeze()
	hlat, llat = np.amax(xlat), np.amin(xlat)
	hlong, llong = np.amax(xlong), np.amin(xlong)
