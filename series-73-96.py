# List files [x]
# Obter datas de todos esses arquivos
# Separate these files
# Check the order [x]
# Verify days, verify missing days
# Obtain Data
# Save File

import netCDF4
import arrow
import numpy as np

import timeLoader
# Dependencies
from settings import settings
import fileManager
from os import listdir

publicDiario = []
publicPrevisao = []
publicAll = []
lastSimulationDay = ['']
def getDateList(fileList):
    dateList = []

    for element in fileList:
        currentYear = element[11:15]
        currentMonth = element[16:18]
        currentDay = element[19:21]
        currentHour = 20
        currentDate = arrow.Arrow(\
        				int(currentYear), \
        				int(currentMonth), \
        				int(currentDay), \
        				int(currentHour), \
        				tzinfo = 'UTC')
        dateList.append(currentDate)
    return dateList

def isThereNextDay(currentDay, nextDay):
    if (currentDay.replace(days=+1) == nextDay):
        return True
    else:
        return False


fileList = fileManager.listFiles('./input/')
dateList = getDateList(fileList)

#
#for i in range(len(dateList)):
#    print(dateList[i])
#    

def getInformation(fileItem):
    
    # Starting Settings
    
    dataset = netCDF4.Dataset('./input/' + fileItem)
    control = 0
    diario = []
    previsao = []
    completo = []
    semanal = {}
    arquivo = 1
    date_array = np.array([])
    semanal[arquivo] = {'Diário' : [], 'Previsão' : []}
    
    # Dataset Variables
    
    times_array = dataset.variables['Times'][:]
    
    
    for times in times_array:
        currentTime = b''.join(times.tolist()).decode('UTF-8')
        #print(currentTime)
        
        # -- Organize the current date
        
        strDate = currentTime
        currentYear = strDate[:4]
        currentMonth = strDate[5:7]
        currentDay = strDate[8:10]
        currentHour = strDate[11:13]
        currentMinute = strDate[14:16]
        currentSeconds = strDate[17:]

        xlat = dataset.variables['XLAT'][:]
        xlong = dataset.variables['XLONG'][:]
        temp = dataset.variables['T2'][:]
        th2 = dataset.variables['TH2'][:]
        u10 = dataset.variables['U10'][:]
        v10 = dataset.variables['V10'][:]
        p = dataset.variables['PSFC'][:]
        qv = dataset.variables['Q2'][:]
        h = dataset.variables['HGT'][:]
        rainc = dataset.variables['RAINC'][:]
        hfx = dataset.variables['HFX'][:]
        lh = dataset.variables['LH'][:]
        swdown = dataset.variables['SWDOWN'][:]
        simulation_start = dataset.SIMULATION_START_DATE
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
        
        qv_array = qv[:,15:16, 25:26].squeeze()
        qvfix = qv_array[control:control+1][0]   
        
        rainc_array = rainc[:,15:16, 25:26].squeeze()
        raincfix = rainc_array[control:control+1][0]   

        hfx_array = hfx[:,15:16, 25:26].squeeze()
        hfxfix = hfx_array[control:control+1][0]
        
        lh_array = lh[:,15:16, 25:26].squeeze()
        lhfix = lh_array[control:control+1][0]
        
        swdown_array = swdown[:,15:16, 25:26].squeeze()
        swdownfix = swdown_array[control:control+1][0]
        
        print("Running control", control)
        print("lastSimulationDay", lastSimulationDay[-1])
        print("simulation_start", simulation_start)
        if (simulation_start == lastSimulationDay[-1]):
            control += 1
            break 
        
        if (control < 24):
            status = 'Diária'
            statusn = 1
            diario.append([fileItem, year, month, day, hour, julian, tempfix, u10fix, v10fix, pfix, qvfix, th2fix, raincfix, hfxfix, lhfix, swdownfix, status])
        else:
            status = 'Previsão'
            statusn = 0
            previsao.append([fileItem, year, month, day, hour, julian, tempfix, u10fix, v10fix, pfix, qvfix, th2fix, raincfix, hfxfix, lhfix, swdownfix, status])
        control += 1
        #completo.append([year, month, day, hour, weekday, julian, timezone, tempfix, u10fix, v10fix, pfix, qvfix, cd, status])
        date_array = np.append(date_array, currentTime)
    
    if (dataset):
        dataset.close()
    
    lastSimulationDay.append(simulation_start)
    return diario, previsao

#def getSeries(fileList, dateList, today = True, index = 0, prev = 23):
#    
#    (diario, previsao) = getInformation(fileList[index])
#    publicAll.append(diario)
#     if (today == False):
#         print("\nPrevisao >>", dateList[index])
#     else:
#         print("\nDiario >>", dateList[index])
#         publicAll.append(diario)
    
