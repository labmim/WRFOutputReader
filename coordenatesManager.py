import numpy as np
from settings import settings

variables = settings['variables']

# /*
#   Obtém dataset de latitude
# */

def getLatitudeByDataset(dataset):
    latitude = dataset.variables[variables['latitude']]
    return latitude
latitude = getLatitudeByDataset(dataset)

# /*
#   Obtém dataset de longitude
# */

def getLongitudeByDataset(dataset):
    latitude = dataset.variables[variables['longitude']]
    return longitude
longitude = getLongitudeByDataset(dataset)

# /*
#   Obtém latitude
# */

def getLatitude():
    latitude = variables['latitude']
    lat = latitude[:1, :, :].squeeze()
    return lat

# /*
#   Obtém longitude
# */

def getLongitude():
    longitude = variables['longitude']
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