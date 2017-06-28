#coding: utf-8
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import collections, axes, transforms
import netCDF4
from os import listdir
from datetime import datetime, timedelta
from mpl_toolkits.basemap import Basemap
from matplotlib import ticker
import arrow

from correctFileName import CorrectNumberInFileName
import timeLoader
from settings import settings
import fileManager
import mapManager


"""

    As variáveis de tempo vão estar disponíveis
    As variáveis do dataset vão estar disponíveis


"""
INPUT_PATH = settings['settings']['location']['input']
OUTPUT_PATH = settings['settings']['location']['output']

# /*
#   A partir da grade, define determinadas configurações da projeção do mapa
# */

grades = settings['main']['grades']

def getLowerValue(variable):
    varflat = variable.flatten()
    varlow = np.amin(varflat)
    return varlow


def getHigherValue(variable):
    varflat = variable.flatten()
    varhigh = np.amax(varflat)
    return varhigh

def getLowerWindValue(variable, variable2):
    var1flat = variable.flatten()
    var2flat = variable2.flatten()
    speedflat = np.sqrt(var1flat*var1flat + var2flat*var2flat)
    varlow = np.amin(speedflat)
    return varlow

def getHigherWindValue(variable, variable2):
    var1flat = variable.flatten()
    var2flat = variable2.flatten()
    speedflat = np.sqrt(var1flat*var1flat + var2flat*var2flat)
    varhigh = np.amax(speedflat)
    return varhigh

