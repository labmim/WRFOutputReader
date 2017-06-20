#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 18:39:46 2016

@author: eowfenth
"""

import numpy as np
import matplotlib.pyplot as plt
import netCDF4
from os import listdir
import arrow

location = ''
file = 'met_em'
gradeSize = 'd01'
date = '2016-09-19'
fileFormat = 'nc'
#
listdir()
directory = '../../project/input/'
# 1. Look for the directory and the files in it
try:
    filesList = sorted(listdir(directory))
    print("There are", len(filesList), "files in this path.")
    print("---------------")
    print("These are the files:")
    print("---------------")
    for element in filesList:
        print(element)
    
except:
    print("---------------")
    print("Something is wrong. Make sure the data entries are correct and")
    print("there are all the files in the path.")
    print("---------------")
    

# 2. Open each file and organize dates.

date_array = np.array([])
timeList = []

diario = []
previsao = []
completo = []
semanal = {}
arquivo = 1
i = 0
for file in filesList:
    currentFile = file
    print("---------------")
    print("Current file:", currentFile)
    print("---------------")
    currentDataset = netCDF4.Dataset(directory + currentFile)
    
    print(currentDataset.SIMULATION_START_DATE)
    xlat = currentDataset.variables['XLAT'][:,:,:]# 10
    xlong = currentDataset.variables['XLONG'][:,:,:] # 12
    temp = currentDataset.variables['T2'][:]
    th2 = currentDataset.variables['TH2'][:]
    u10 = currentDataset.variables['U10'][:]
    v10 = currentDataset.variables['V10'][:]
    p = currentDataset.variables['PSFC'][:,:,:]
    qv = currentDataset.variables['Q2'][:,:,:]
    h = currentDataset.variables['HGT'][:]
    times_array = currentDataset.variables['Times'][:]
    juliand = int(currentDataset.JULDAY)
    control = 0
    
    semanal[arquivo] = {'Diário' : [], 'Previsão' : []}
    for times in times_array:
        currentTime = b''.join(times.tolist()).decode('UTF-8')
        print(currentTime)
        
        # -- Organize the current date
        
        strDate = currentTime
        currentYear = strDate[:4]
        currentMonth = strDate[5:7]
        currentDay = strDate[8:10]
        currentHour = strDate[11:13]
        currentMinute = strDate[14:16]
        currentSeconds = strDate[17:]

        # -- Instanciate an aware Arrow object
        currentDate = arrow.Arrow(int(currentYear), int(currentMonth), int(currentDay), int(currentHour), tzinfo = 'UTC')
        cd = currentDate.to('America/Bahia')
        
        # -- Format current date
        
        year = cd.format('YYYY')
        month = cd.format('MM')
        day = cd.format('DD')
        hour = cd.format('HH')
        weekday = cd.format('dddd')
        julian = cd.format('DDD')
        timezone = cd.format('ZZ')
        
        # -- Format temperature and variables
        
        temp_array = temp[:,15:16,25:26].squeeze()
        tempfix = temp_array[control:control+1][0]       

        th2_array = th2[:,15:16,25:26].squeeze()
        th2fix = th2_array[control:control+1][0] 
        
        u10_array = u10[:,15:16, 25:26].squeeze()
        u10fix = u10_array[control:control+1][0] 

        v10_array = v10[:,15:16, 25:26].squeeze()
        v10fix = v10_array[control:control+1][0]     

        p_array = p[:,15:16, 25:26].squeeze()
        pfix = p_array[control:control+1][0]

        qv_array = qv[:,15:16, 25:26].squeeze()
        qvfix = qv_array[control:control+1][0]     
        
#
        
        if (control < 24):
            status = 'Diária'
            statusn = 1
            diario.append([year, month, day, hour, julian, tempfix, u10fix, v10fix, pfix, qvfix, th2fix, status])
        else:
            status = 'Previsão'
            statusn = 0
            previsao.append([year, month, day, hour, julian, tempfix, u10fix, v10fix, pfix, qvfix, th2fix, status])
        control += 1
        completo.append([year, month, day, hour, weekday, julian, timezone, status, tempfix, u10fix, v10fix, pfix, qvfix, cd, status])
        date_array = np.append(date_array, currentTime)
    
    semanal[arquivo]['Diário'] = diario
    semanal[arquivo]['Previsão'] = previsao
    diario = []
    previsao = []
    np.savetxt('diario.dat', diario, fmt='%s')
    i += 1
    
#    print(currentDataset.variables['T2'])
#    print(currentDataset.variables['U10'])
#    print(currentDataset.variables['V10'])
#    print(currentDataset.variables['P'])
    currentDataset.close()
    arquivo += 1
    #break

def createDatWeekly(fileAmount):
    c = []
    e = 1
    while e is not fileAmount:
        for elmt in semanal[e]['Diário']:
            c.append(elmt)
        e += 1
    for elmt in semanal[e]['Diário']:    
        c.append(elmt)
    for elmt in semanal[e]['Previsão']: 
        c.append(elmt)
    np.savetxt('semanal2.dat', c, fmt='%s')

    return c

createDatWeekly(3)


# Checo lista de arquivos.
# Verifico se há uma sequencia diaria entre esses arquivos.
    # Caso sim, pegar os diários e no ultimo arquivo adicionar os de Previsão.
    # Caso não, preencher com Previsão os dias que estão vazios.
# Retornar dat