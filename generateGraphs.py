import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections, axes, transforms
import netCDF4
from os import listdir
from datetime import datetime, timedelta
from mpl_toolkits.basemap import Basemap
from matplotlib import ticker
import matplotlib as mpl
import arrow

from correctFileName import CorrectNumberInFileName
from timeLoader import date, analysis
from settings import settings
import fileManager
import mapManager
#import coordenatesManager
#from settings import settings
#import settings

#import Utilities as utils

"""

    As variáveis de tempo vão estar disponíveis
    As variáveis do dataset vão estar disponíveis


"""
time = settings['time']
dataset = netCDF4.Dataset(fileManager.getTodayFilePath())

# /*
#   A partir da grade, define determinadas configurações da projeção do mapa
# */

grade = fileManager.getGradeSize()

def makeMeridians(grade):
    if (grade == "d01"):
        return np.arange(llong, hlong, 1.3)
    elif (grade == "d02"):
        return np.arange(llong, hlong, 0.13)
    else:
        return np.arange(-38.7334, -38.2808, 0.07)
def makeParallels(grade):
    if (grade == "d01"):
        return np.arange(llat, hlat, 1.1)
    elif (grade == "d02"):
        return np.arange(llat, hlat, 0.09)
    else:
        return np.arange(-13.1336, -12.6928, 0.06)

xlat = dataset.variables['XLAT'][:,:,:]
xlong = dataset.variables['XLONG'][:,:,:]
temperature = []; lat = []; lon = []
lon = xlong[:1, :,:].squeeze()
lat = xlat[:1, :, :].squeeze()
hlat, llat = np.amax(xlat), np.amin(xlat)
hlong, llong = np.amax(xlong), np.amin(xlong)

#lon2 = coordenatesManager.getLongitude()
#lat2 = coordenatesManager.getLatitude()
#hlat2, llat = coordenatesManager.getMaxMinFromLatitude()
#hlong, llong = coordenatesManager.getMaxMinFromLongitude() 

def getLowerValue(variable):
    varflat = variable.flatten()
    varlow = np.amin(varflat)
    print(varlow)
    return varlow


def getHigherValue(variable):
    varflat = variable.flatten()
    varhigh = np.amax(varflat)
    print(varhigh)
    return varhigh

def getLowerWindValue(variable, variable2):
    var1flat = variable.flatten()
    var2flat = variable2.flatten()
    speedflat = np.sqrt(var1flat*var1flat + var2flat*var2flat)
    varlow = np.amin(speedflat)
    print(varlow)
    return varlow

def getHigherWindValue(variable, variable2):
    var1flat = variable.flatten()
    var2flat = variable2.flatten()
    speedflat = np.sqrt(var1flat*var1flat + var2flat*var2flat)
    varhigh = np.amax(speedflat)
    print(varhigh)
    return varhigh