def generateGraphs(grade, variable, token = 0):
    

    datasetFile = fileManager.getCurrentFilePathByGrade(grade)
    dataset = netCDF4.Dataset(datasetFile)
    analysis = timeLoader.organizeAnalysisDate(dataset.START_DATE).to('utc').format('DD/MM/YYYY HH:mm:ss')
    date = timeLoader.arrangeDate(dataset);
    if (variable == "temperature"):
        xlat = dataset.variables['XLAT'][:,:,:]
        xlong = dataset.variables['XLONG'][:,:,:]
        temperature = []; lat = []; lon = []
        lon = xlong[:1, :,:].squeeze()
        lat = xlat[:1, :, :].squeeze()
        hlat, llat = np.amax(xlat), np.amin(xlat)
        hlong, llong = np.amax(xlong), np.amin(xlong)        
        var = dataset.variables['T2'][:,:,:].squeeze()
        for i in range(1, len(date)):
            
            # Settings
            
            varmax = getHigherValue(var) - 273.15
            varmin = getLowerValue(var) - 273.15
            celcius = var[i:i+1,:,:] - 273.15 
            colormap = settings['temperature']['colormap']  
            
            # Plot Settings
            
            plt.figure(figsize=(18,9))
            title = mapManager.createTitle('temperature', date, i, analysis)
            plt.title(title, 
                      fontsize = 12, 
                      ha = 'left', 
                      x = -0.01)
            
            plt.suptitle("$^\circ\mathcal{C}$",
                         fontsize = 18, 
                         ha = 'center', 
                         x = 0.79, 
                         y = 0.75)
            plt.xlabel('Longitude', 
                       fontsize = 12, 
                       labelpad = 25)
            plt.ylabel('Latitude', 
                       fontsize = 12, 
                       labelpad = 60)
            
            # Map Settings
            
            m = mapManager.createMap(llong, hlong, llat, hlat)
            x,y = m(lon, lat)
            m.drawcoastlines()
            m.drawparallels(mapManager.makeParallels(llat, hlat, grade), 
                            linewidth=0, 
                            labels=[1,0,0,1], 
                            color='r', 
                            zorder=0, 
                            fmt="%.2f")
            m.drawmeridians(mapManager.makeMeridians(llong, hlong, grade), 
                            linewidth=0, 
                            labels=[1,0,0,1], 
                            color='r', 
                            zorder=0, 
                            fmt="%.2f")
            m.contourf(x, y, np.squeeze(celcius), 
                            alpha = 0.4, 
                            cmap = colormap, 
                            vmin=varmin, 
                            vmax=varmax)
            m.pcolor(x,y,np.squeeze(celcius), 
                            alpha = 0.4,
                            cmap = colormap, 
                            vmin=varmin, 
                            vmax=varmax)
            
            # Colorbar Settings
            cb = plt.colorbar(shrink=0.5, pad=0.04)
            cb.ax.tick_params(labelsize=10)       
            
            #plt.show()
            
            # Log
            
            fileManager.generateLog('temperature', i, grade)
            # Saving Settings
            
            path = fileManager.getSavePath('temperature', grade)
            fileName = fileManager.getSaveFileName('temperature', i, grade)
            
            plt.savefig(path + fileName, bbox_inches='tight')
            plt.close()
        if (dataset):
            dataset.close()
            
    elif (variable == "pressure"):
        xlat = dataset.variables['XLAT'][:,:,:]
        xlong = dataset.variables['XLONG'][:,:,:]
        temperature = []; lat = []; lon = []
        lon = xlong[:1, :,:].squeeze()
        lat = xlat[:1, :, :].squeeze()
        hlat, llat = np.amax(xlat), np.amin(xlat)
        hlong, llong = np.amax(xlong), np.amin(xlong)
        var = dataset.variables['PSFC'][:,:,:].squeeze()
        for i in range(1, len(date)):

            # Settings

            colormap = settings['pressure']['colormap']
            varmax = getHigherValue(var) / 100
            varmin = getLowerValue(var) / 100
            mbar = var[i:i+1,:,:] / 100


            # Plot Setings
            plt.figure(figsize=(18,9))
            title = mapManager.createTitle('pressure', date, i, analysis)
            plt.title(title, 
                        fontsize = 12, 
                        ha = 'left', 
                        x = -0.01)
            plt.suptitle("${mBar}$", 
                        fontsize = 18, 
                        ha = 'center', 
                        x = 0.79, 
                        y = 0.75)
            plt.xlabel('Longitude', 
                        fontsize = 12, 
                        labelpad = 25)
            plt.ylabel('Latitude', 
                        fontsize = 12, 
                        labelpad = 60)

            # Map Settings
            m = mapManager.createMap(llong, hlong, llat, hlat)
            x,y = m(lon, lat)
            m.drawcoastlines()
            m.drawparallels(mapManager.makeParallels(llat, hlat, grade), 
                            linewidth=0, 
                            labels=[1,0,0,1], 
                            color='r', 
                            zorder=0, 
                            fmt="%.2f")
            m.drawmeridians(mapManager.makeMeridians(llong, hlong, grade), 
                            linewidth=0, 
                            labels=[1,0,0,1], 
                            color='r', 
                            zorder=0, 
                            fmt="%.2f")
            m.contourf(x, y, np.squeeze(mbar), 
                            alpha = 0.4, 
                            cmap = colormap, 
                            vmin=varmin, 
                            vmax=varmax)
            m.pcolor(x,y,np.squeeze(mbar), 
                            alpha = 0.4,
                            cmap = colormap, 
                            vmin=varmin, 
                            vmax=varmax)

            # Colorbar Settings
            cb = plt.colorbar(shrink=0.5, pad=0.04)
            cb.ax.tick_params(labelsize=10)

            # plt.show()

            # Log
            
            fileManager.generateLog('pressure', i, grade)
            # Saving Settings
            
            path = fileManager.getSavePath('pressure', grade)
            fileName = fileManager.getSaveFileName('pressure', i, grade)
            
            plt.savefig(path + fileName, bbox_inches='tight')
            plt.close()
        if (dataset):
            dataset.close()
    elif (variable == "wind"):
        xlat = dataset.variables['XLAT'][:,:,:]
        xlong = dataset.variables['XLONG'][:,:,:]
        temperature = []; lat = []; lon = []
        lon = xlong[:1, :,:].squeeze()
        lat = xlat[:1, :, :].squeeze()
        hlat, llat = np.amax(xlat), np.amin(xlat)
        hlong, llong = np.amax(xlong), np.amin(xlong)
        u10 = dataset.variables['U10'][:].squeeze()
        v10 = dataset.variables['V10'][:].squeeze()

        for i in range(1, len(date)):

            # Settings 
            u = u10[i:i+1,:,:].squeeze()
            v = v10[i:i+1,:,:].squeeze()
            varmax = getHigherWindValue(u10, v10)
            varmin = getLowerWindValue(u10, v10)

            # Plot Settings
            fig = plt.figure(figsize=(18,9))
            title = mapManager.createTitle('wind', date, i, analysis)
            plt.title(title, 
                    fontsize = 12, 
                    ha = 'left', 
                    x = -0.01)
            plt.xlabel('Longitude', 
                    fontsize = 12, 
                    labelpad = 25)
            plt.ylabel('Latitude', 
                    fontsize = 12, 
                    labelpad = 60)

            # Map Settings
            m = mapManager.createMap(llong, hlong, llat, hlat)
            
            x,y = m(lon, lat)
            yy = np.arange(0, y.shape[0], 3)
            xx = np.arange(0, x.shape[1], 3)
            speed = np.sqrt(u*u + v*v)
            points = np.meshgrid(yy, xx)

            m.contourf(x, y, np.sqrt(u*u + v*v), 
                            alpha = 0.4, 
                            cmap = 'Blues', 
                            vmin=varmin, 
                            vmax=varmax)

            cs = m.pcolor(x,y,np.squeeze(speed), 
                            alpha = 0.4, 
                            cmap = 'Blues', 
                            vmin=varmin, 
                            vmax=varmax)

            widths = np.linspace(0, 2, xx.size)

            Q = m.quiver(x[points], 
                        y[points], 
                        u[points], 
                        v[points], 
                        scale_units='xy', 
                        width= 0.0035)

            qk = plt.quiverkey(Q, 
                            1.095, 
                            0.78, 
                            2, 
                            r'$2 \frac{m}{s}$',
                           fontproperties={'size': 18}, 
                           labelpos='N')

            m.drawcoastlines(color = '0.15')

            m.drawparallels(mapManager.makeParallels(llat, hlat, grade), 
                            linewidth=0, 
                            labels=[1,0,0,1], 
                            color='r', 
                            zorder=0, 
                            fmt="%.2f")
            m.drawmeridians(mapManager.makeMeridians(llong, hlong, grade), 
                            linewidth=0, 
                            labels=[1,0,0,1], 
                            color='r', 
                            zorder=0, 
                            fmt="%.2f")

            # Colorbar Settings
            cb = plt.colorbar(shrink=0.5, pad=0.04)
            cb.ax.tick_params(labelsize=10)

