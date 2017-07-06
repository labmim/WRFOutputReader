#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 00:07:46 2016

@author: eowfenth
"""
# Dependencies

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections, axes, transforms
import netCDF4
from os import listdir
from datetime import datetime, timedelta
from mpl_toolkits.basemap import Basemap
from matplotlib import ticker
import matplotlib.patches as mpatches
import statistics as stats

# Variables
# T2, TH2, G2, V10, U10, PSFC

dataset = netCDF4.Dataset('../input/wrfout_d03_2017-06-26.nc')

xlat = dataset.variables['XLAT'][:,:,:]
xlong = dataset.variables['XLONG'][:,:,:]
temp = dataset.variables['T2'][:,:,:]
th2 = dataset.variables['TH2'][:,:,:]
u10 = dataset.variables['U10'][:,:,:]
v10 = dataset.variables['V10'][:,:,:]
qvapor = dataset.variables['Q2'][:,:,:]
psfc = dataset.variables['PSFC'][:,:,:] 


# Setup 
print("Highest Temperature:", np.amax(temp))
print("Lowest Temperature:", np.amin(temp))
print("")
print("Highest U10:", np.amax(u10))
print("Lowest U10:", np.amin(u10))
print("")
print("Highest V10:", np.amax(v10))
print("Lowest V10:", np.amin(v10))
print("")
print("Highest QVAPOR:", np.amax(qvapor))
print("Lowest QVAPOR:", np.amin(qvapor))
print("")
print("Highest PSFC:", np.amax(psfc))
print("Lowest PSFC:", np.amin(psfc))
print("")

print("Highest Latitude:", np.amax(xlat))
hlat, llat = np.amax(xlat), np.amin(xlat)
print("Lowest Latitude:",np.amin(xlat))
print("")

print("Highest Longitude:",np.amax(xlong))
hlong, llong = np.amax(xlong), np.amin(xlong)
print("Lowest Longitude:",np.amin(xlong))
print("")

print("Central Latitude:", dataset.CEN_LAT)
print("Central Longitude:", dataset.CEN_LON)

print("Start Date:", dataset.START_DATE)
print("Simulation Start Date", dataset.SIMULATION_START_DATE)
print("Julian Day:", dataset.JULDAY, "Julian Year:", dataset.JULYR)
print("Map Projection:", dataset.MAP_PROJ_CHAR)



temperature_array = temp#.squeeze()


times_array = dataset.variables['Times'][:]

date_array = np.array([])
for times in times_array:
    #print(times[:4])
    #print(times[5:7])
    #print(times[8:10])
    #print(times[11:])
    #print(type(b''.join(times.tolist()).decode('UTF-8')))
    currentTime = b''.join(times.tolist()).decode('UTF-8')
    date_array = np.append(date_array, currentTime)

#for slice in temperature_array:
#    sliced_temperature = np.append(sliced_temperature, slice[11:12,11:12])
#for slice in height_array[:]:
#    sliced_height = np.append(sliced_height, slice[11:12, 11:12])
print("Gathering data...")
print("-----")
sliced_temperature = np.array([])
sliced_temperature2 = np.array([])
sliced_temperature3 = np.array([])
#sliced_height = np.array([])

day = {}
day2 = {}
day3 = {}
#f1 = np.loadtxt('testet.dat')
#print(f1)

sLat = 14
sLong = 25
sHour = 0

#for hour in range(len(date_array)):
##    print(date_array[hour])
##    print(date_array[hour][:4])
##    print(date_array[hour][5:7])
##    print(date_array[hour][8:10])
##    print(date_array[hour][11:])
#    #print("Reading from day", date_array[hour][0:10])
#    #print("Moment:", date_array[hour][11:])
#    sHour = hour
#    for slice in temperature_array[hour: hour + 1,:,:]:
#        sliced_temperature = np.append(sliced_temperature, slice[sLat:sLat+1, sLong:sLong+1])
#    #for slice in height_array[hour: hour + 1,:,:]:
#    #    sliced_height = np.append(sliced_height, slice[11:12, 11:12])
#    for slice in temperature_array[hour: hour + 1,:,:]:
#        sliced_temperature2 = np.append(sliced_temperature2, slice[sLat+1:sLat+2, sLong:sLong+1])
#        
#    for slice in temperature_array[hour: hour + 1,:,:]:
#        sliced_temperature3 = np.append(sliced_temperature3, slice[sLat+2:sLat+3, sLong:sLong+1])
#
#    if ((hour + 1) % 24 == 0):
#        print("")
#        print("For point 1, Completing day", (hour + 1) // 24 )
#        day[((hour + 1) // 24)] = sliced_temperature
#
#    if ((hour + 1) % 24 == 0):
#        print("")
#        print("For point 2, Completing day", (hour + 1) // 24 )
#        day2[((hour + 1) // 24)] = sliced_temperature2
#    
#    if ((hour + 1) % 24 == 0):
#        print("")
#        print("For point 3, Completing day", (hour + 1) // 24 )
#        day3[((hour + 1) // 24)] = sliced_temperature3
#
#    if (hour == len(date_array) - 1):
#        
#        print("Completing period from", date_array[0][0:10], "to", date_array[-1][0:10])
#        print("-----")
#        print("Plotting period...")
#        limits = [0, 23]
##        for d in day:
##            plt.title('Temperature at 2 meters over day ' + str(d))
##            plt.ylabel('Temperature in Celcius (C)')
##            plt.xlabel('Time in Hour')
##            plt.xlim(limits)
##            plt.ylim([19,30])
##            plt.plot(day[d] - 273.15)
##            plt.savefig('day' + str(d) + '.png', bbox_inches='tight')
##            #plt.hold(True)
##            #plt.plot(f1, '--', color = 'm')
##            #plt.savefig('day' + str(d) + '-2.png', bbox_inches='tight')
##            plt.show()
##            plt.close()
##            limits[0] += 24
##            limits[1] += 24
#        plt.title('Temperature at 2 meters over period')
#        plt.ylabel('Temperature in Celcius (C)')
#        plt.xlabel('Time in Hour')
#        plt.xlim([0,23])
#        plt.ylim([19,30])        
#        plt.plot(day[4] - 273.15, label = 'Latitude 14')
#
#        plt.hold(True)
#        plt.plot(day2[4] - 273.15, color = 'k', label = 'Latitude 15')
#        
#        plt.hold(True)
#        plt.plot(day3[4] - 273.15, color = 'y', label = 'Latitude 16')
#        plt.savefig('period.png', bbox_inches='tight')
#
#        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#        # Place a legend to the right of this smaller subplot.
#        #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#        #plt.show()
#        #plt.close()
#        #plt.hold(True)
#        #plt.plot(f1, '--', color = 'm')
#        #plt.savefig('period2.png', bbox_inches='tight')
#        plt.show()
#        plt.close()

day = {}
day2 = {}
day3 = {}
#f1 = np.loadtxt('testet.dat')
#print(f1)

sLat = 14
sLong = 25
sHour = 0
sliced_variable = np.array([])
sliced_variable2 = np.array([])
sliced_variable3 = np.array([])
sliced_variable4 = np.array([])



##
#
#
#
#
selected_array = temp
meanList = np.array([])
deviationList = np.array([])
#
#selected_array = np.sqrt(u10*u10 + v10*v10)
#
#
#
##
for hour in range(len(date_array)):
#    print(date_array[hour])
#    print(date_array[hour][:4])
#    print(date_array[hour][5:7])
#    print(date_array[hour][8:10])
#    print(date_array[hour][11:])
    #print("Reading from day", date_array[hour][0:10])
    #print("Moment:", date_array[hour][11:])
    sHour = hour
    for slice in selected_array[hour: hour + 1,:,:]:
        sliced_variable = np.append(sliced_variable, slice[15:16,24:25].squeeze())
        sliced_variable2 = np.append(sliced_variable2, slice[15:16,25:26].squeeze())
        sliced_variable3 = np.append(sliced_variable3, slice[14:15,24:25].squeeze())
        sliced_variable4 = np.append(sliced_variable4, slice[14:15,25:26].squeeze())
        meanVariable = np.array([])
        v1 = slice[16:17,24:25].squeeze()
        meanVariable = np.append(meanVariable, v1)
        v2 = slice[16:17,25:26].squeeze()
        meanVariable = np.append(meanVariable, v2)
        v3 = slice[15:16,24:25].squeeze()
        meanVariable = np.append(meanVariable, v3)
        v4 = slice[15:16,25:26].squeeze()
        meanVariable = np.append(meanVariable, v4)
        
        meanVar = np.mean((v1,v2,v3,v4))
        deviationVar = np.std((v1, v2, v3, v4), ddof=1)
        
        #meanVariable = (slice[15:16,25:25].squeeze())
        meanList = np.append(meanList, meanVar)
        deviationList = np.append(deviationList, deviationVar)
        meanList = meanList.squeeze()
        deviationList = deviationList.squeeze()
        # Pegar os 4 valores de variavel
        # Achar o valor médio, e seu desvio
        # Aplicar
        #sliced_variable = np.append(sliced_variable, slice[15:16,24:25].squeeze())
        
        #vlats = slice[15:16, :].squeeze()[0]
        
        ulons = slice[:,25:26].squeeze()[0]
        vlats = slice[15:16, :].squeeze()[0]

        ulons = slice[:,24:25].squeeze()[0]
        vlats = slice[16:17, :].squeeze()[0]

        ulons = slice[:,25:26].squeeze()[0]
        vlats = slice[16:17, :].squeeze()[0]
        
    #for slice in height_array[hour: hour + 1,:,:]:
    #    sliced_height = np.append(sliced_height, slice[11:12, 11:12])
#    for slice in selected_array[hour: hour + 1,:,:]:
#        sliced_variable2 = np.append(sliced_variable2, slice[sLat+1:sLat+2, sLong:sLong+1])
#        
#    for slice in selected_array[hour: hour + 1,:,:]:
#        sliced_variable3 = np.append(sliced_variable3, slice[sLat+2:sLat+3, sLong:sLong+1])

    if ((hour + 1) % 24 == 0):
        print("")
        print("For point 1, Completing day", (hour + 1) // 24 )
        day[((hour + 1) // 24)] = sliced_variable

#    if ((hour + 1) % 24 == 0):
#        print("")
#        print("For point 2, Completing day", (hour + 1) // 24 )
#        day2[((hour + 1) // 24)] = sliced_variable2
#    
#    if ((hour + 1) % 24 == 0):
#        print("")
#        print("For point 3, Completing day", (hour + 1) // 24 )
#        day3[((hour + 1) // 24)] = sliced_variable3

    if (hour == len(date_array) - 1):
        
        print("Completing period from", date_array[0][0:10], "to", date_array[-1][0:10])
        print("-----")
        print("Plotting period...")
        limits = [0, 23]
#        for d in day:
#            plt.title('Temperature at 2 meters over day ' + str(d))
#            plt.ylabel('Temperature in Celcius (C)')
#            plt.xlabel('Time in Hour')
#            plt.xlim(limits)
#            plt.ylim([19,30])
#            plt.plot(day[d] - 273.15)
#            plt.savefig('day' + str(d) + '.png', bbox_inches='tight')
#            #plt.hold(True)
#            #plt.plot(f1, '--', color = 'm')
#            #plt.savefig('day' + str(d) + '-2.png', bbox_inches='tight')
#            plt.show()
#            plt.close()
#            limits[0] += 24
#            limits[1] += 24
        fig = plt.figure(figsize=(10,7))
        plt.title('Some variable over period')
        plt.ylabel('Some unit')
        plt.xlabel('Time in Hour (UTC)')
        plt.xlim([0,23])
        #plt.ylim([19,30])  
        L = []
        for i in range(97):
            L += [i]
        #plt.errorbar(L, meanList, yerr = deviationList, color = 'red', ecolor = 'lightcoral', ls='dotted') #label = 'Latitude 14')

        #plt.hold(True)

        #fig.plot(y1, x, y2, x, color='black')
        #plt.fill_between(meanVar, deviationVar, color='grey', alpha='0.5')

        #plt.plot(sliced_variable2, color = 'k')#')
        #plt.plot(sliced_variable, color = 'y')
        #plt.plot(sliced_variable3, color = 'g')
        #plt.plot(sliced_variable4, color = 'b')
        #plt.plot(meanList, color='red')
        #plt.plot(sliced_variable, sliced_variable2, sliced_variable, sliced_variable3)
        #plt.plot(date_array, meanVar, 'k-')
        
        plt.fill_between(L, (meanList-deviationList),  (meanList+deviationList), color = 'pink')#, interpolate=True)
#
        #print(len(date_array), len(meanList), len(deviationList))
        #plt.fill_between()
#        plt.hold(True)
#        plt.plot(day3[4], color = 'y', label = 'Latitude 16')
#        plt.savefig('period.png', bbox_inches='tight')

        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        # Place a legend to the right of this smaller subplot.
        #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        #plt.show()
        #plt.close()
        #plt.hold(True)
        #plt.plot(f1, '--', color = 'm')
        #plt.savefig('period2.png', bbox_inches='tight')
        plt.show()
        plt.close()
        
dataset.close()