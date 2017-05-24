from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from settings import settings
from timeLoader import date, analysis
import fileManager
import numpy as np

time = settings['time']
OUTPUT_PATH = settings['settings']['location']['output']

# /*
# Instancia um mapa
# */

def createMap(lowestLongitude, highestLongitude, lowestLatitude, highestLatitude):
    map = Basemap(rsphere=(6378137.00,6356752.3142),\
                   resolution='h',area_thresh=0.1,projection='merc',\
                    llcrnrlon= lowestLongitude, llcrnrlat= lowestLatitude,
                    urcrnrlon= highestLongitude, urcrnrlat= highestLatitude)
    return map


# /*
# Cria um título formatado para o mapa
# */

def createTitle(variable, hour):
    model = settings['settings']['title_information']['model']
    lab = settings['settings']['title_information']['lab']
    forecast = date[hour].format(time['format'], locale=time['locale'])
    variableTitle = settings[variable]['title']
    title = " " + model + " — " + lab + "\n Início Análise: " + analysis + " (UTC)"+ "\n Previsão: " + forecast + " HL"  + " — " + variableTitle
    return title

# /*
# Desenha as linhas das costas, meridianos e paralelos
# */

    

# /*
#   Salva o arquivo com o nome correto
#   No formato, "grade_imagemNumber.png"
# */

def getSavePath(variable, hour):
    OUTPUT_PATH = settings['settings']['location']['output']
    savePath = OUTPUT_PATH + fileManager.getGradeSize() + "/" + fileManager.getGradeSize() + "_" + CorrectNumberInFileName(hour) + settings[variable]['filename_extension'] +'.png'
    return savePath


def CorrectNumberInFileName(index):
    if (index < 10):
        return "00" + str(index)
    elif (index >= 10 and index <= 99):
        return "0" + str(index)
    return str(index)


# /*
# Define os meridianos
# */

def makeMeridians(llong, hlong, grade):
    if (grade == "d01"):
        return np.arange(llong, hlong, 1.3)
    elif (grade == "d02"):
        return np.arange(llong, hlong, 0.13)
    else:
        return np.arange(-38.7334, -38.2808, 0.07)

# /*
# Define os paralelos
# */

def makeParallels(llat, hlat, grade):
    if (grade == "d01"):
        return np.arange(llat, hlat, 1.1)
    elif (grade == "d02"):
        return np.arange(llat, hlat, 0.09)
    else:
        return np.arange(-13.1336, -12.6928, 0.06)