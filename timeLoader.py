import netCDF4
import arrow
import numpy as np

# Dependencies
from settings import settings
import fileManager


# dataset variables in come

dataset = netCDF4.Dataset(fileManager.getTodayFilePath())

times_array = dataset.variables['Times'][:]

"""

    As variáveis do dataset estarão disponíveis.
    As váriveis de settings estarão disponíveis.
        

    Array de objetos serão expostos para determinado dataset.
"""

# --- End of Dependencies ---

times = times_array
date_array = np.array([])
date = np.array([])


def organizeAnalysisDate(dateString):
    strDate = dateString
    currentYear = strDate[:4]
    currentMonth = strDate[5:7]
    currentDay = strDate[8:10]
    currentHour = strDate[11:13]
    #currentMinute = strDate[14:16]
    #currentSeconds = strDate[17:]

    # -- Instanciate an aware Arrow object
    print(currentDay, currentMonth, currentYear)
    currentDate = arrow.Arrow(\
				int(currentYear), \
				int(currentMonth), \
				int(currentDay), \
				int(currentHour), \
				tzinfo = 'UTC')
    analysisDate = currentDate.to('America/Bahia')
    return analysisDate

analysis = organizeAnalysisDate(dataset.START_DATE).to('utc').format('DD/MM/YYYY HH:mm:ss')

def organizeDate(dateString):
    # -- Slicing the string
    # dateString current format: 2017-01-13_00:00:00
    strDate = dateString
    currentYear = strDate[:4]
    currentMonth = strDate[5:7]
    currentDay = strDate[8:10]
    currentHour = strDate[11:13]
    #currentMinute = strDate[14:16]
    #currentSeconds = strDate[17:]

    # -- Instanciate an aware Arrow object
    currentDate = arrow.Arrow(\
				int(currentYear), \
				int(currentMonth), \
				int(currentDay), \
				int(currentHour), \
				tzinfo = 'UTC')
    date = currentDate.to('America/Bahia')
    return date

for times in times_array:
    #print(times[:4])
    #print(times[5:7])
    #print(times[8:10])
    #print(times[11:])
    #print(type(b''.join(times.tolist()).decode('UTF-8')))

    # Proccess bytes to string
    currentTime = b''.join(times.tolist()).decode('UTF-8')

    cd = organizeDate(currentTime)

    # -- Format current date

    year = cd.format('YYYY')
    month = cd.format('MM')
    day = cd.format('DD')
    hour = cd.format('HH')
    weekday = cd.format('dddd')
    julian = cd.format('DDD')
    timezone = cd.format('ZZ')
    date_array = np.append(date_array, currentTime)
    date = np.append(date, cd)

#
#class TimeLoader(object):
#    def __init__(self):
#        self.dateArray = np.array([])
#
#    def getTime(self, index):
#        return self.dateArray[index]
#
#import timeLoader
#print(timeLoader.date[0].format('YYYY-MM-DD HH:mm:ss ZZ dddd', locale='pt_br'))
#print(timeLoader.date[0].format('DD/MM/YYYY HH:mm:ss ZZ'))
#
#now = timeLoader.date
#print(type (timeLoader.date[0]))
#
#print((timeLoader.date[0]).to('utc'))
