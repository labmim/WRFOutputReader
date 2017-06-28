#coding: utf-8
import os
from settings import settings
import arrow

# Constants
INPUT_PATH = settings['settings']['location']['input']
OUTPUT_PATH = settings['settings']['location']['output']
FILE_INFORMATION = settings['settings']['file_information']

# Verificar a data de hoje

# /*
#   Está em horário * LOCAL *
# */

def getTodayDate():
    today = arrow.utcnow().to('America/Bahia').format('YYYY-MM-DD')
    return today

# Verifica os arquivos existentes dentro de input

# /*
#   Retorna a lista de arquivos .nc
# */

def listFiles(path):
    ncList = []
    fileList = os.listdir(path)
    for file in fileList:
#        if file[-3:] == ".nc":
#            ncList.append(file)
        if file[0:6] == FILE_INFORMATION['base']:
            ncList.append(file)
    ncList.sort()
    return ncList

# /*
#   Retorna a data de um dado arquivo a partir do nome
#   A partir do padrão "wrfout_GRADE_ANO-MES-DIA.nc"
# */

def obtainDateFromFileName(givenFile):
    #currentYear = givenFile[11:15]
    #currentMonth = givenFile[16:18]
    #currentDay = givenFile[19:21]
    fileDate = givenFile[11:21]
    return fileDate

# /*
#   Retorna o arquivo do dia atual
#   do contrário, retorna o último
# */

def getCurrentFileName():
    today = getTodayDate()
    fileList = listFiles(INPUT_PATH)
    for item in fileList:
        itemDate = obtainDateFromFileName(item)
        if (itemDate == today):
            if (itemDate[0:6] == 'wrfout'):
                return item
    return fileList.pop(-1)

# /*
#   Retorna o arquivo com o caminho completo
# */

def getTodayFilePath():
    return INPUT_PATH + getCurrentFileName()


# /*
#   Retorna o tamanho da grade
#   A partir do padrão "wrf_GRADE_ANO-MES-DIA.nc"
# */

def getGradeSize():
    currentFile = getCurrentFileName()
    grade = currentFile[7:10]
    return grade

# /*
#   Retorna um arquivo netcdf com a grade desejada
# */

def getFileByGrade(grade):
    list = listFiles(INPUT_PATH)
    for item in list:
        if item[7:10] == grade:
            return item

# /*
#   Retorna o arquivo com caminho completo a partir da grade
# */

def getCurrentFilePathByGrade(grade):
    item = getFileByGrade(grade)
    return INPUT_PATH + item

# /*
#  Gera um caminho para salvar os gráficos
# */

def getSavePath(variable, grade):
    date = obtainDateFromFileName(getCurrentFileName())
    path = OUTPUT_PATH + \
            date + "/"
    if not os.path.exists(path):
        os.makedirs(path)
    return path

# /*
#   Gera um número de arquivo adequado
#   no formato "0XX.png""
# */

def correctNumberInFileName(index):
    if (index < 10):
        return "00" + str(index)
    elif (index >= 10 and index <= 99):
        return "0" + str(index)
    return str(index)

# /*
#   Gera um nome para o arquivo
# */

# variable + _ + grade + data + .png
def getSaveFileName(variable, index, grade):
    saveName = grade.upper() + "_" + settings[variable]['filename_extension'].upper() + \
    correctNumberInFileName(index) + ".png"
    return saveName

# /*
#   Gera um log informativo
# */

def generateLog(variable, index, grade):
    print("Generating figure no. " + str(index) + " from " + variable + "/" + grade)