#     print("\n'is there next day?'", isThereNextDay(dateList[index], dateList[index+1]))
#     print("Today ->", dateList[index])
#     print("Next Day ->", dateList[index+1])


#     if (isThereNextDay(dateList[index], dateList[index+1])):
        
#         try:
#             getSeries(fileList[index+1:], dateList[index+1:], today = True)
#         except:
#             print("Out of Range")
#     else:


#         if (isThereNextDay(dateList[index].replace(days=+1), dateList[index+1])):
#             print("\n'is there next day?'", isThereNextDay(dateList[index].replace(days=+1), dateList[index+1]))
#             print("Today ->", dateList[index].replace(days=+1))
#             print("Next Day ->", dateList[index+1])
#             try:
#                 getSeries(fileList[index+2:], dateList[index+2:])
#             except:
#                 print("Out of Range")
            
#         else:
#             print("\nPrevisao >>", (prev - 22), dateList[index].replace(days=+1))
#             publicAll.append(previsao[0:24])
# #            
#             print("\n'is there next day?'", isThereNextDay(dateList[index], dateList[index+1]))
#             print("Today ->", dateList[index].replace(days=+1))
#             print("Next Day ->", dateList[index+1])
#             print("\nPrevisao >>", (prev - 21), dateList[index].replace(days=+2))
#             publicAll.append(previsao[24:48])

#             if (isThereNextDay(dateList[index].replace(days=+2), dateList[index+1])):
#                 print("\n'is there next day?'", isThereNextDay(dateList[index].replace(days=+2), dateList[index+1]))
#                 print("Today ->", dateList[index].replace(days=+2))
#                 print("Next Day ->", dateList[index+1])
#                 try:
#                     getSeries(fileList[index+1:], dateList[index+1:])
#                 except:
#                     print("Out of Range")
#             else:
#                 print("\nPrevisao >>", (prev - 20), dateList[index].replace(days=+3))
#                 publicAll.append(previsao[48:72])

#                 print("\n'is there next day?'", isThereNextDay(dateList[index].replace(days=+3), dateList[index+1]))
#                 print("Today ->", dateList[index].replace(days=+3))
#                 print("Next Day ->", dateList[index+1])
#                 try:
#                     getSeries(fileList[index+1:], dateList[index+1:])
#                 except:
#                     print("Out of Range")
# #                return
# #                print("\n'is there next day?'", isThereNextDay(dateList[index].replace(days=+2), dateList[index+1]))
# #                print("Today ->", dateList[index].replace(days=+2))
# #                print("Next Day ->", dateList[index+1])
# #                print("Peguei a previsão", prev - 20, dateList[index].replace(days=+3))
# #                getSeries(fileList[index+1:], dateList[index+1:])
        
        
# #def getSeries(fileList, dateList, diario = True):
# #    for i in range(len(fileList)):
# #        (diario, previsao, semanal, completo) = getInformation(fileList[i])
# #        publicPrevisao.append(diario)
# #        np.savetxt('diario.dat', diario, fmt='%s')
# #        np.savetxt('previsao.dat', previsao, fmt='%s')
# #        while (i < len(fileList)):
# #            print("currentDay", dateList[i])
# #            print("nextDay", dateList[i+1])
# #            print("i", i)
# #            print("'is there next day?'", isThereNextDay(dateList[i], dateList[i+1]))
# #            if (isThereNextDay(dateList[i], dateList[i+1])):
# #                print("There is next day")
# #                getSeries(fileList[i+1:], dateList[i+1:])
# #            else:
# #                print("There is not next day")
#  #                publicPrevisao.append(previsao)
# #                if (isThereNextDay(dateList[i], dateList[i+1])):
# #                    getSeries(fileList[i+1:], dateList[i+1:])
#             # while (!isThereNextDay(dateList[i], dateList[i+1])):
#                 #if (There is Next Batch)
#                     #publicPrevisao.append(previsaoNxtBatch)
# #                if (isThereNextDay(dateList[i], dateList[i+1])):
# #                    getSeries(fileList[i+1:], dateList[i+1:])
                
                
            
        
        
#         # Obter informação de i (diária)
#         # Verificar se o próximo dia é o dia seguinte (rsrs)
#         # Caso seja, break
#         # Caso não seja, obter previsão do dia seguinte (previsão)
#         # Verificar se o dia seguinte tem arquivo, do contrário repita.
        
#         # getInformation
#         # while (True):
    
#getSeries(fileList[0:], dateList[0:])

#for element in range(len((fileList[:]))):
#    item = getInformation(fileList[element])
#    publicAll.append(item)
for element in range(len(fileList[:])):
    (diario, previsao) = getInformation(fileList[element])
    publicAll.append(previsao[49:])
document = []
for element in publicAll:
    for elmt in element:
        print(elmt)
        document.append(elmt)

np.savetxt('series-73-96.dat', document, fmt='%s')

