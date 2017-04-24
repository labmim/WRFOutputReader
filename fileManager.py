import os
from settings import settings
import arrow

# Constants
INPUT_PATH = settings['settings']['location']['input']
OUTPUT_PATH = settings['settings']['location']['output']

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
        if file[-3:] == ".nc":
            ncList.append(file)
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

def getTodayFileName():
    today = getTodayDate()
    fileList = listFiles(INPUT_PATH)
    for item in fileList:
        itemDate = obtainDateFromFileName(item)
        if (itemDate == today):
            return item
    return fileList[-1]

# /*
#   Retorna o arquivo com o caminho completo
# */

def getTodayFilePath():
    return INPUT_PATH + getTodayFileName()


# /*
#   Retorna o tamanho da grade
#   A partir do padrão "wrf_GRADE_ANO-MES-DIA.nc"
# */

def getGradeSize():
    currentFile = getTodayFileName()
    grade = currentFile[7:10]
    return grade

# /*
#  Gera um caminho para salvar os gráficos
# */

def getSavePath(variable, grade):
    date = obtainDateFromFileName(getTodayFileName())
    path = OUTPUT_PATH + \
            date + "/" + \
            getGradeSize() + '/' + \
            variable + "/"
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
    saveName = variable + "_" + grade + "_" + \
    correctNumberInFileName(index) + ".png"
    return saveName

# /*
#   Gera um log informativo
# */

def generateLog(variable, index, grade):
    print("Generating figure no. " + str(index) + " from " + variable + "/" + grade)