#            plt.show()

            # Log
            fileManager.generateLog('wind', i, grade)

            # Saving Settings
            path = fileManager.getSavePath('wind', grade)
            fileName = fileManager.getSaveFileName('wind', i, grade)
            
            plt.savefig(path + fileName, bbox_inches='tight')
            plt.close()
    elif (variable == "vapor"):
        xlat = dataset.variables['XLAT'][:,:,:]
        xlong = dataset.variables['XLONG'][:,:,:]
        temperature = []; lat = []; lon = []
        lon = xlong[:1, :,:].squeeze()
        lat = xlat[:1, :, :].squeeze()
        hlat, llat = np.amax(xlat), np.amin(xlat)
        hlong, llong = np.amax(xlong), np.amin(xlong)
        var = dataset.variables['Q2'][:,:,:].squeeze()

        for i in range(1, len(date)):

            # Settings 
            colormap = settings['vapor']['colormap']
            varmax = getHigherValue(var) * 1000
            varmin = getLowerValue(var) * 1000
            gkg = var[i:i+1,:,:] * 1000

            # Plot Settings 
            plt.figure(figsize=(18,9))
            title = mapManager.createTitle('vapor', date, i, analysis)
            plt.title(title, 
                    fontsize = 12, 
                    ha = 'left', 
                    x = -0.01)
            plt.suptitle("$g/kg \frac{m}{s}$", 
                    fontsize = 18, 
                    ha = 'center', 
                    x = 0.79, 
                    y = 0.75)
            plt.xlabel('Longitude', 
                    fontsize = 12, 
                    labelpad = 25)
            plt.ylabel('Latitude', 
                    fontsize = 12, 
                    labelpad = 60)

            # Map Settings
            m = mapManager.createMap(llong, hlong, llat, hlat)
            x,y = m(lon, lat)
            m.drawcoastlines()
            m.drawparallels(mapManager.makeParallels(llat, hlat, grade), 
                            linewidth=0, 
                            labels=[1,0,0,1], 
                            color='r', 
                            zorder=0, 
                            fmt="%.2f")
            m.drawmeridians(mapManager.makeMeridians(llong, hlong, grade), 
                            linewidth=0, 
                            labels=[1,0,0,1], 
                            color='r', 
                            zorder=0, 
                            fmt="%.2f")
            m.contourf(x, y, np.squeeze(gkg), 
                            alpha = 0.4, 
                            cmap = colormap, 
                            vmin=varmin, 
                            vmax=varmax)
            m.pcolor(x,y,np.squeeze(gkg), 
                            alpha = 0.4,
                            cmap = colormap, 
                            vmin=varmin, 
                            vmax=varmax)

            # Colorbar Settings
            cb = plt.colorbar(shrink=0.5, pad=0.04)
            cb.ax.tick_params(labelsize=10)

            # plt.show()

            # Log
            fileManager.generateLog('vapor', i, grade)

            # Saving Settings
            path = fileManager.getSavePath('vapor', grade)
            fileName = fileManager.getSaveFileName('vapor', i, grade)
            
            plt.savefig(path + fileName, bbox_inches='tight')
            plt.close()
    elif (variable == "rain"):
        xlat = dataset.variables['XLAT'][:,:,:]
        xlong = dataset.variables['XLONG'][:,:,:]
        temperature = []; lat = []; lon = []
        lon = xlong[:1, :,:].squeeze()
        lat = xlat[:1, :, :].squeeze()
        hlat, llat = np.amax(xlat), np.amin(xlat)
        hlong, llong = np.amax(xlong), np.amin(xlong)
        var = dataset.variables['Q2'][:,:,:].squeeze()

        for i in range(1, len(date)):

            # Settings 
            colormap = settings['rain']['colormap']
            varmax = getHigherValue(var)
            varmin = getLowerValue(var)
            mm = var[i:i+1,:,:]

            # Plot Settings 
            plt.figure(figsize=(18, 9))
            title = mapManager.createTitle('rain', date, i, analysis)
            plt.title(title, 
                    fontsize = 12, 
                    ha = 'left', 
                    x = -0.01)
            plt.suptitle("$mm$", 
                    fontsize = 18, 
                    ha = 'center', 
                    x = 0.79, 
                    y = 0.75)
            plt.xlabel('Longitude', 
                    fontsize = 12, 
                    labelpad = 25)
            plt.ylabel('Latitude', 
                    fontsize = 12, 
                    labelpad = 60)

            # Map Settings
            m = mapManager.createMap(llong, hlong, llat, hlat)
            x,y = m(lon, lat)
            m.drawcoastlines()
            m.drawparallels(mapManager.makeParallels(llat, hlat, grade), 
                            linewidth=0, 
                            labels=[1,0,0,1], 
                            color='r', 
                            zorder=0, 
                            fmt="%.2f")
            m.drawmeridians(mapManager.makeMeridians(llong, hlong, grade), 
                            linewidth=0, 
                            labels=[1,0,0,1], 
                            color='r', 
                            zorder=0, 
                            fmt="%.2f")
            m.contourf(x, y, np.squeeze(mm), 
                            alpha = 0.4, 
                            cmap = colormap, 
                            vmin=varmin, 
                            vmax=varmax)
            m.pcolor(x,y,np.squeeze(mm), 
                            alpha = 0.4,
                            cmap = colormap, 
                            vmin=varmin, 
                            vmax=varmax)

            # Colorbar Settings
            cb = plt.colorbar(shrink=0.5, pad=0.04)
            cb.ax.tick_params(labelsize=10)

            # plt.show()

            # Log
            fileManager.generateLog('rain', i, grade)

            # Saving Settings
            path = fileManager.getSavePath('rain', grade)
            fileName = fileManager.getSaveFileName('rain', i, grade)
            
            plt.savefig(path + fileName, bbox_inches='tight')
            plt.close()
    if (dataset):
        dataset.close()
    return 0