def generateGraphs(variable, token = 0):
    
    if (variable == "temperature"):        
        var = dataset.variables['T2'][:,:,:].squeeze()
        # Necessário consertar o path do arquivo salvo
            
        for i in range(1, len(date)):
            
            # Settings
            
            varmax = getHigherValue(var) - 273.15
            varmin = getLowerValue(var) - 273.15
            celcius = var[i:i+1,:,:] - 273.15 
            colormap = settings['temperature']['colormap']  
            
            # Plot Settings
            
            plt.figure(figsize=(18,9))
            title = mapManager.createTitle('temperature', i)
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
            m.drawparallels(makeParallels(grade), 
                            linewidth=0, 
                            labels=[1,0,0,1], 
                            color='r', 
                            zorder=0, 
                            fmt="%.2f")
            m.drawmeridians(makeMeridians(grade), 
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
            plt.savefig('/Users/nicolasdecordi/Nicolas/WRFOutputReader/output/d03_2017-03-11/Temperatura/' + CorrectNumberInFileName(i) + '.png', bbox_inches='tight')
            #plt.savefig(mapManager.getSavePath('temperature', i), bbox_inches='tight')
            plt.close()
        if (dataset):
            dataset.close()
            
    elif (variable == "Pressure"):
        var = dataset.variables['PSFC'][:,:,:].squeeze()

        for i in range(1, 97):
            forecast = date[i].format(time['format'], locale=time['locale'])
            title = " " + model + " — " + lab + "\n Início Análise: " + analysis + " (UTC)"+ "\n Previsão: " + forecast + " HL"

            colormap = settings['pressure']['colormap']
            varmax = getHigherValue(var) / 100
            varmin = getLowerValue(var) / 100
            print(varmax, varmin)
            plt.figure(figsize=(18,9))
            m = Basemap(rsphere=(6378137.00,6356752.3142),\
                    resolution='h',area_thresh=0.1,projection='merc',\
                    llcrnrlon= llong, llcrnrlat= llat,
                    urcrnrlon= hlong, urcrnrlat= hlat)
            x,y = m(lon, lat)
            fix = var[i:i+1,:,:] / 100
            m.contourf(x, y, np.squeeze(fix), alpha = 0.4, cmap = colormap)#, vmin=varmin, vmax=varmax)
            m.pcolor(x,y,np.squeeze(fix), alpha = 0.4,cmap = colormap)#, vmin=varmin, vmax=varmax)
            #cbar = m.colorbar(cs, location='right')
            #cNorm = mpl.colors.Normalize(vmin=varmin, vmax=varmax)
            #cs.set_norm(cNorm)
            cb = plt.colorbar(shrink=0.5, pad=0.04)
            cb.ax.tick_params(labelsize=10)
            cb.set_label('Pressão', fontsize = 10, labelpad = 10)
            m.drawcoastlines()
            m.drawparallels(np.arange(-13.1336, -12.6928, 0.06), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f")
            m.drawmeridians(np.arange(-38.7334, -38.2808, 0.07), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f" )
            plt.title(title, fontsize = 12, ha = 'left', x = -0.01)
            plt.suptitle("$\mathrm{mBar}$", fontsize = 18, ha = 'center', x = 0.79, y = 0.75)
            plt.xlabel('Longitude', fontsize = 12, labelpad = 25)
            plt.ylabel('Latitude', fontsize = 12, labelpad = 60)
            plt.show()
            plt.close()
        if (dataset):
            dataset.close()
    elif (variable == "Wind"):
        u10 = dataset.variables['U10'][:].squeeze()
        v10 = dataset.variables['V10'][:].squeeze()

        for i in range(1, 97):
            forecast = date[i].format(time['format'], locale=time['locale'])
            title = " " + model + " — " + lab + "\n Início Análise: " + analysis + " (UTC)"+ "\n Previsão: " + forecast + " HL" + " — " + "Velocidade do Vento (10 m)"
            u = u10[i:i+1,:,:].squeeze()
            v = v10[i:i+1,:,:].squeeze()

            varmax = getHigherWindValue(u10, v10)
            varmin = getLowerWindValue(u10, v10)
            print(varmax, varmin)
            fig = plt.figure(figsize=(18,9))
            m = Basemap(rsphere=(6378137.00,6356752.3142),\
                        resolution='h',area_thresh=0.1,projection='merc',\
                        llcrnrlon= llong, llcrnrlat= llat,
                        urcrnrlon= hlong, urcrnrlat= hlat)
            #m.fillcontinents(lake_color='aqua')
            #m.drawcoastlines()
            x,y = m(lon, lat)

#            yy = np.arange(0, y.shape[0], 2)
#            xx = np.arange(0, x.shape[1], 2)
            yy = np.arange(0, y.shape[0], 3)
            xx = np.arange(0, x.shape[1], 3)
            speed = np.sqrt(u*u + v*v)
            points = np.meshgrid(yy, xx)

            m.contourf(x, y, np.sqrt(u*u + v*v), alpha = 0.4, cmap = 'Blues', vmin=varmin, vmax=varmax)
            #m.barbs(x[points], y[points], u[points], v[points])
            cs = m.pcolor(x,y,np.squeeze(speed), alpha = 0.4, cmap = 'Blues', vmin=varmin, vmax=varmax)
            #plt.figure(1)
            #plt.grid(True)
        #    m.colorbar()
            #cbar = m.colorbar(cmap = mpl.cm.cool, location='right', pad="5%")
            #cbar = m.colorbar(cs, location='right', pad="5%")
            #cmap = plt.get_cmap('jet_r')
            #cmap_r = reverse_colourmap(cmap)
#            cNorm = mpl.colors.Normalize(vmin=0, vmax=12)
#            cs.set_norm(cNorm)
#            plt.colorbar(norm=cNorm, shrink=0.5)
            widths = np.linspace(0, 2, xx.size)
        #    m.quiver(x[points], y[points],
        #    u[points], v[points], speed[points],
        #    cmap=plt.cm.autumn)
            #Q = m.quiver(x, y, u, v, scale_units='xy', linewidths=widths)
                #cmap=plt.cm.gray, scale=700)
            Q = m.quiver(x[points], y[points], u[points], v[points], scale_units='xy', width= 0.0035) #0.0035
            qk = plt.quiverkey(Q, 1.095, 0.78, 2, r'$2 \frac{m}{s}$',
                           fontproperties={'size': 18}, labelpos='N')
            #m.plot(x, y, 'bo', markersize=1, color='black')
            #m.contourf(x, y, np.sqrt(u*u + v*v), alpha = 0.4)
            m.drawcoastlines(color = '0.15')
#            hora = i - 3
#            plt.title("Velocidade do Vento a 10 metros " + (str(hora)) + ":00 Local", y=1.04)
#            plt.xlabel('Longitude')
#            plt.ylabel('Latitude')
            #plt.title("Wind - Hour " + str(i))
            cb = plt.colorbar(shrink=0.5, pad=0.04)
            cb.ax.tick_params(labelsize=10)
            #cb.set_label('Velocidade do Vento', fontsize = 10, labelpad = 10)
            m.drawcoastlines()
            m.drawparallels(np.arange(-13.1336, -12.6928, 0.06), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f")
            m.drawmeridians(np.arange(-38.7334, -38.2808, 0.07), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f" )
#            m.drawparallels(np.arange(llat, hlat, 0.09), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f")
#            m.drawmeridians(np.arange(llong, hlong, 0.13), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f" )
#            m.drawparallels(np.arange(llat, hlat, 1.1), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f")
#            m.drawmeridians(np.arange(llong, hlong, 1.3), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f" )
            plt.title(title, fontsize = 12, ha = 'left', x = -0.01)
            plt.xlabel('Longitude', fontsize = 12, labelpad = 25)
            plt.ylabel('Latitude', fontsize = 12, labelpad = 60)
            plt.savefig('/Users/nicolasdecordi/Nicolas/WRFOutputReader/output/d03_2017-03-11/Vento/' + CorrectNumberInFileName(i) + '.png', bbox_inches='tight')
#            plt.show()
            plt.close()
    elif (variable == "Vapor"):
        var = dataset.variables['Q2'][:,:,:].squeeze()

        for i in range(1, 97):
            forecast = date[i].format(time['format'], locale=time['locale'])
            title = " " + model + " — " + lab + "\n Início Análise: " + analysis + " (UTC)"+ "\n Previsão: " + forecast + " HL" " — " + "Umidade Específica"

            colormap = settings['water_vapor']['colormap']
            varmax = getHigherValue(var) * 1000
            varmin = getLowerValue(var) * 1000
            print(varmax, varmin)
            plt.figure(figsize=(18,9))
            m = Basemap(rsphere=(6378137.00,6356752.3142),\
                    resolution='h',area_thresh=0.1,projection='merc',\
                    llcrnrlon= llong, llcrnrlat= llat,
                    urcrnrlon= hlong, urcrnrlat= hlat)
            x,y = m(lon, lat)
            fix = var[i:i+1,:,:] * 1000
            m.contourf(x, y, np.squeeze(fix), alpha = 0.4, cmap = colormap, vmin=varmin, vmax=varmax)
            m.pcolor(x,y,np.squeeze(fix), alpha = 0.4,cmap = colormap, vmin=varmin, vmax=varmax)
            #cbar = m.colorbar(cs, location='right')
            #cNorm = mpl.colors.Normalize(vmin=varmin, vmax=varmax)
            #cs.set_norm(cNorm)
            cb = plt.colorbar(shrink=0.5, pad=0.04)
            cb.ax.tick_params(labelsize=10)
            #cb.set_label('Umidade', fontsize = 10, labelpad = 10)
            m.drawcoastlines()
#            m.drawparallels(np.arange(llat, hlat, 1.1), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f")
#            m.drawmeridians(np.arange(llong, hlong, 1.3), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f" )
#            m.drawparallels(np.arange(-13.1336, -12.6928, 0.06), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f")
#            m.drawmeridians(np.arange(-38.7334, -38.2808, 0.07), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f" )
#            m.drawparallels(np.arange(llat, hlat, 0.06), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f")
#            m.drawmeridians(np.arange(llong, hlong, 0.07), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f" )
            m.drawparallels(np.arange(llat, hlat, 0.09), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f")
            m.drawmeridians(np.arange(llong, hlong, 0.13), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f" ) 
            plt.title(title, fontsize = 12, ha = 'left', x = -0.01)
            plt.suptitle("$g/kg \frac{m}{s}$", fontsize = 18, ha = 'center', x = 0.79, y = 0.75)
            plt.xlabel('Longitude', fontsize = 12, labelpad = 25)
            plt.ylabel('Latitude', fontsize = 12, labelpad = 60)
#            plt.show()
            plt.savefig('/Users/nicolasdecordi/Nicolas/WRFOutputReader/output/d03_2017-03-11/Umidade/' + CorrectNumberInFileName(i) + '.png', bbox_inches='tight')

            plt.close()
        if (dataset):
            dataset.close()
    return 0;

##generateGraphs("Temperature")
#var = dataset.variables['T2'][:,:,:].squeeze()
#
#def generateGraph(variable):
#    colormap = settings['temperature']['colormap']
#    varmax = getHigherValue(var) - 273.15
#    varmin = getLowerValue(var) - 273.15
#    print(varmax, varmin)
#    forecast = date[15].format(time['format'], locale=time['locale'])
#    title = " " + model + " — " + lab + "\n Início Análise: " + analysis + " (UTC)"+ "\n Previsão: " + forecast + " HL"
#    plt.figure(figsize=(18,9))
#    m = Basemap(rsphere=(6378137.00,6356752.3142),\
#            resolution='h',area_thresh=0.1,projection='merc',\
#            llcrnrlon= llong, llcrnrlat= llat,
#            urcrnrlon= hlong, urcrnrlat= hlat)
#    x,y = m(lon, lat)
#    fix = var[15:15+1,:,:] - 273.15
#    m.contourf(x, y, np.squeeze(fix), alpha = 0.4, cmap = colormap)
#    cs = m.pcolor(x,y,np.squeeze(fix), alpha = 0.4,cmap = colormap)#, vmin=(291 - 273.15), vmax=(304  - 273.15))
#    #cbar = m.colorbar(cs, location='right')
#    cNorm = mpl.colors.Normalize(vmin=varmin, vmax=varmax)
#    #cs.set_norm(cNorm)
#    cb = plt.colorbar(norm=cNorm, shrink=0.5, pad=0.04)
#    cb.ax.tick_params(labelsize=10)
#    cb.set_label('Temperatura', fontsize = 10, labelpad = 10)
##m.fillcontinents(lake_color='aqua')
#    m.drawcoastlines()
#    m.drawparallels(np.arange(-13.1336, -12.6928, 0.06), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f")
#    m.drawmeridians(np.arange(-38.7334, -38.2808, 0.07), linewidth=0, labels=[1,0,0,1], color='r', zorder=0, fmt="%.2f" )
#    plt.title(title, fontsize = 12, ha = 'left', x = -0.01)
#    plt.suptitle("$^\circ\mathcal{C}$", fontsize = 16, ha = 'center', x = 0.79, y = 0.75)
#    plt.xlabel('Longitude', fontsize = 12, labelpad = 25)
#    plt.ylabel('Latitude', fontsize = 12, labelpad = 60)
#    plt.show()
#    if (dataset):
#        dataset.close()
#
generateGraphs('temperature')
