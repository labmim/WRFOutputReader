import numpy as np
from settings import settings

variables = settings['variables']

# /*
#   Obtém latitude
# */

def getLatitude():
    latitude = dataset.variables[variables['latitude']]
    lat = latitude[:1, :, :].squeeze()
    return lat

# /*
#   Obtém longitude
# */

def getLongitude():
    longitude = dataset.variables[variables['longitude']]
    lon = longitude[:1, :, :].squeeze()
    return lon

# /*
#   Obtém máximos e mínimos da latitude
# */

def getMaxMinFromLatitude(latitude):
    hlat, llat = np.amax(latitude), np.amin(latitude)
    return hlat, llat

# /*
#   Obtém máximos e mínimos da longitude
# */

def getMaxMinFromLongitude(longitude):
    hlong, llong = np.amax(longitude), np.amin(longitude)
    return hlong, llong