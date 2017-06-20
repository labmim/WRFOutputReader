# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 19:53:33 2016

@author: eowfenth
"""
import numpy as np
import matplotlib.pyplot as plt
import netCDF4
dataset = netCDF4.Dataset('Files/met_em.d02.2016-07-27_15_00_00.nc')

## D02 --
## 27/07/2016 - 15:00:00

# Output from METGRID V3.7.1
#print(dataset.variables.keys())
#print(dataset.dimensions.keys())

# Temperature - "perturbation potential temperature (theta-t0)"
temperature = dataset.variables['TT']
print("Temperature dimensions", temperature.dimensions)
print("Temperature units:", temperature.units)
temperature_array = temperature[:].squeeze()

print(' ')
# Surface Pressure
surface_pressure = dataset.variables['PSFC']
print("Surface pressure dimensions", surface_pressure.dimensions)
print("Surface Pressure units:", surface_pressure.units)
surface_pressure_array = surface_pressure[:].squeeze()

print(' ')
# Relative Humidity
relative_humidity = dataset.variables['RH']
print("Relative humidity dimensions", relative_humidity.dimensions)
print("Relative humidity units:", relative_humidity.units)
relative_humidity_array = relative_humidity[:].squeeze()

print(' ')
# UU -- "x-wind component"
uu = dataset.variables['UU']
print("UU dimensions", uu.dimensions)
print("UU units:", uu.units)
uu_array = uu[:].squeeze()

print(' ')
# VV -- "y-wind component"
vv = dataset.variables['VV']
print("VV dimensions", vv.dimensions)
print("VV units:", vv.units)
vv_array = vv[:].squeeze()[0:1,:-1,].squeeze()

#print(dataset)
#print(surface_pressure)

xlat = dataset.variables['XLAT_U'][0][:,:-1]
xlong = dataset.variables['XLONG_U'][0][:,:-1]
latmax, latmin = -13.453, -12.418
longmax, longmin = -39.115, -38.005

latmask=np.ma.masked_where(xlat<latmin,xlat).mask+np.ma.masked_where(xlat>latmax,xlat).mask
lonmask=np.ma.masked_where(xlong<longmin,xlong).mask+np.ma.masked_where(xlong>longmax,xlat).mask
totmask = lonmask + latmask

#plt.pcolormesh(totmask)
sliced_temp = temperature_array[:,11:12,11:12]
print(sliced_temp)

albedo = dataset.variables['ALBEDO12M'][:].squeeze()[:1].squeeze()

mark = np.ma.masked_where(totmask, albedo)
#fig=plt.figure()

#plt.contourf(mark)
fig=plt.figure()
plt.contourf(albedo)
plt.show()



#rint(dataset.variables['ST100200'])
#print(dataset.variables['ST040100'])
#print(dataset.variables['ST010040'])
#print(dataset.variables['ST000010'])

print(dataset.variables['GHT'])
height_array = dataset.variables['GHT'][:].squeeze()

#print(dataset.variables['GHT'])
# 
#print(dataset.variables.keys())
#
#ind = vv_array[0,:,:]
#print(ind)

# Lat, lon: -13 PARA UTILIZAR E EXTRAIR
    # -38.508
#print(dataset)
#a = dataset['corner_lats'][:]

# Aqui, temos o vetor completo.

#st = temperature_array[:,11:12,11:12]

print(" ")
print(dataset.SIMULATION_START_DATE, "\n")

sliced_pressure = np.array([])
pressure = dataset.variables['PRES']
pressure_array = pressure[:].squeeze()
sliced_temperature = np.array([])

for slice in pressure_array:
    sliced_pressure = np.append(sliced_pressure, slice[11:12, 11:12])
#sliced_pressure = sliced_pressure[::-1]
for slice in temperature_array:
    sliced_temperature = np.append(sliced_temperature, slice[11:12,11:12])
sliced_temperature = sliced_temperature - 273

sliced_height = np.array([])
for slice in height_array:
    sliced_height = np.append(sliced_height, slice[11:12, 11:12])
sliced_height = sliced_height


plt.plot(sliced_temperature, sliced_height)
plt.xlabel('Height')
plt.ylabel('Temperature')
plt.show()
