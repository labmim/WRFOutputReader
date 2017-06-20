#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 09:28:33 2016

@author: eowfenth
"""
# Dependencies
import numpy as np
import matplotlib.pyplot as plt
import netCDF4
from os import listdir


location = 'Files'
file = 'met_em'
gradeSize = 'd01'
date = '2016-09-19'
fileFormat = 'nc'

directory = location + '/' + date + '/' + gradeSize + '/'
# 1. Look for the directory and the files in it

try:
    filesList = sorted(listdir(directory))
    print("There are", len(filesList), "files in this path.")
    print("---------------")
    print("These are the files:")
    print("---------------")
    print(filesList)
    
except:
    print("---------------")
    print("Something is wrong. Make sure the data entries are correct and")
    print("there are all the files in the path.")
    print("---------------")


currentDay = {}
period = []
completed = False

# 2. Will read each file
#while not completed:
for file in filesList:
    currentFile = file
    print("---------------")
    print("Current file:", currentFile)
    print("---------------")
    currentDataset = netCDF4.Dataset(directory + currentFile)
    
    print("Reading file for date:", currentDataset.SIMULATION_START_DATE)
    currentHour = currentDataset.SIMULATION_START_DATE[11:]
    period.append(currentHour)
    print("---------------")

    # Temperature - "perturbation potential temperature (theta-t0)"
    temperature = currentDataset.variables['TT']
    #print("Temperature dimensions", temperature.dimensions)
    #print("Temperature units:", temperature.units)
    temperature_array = temperature[:].squeeze()

    # Height - 
    height = currentDataset.variables['GHT']
    #print("Height dimensions", height.dimensions)
    #print("Height units:", height.units)
    height_array = height[:].squeeze()
    
    sliced_temperature = np.array([])
    sliced_height = np.array([])
    for slice in temperature_array:
        sliced_temperature = np.append(sliced_temperature, slice[11:12,11:12])
    for slice in height_array[:]:
        sliced_height = np.append(sliced_height, slice[11:12, 11:12])
    
#    plt.plot(sliced_temperature, sliced_height)
#    plt.ylabel('height')
#    plt.xlabel('Temperature')
#    plt.show()
    
# 3. Will add info to a file
    currentDay[currentHour] = [sliced_height, sliced_temperature]

    print("Finished reading")
    currentDataset.close()
    
# 4. Will plot the information

print("---------------")
print("Printing summary:")
print("")
print("There are", len(period), "simulation times available.")
print("The grid for the gathered data is", len(currentDay[period[0]][0]), "x", len(currentDay[period[0]][1]))
print("")
print("Now, plotting from", period[0], "to", period[-1], "from", date)
print("---------------")




choseTemperature = np.array([])
for index in range(len(period)):
#    print(period[index])
#    print(currentDay[period[index]][0][0:1])
#    print(currentDay[period[index]][1][0:1])
    choseTemperature = np.append(choseTemperature, currentDay[period[index]][1][0:1])
#   print(choseTemperature)
plt.plot(choseTemperature - 273)
plt.ylabel('Temperature in Kelvin (K)')
plt.xlabel('Time in Hour (hh:mm:ss)')
plt.xticks([0,1,2,3,4,5,6,7], period, rotation = 'vertical')
plt.show()

#print(currentDay[period[index]][0][0:1])
        