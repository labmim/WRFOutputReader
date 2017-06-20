import netCDF4
import numpy as np
dataset = netCDF4.Dataset('../../Experiment/wrfout_d03_2017-01-05_00_00_00')

xlat = dataset.variables['XLAT'][:,:,:]# 10
xlong = dataset.variables['XLONG'][:,:,:] # 12
temp = dataset.variables['T2'][:,:,:]

print("Title:", dataset.TITLE)
print("Start Date:", dataset.START_DATE)
print("Simulation Start Date", dataset.SIMULATION_START_DATE)
print("Julian Day:", dataset.JULDAY, "Julian Year:", dataset.JULYR)
print("Map Projection:", dataset.MAP_PROJ_CHAR)

print("Highest Temperature:", np.amax(temp))
print("Lowest Temperature:", np.amin(temp))

print("Highest Latitude:", np.amax(xlat))
hlat, llat = np.amax(xlat), np.amin(xlat)
print("Lowest Latitude:",np.amin(xlat))
print(hlat, llat)

print("Highest Longitude:",np.amax(xlong))
hlong, llong = np.amax(xlong), np.amin(xlong)
print("Lowest Longitude:",np.amin(xlong))
print(hlong, llong)

print("Central Latitude:", dataset.CEN_LAT)
print("Central Longitude:", dataset.CEN_LON)