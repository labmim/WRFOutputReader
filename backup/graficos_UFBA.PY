#!/usr/bin/env python
# -*- coding: cp1252 -*-

import datetime
import numpy as np
import math
import matplotlib.patches as mpatches
import matplotlib.pyplot as ax
import matplotlib.lines as mlines

from PIL import Image,ImageDraw,ImageFont
from pylab import *
from matplotlib import collections, axes, transforms
from matplotlib.colors import colorConverter


# Gerando gráficos atualizados para página
# Precipitacao
if 1:
# arquivo fonte    
    f1 = np.loadtxt ('E:/LABMIM/formatado/LBMUFBA_rain.dat')

# variáveis auxiliares
    dia_mes1= [] #eixo do tempo    
    var_mes1= [] #precipitacao

    cont1 = 0
    d_ini=0
    d_end=0
    for line in f1: 
        cont1=cont1+1
        ano1 = f1[:,0] #ano inteiro
        dia1 = f1[:,6] #dia juliano
        hr1  = f1[:,3] #hora
        min1 = f1[:,4] #minuto
        var1 = f1[:,7] #precipitacao
        
        dj_end    = f1[(cont1-1),6]
        prec_last = f1[(cont1-1),7]
#        print ("cuidado")

# exemplo cmd find
#        if cont1==500:
#            a   = np.array(var1)
#            inds = np.nonzero(a>2)
#            a[inds] 
         
		 
    for i in range(1, cont1):
        iano1 = int(ano1[i])
        idj1  = int(dia1[i])
        ihr1  = float(hr1[i])
        imin1 = float(min1[i])
        ivar1 = float(var1[i])

        d1    = datetime.date(iano1, 1, 1) + datetime.timedelta(idj1 - 1)
		
        dia  = d1.day
        mes  = d1.month
        ano  = d1.year
        hora = int(ihr1)
 #       minut= int((ihr1 - hora)*60)
        minut= int(imin1)
        
        dia_completo = datetime.datetime(iano1,mes,dia,hora,minut)
		
        if i==1:
            d_ini = datetime.date(iano1, 1, 1) + datetime.timedelta(dj_end -7)
            d_end = datetime.date(iano1, 1, 1) + datetime.timedelta(dj_end +0)
             
        delta = datetime.timedelta(hours=6)
        dates = drange(d_ini, d_end, delta)

        dia_mes1.append(dia_completo)
        var_mes1.append(ivar1)
  
    fig = figure(1,figsize=(8.5,4))
    ax = fig.add_subplot(111)

    PL01 = ax.plot_date(dia_mes1, var_mes1,'-',xdate=True,ydate=False, lw=3, color='blue')

    # this is superfluous, since the autoscaler should get it right, but
    # use date2num and num2date to to convert between dates and floats if
    # you want; both date2num and num2date convert an instance or sequence
    ax.set_xlim(d_ini, d_end)
    ax.set_ylim( 0.001, 10)
    ax.xaxis.set_major_locator( DayLocator() )
    ax.xaxis.set_minor_locator( HourLocator(arange(0,25,6)) )
    ax.xaxis.set_major_formatter(DateFormatter('%a\n%b-%d' ))

    ax.fmt_xdata = DateFormatter('%d/%m/%y %H:%M')
    #fig.autofmt_xdate()

    #ax.legend( (TPS1,TPS2,TPS3),  ('DTL','NR','PR'), bbox_to_anchor=(0., 1.02, 1., .702),
    #loc=3,ncol=3, mode="expand", borderaxespad=0.)

    ax.axhline(y=0, lw=1, color='black')

    xlabel('Dia',fontsize=12, horizontalalignment='center',verticalalignment='top')
    ylabel('Precipitação (mm)',fontsize=12, horizontalalignment='center',verticalalignment='center')
 
    text(0.5, 0.55,'LabMiM & LaPO (IF) / LMAC (IM)',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes)
    text(0.5, 0.45,'UFBA',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes) 

    ax.xaxis.grid(True, linestyle='-', which='major', color='grey',alpha=0.5)
    #fig.show()
    savefig('E:/LABMIM/formatado/figuras/precip.png')
    
    


if 2:
    f2 = np.loadtxt ('E:/LABMIM/formatado/LBMUFBA_lenta.dat')
    f3 = np.loadtxt ('E:/LABMIM/formatado/LBMUFBA_irga30.dat')

# variaveis auxiliares 
    dia_mes1= [] #eixo do tempo    
    var_mes1= [] #temperatura
    var_mes2= [] #umidade relativa
    var_mes3= [] #velocidade do vento
    var_mes4= [] #direcao do vento
    var_mes5= [] #radiacao solar
    var_mes6= [] #onda longo atmosfera
    var_mes7= [] #saldo de radiação
    var_mes8= [] #radiacao PAR
  
    dia_mes2= [] #eixo do tempo    
    var_mes10= [] #temperatura
    var_mes11= [] #temperatura
    var_mes12= [] #umidade relativa
    var_mes13= [] #temperatura
    var_mes14= [] #umidade relativa
    var_mes15= [] #umidade relativa   
    var_mes16= [] #umidade relativa 
    var_mes17= [] #umidade relativa     
     
    cont1 = 0
    d_ini=0
    d_end=0
    for line in f2:      
        cont1=cont1+1
        ano1 = f2[:,0] #ano inteiro
        dia1 = f2[:,6] #dia juliano
        hr1  = f2[:,3] #hora
        min1 = f2[:,4] #minuto
        
        var1 = f2[:,20] #temperatura do ar
        var2 = f2[:,21] #umidade relativa
        var3 = f2[:,22] #velocidade do vento
        var4 = f2[:,23] #direcao do vento
        
        var5 = f2[:,10] #radiacao solar
        var6 = f2[:,12] #onda longa atmosfera
        var7 = f2[:,17] #saldo radiacao
        var8 = f2[:,19] #radiacao PAR
                
        dj_end  = f2[(cont1-1),6]
  

    for i in range(1, cont1):
        iano1 = int(ano1[i])
        idj1  = int(dia1[i])
        ihr1  = float(hr1[i])
        imin1 = float(min1[i])
        ivar1 = float(var1[i])
        ivar2 = float(var2[i])
        ivar3 = float(var3[i])
        ivar4 = float(var4[i])
        ivar5 = float(var5[i])
        ivar6 = float(var6[i])
        ivar7 = float(var7[i])
        ivar8 = float(var8[i])

        
        d1    = datetime.date(iano1, 1, 1) + datetime.timedelta(idj1 - 1)
		
        dia  = d1.day
        mes  = d1.month
        ano  = d1.year
        hora = int(ihr1)
        minut= int(imin1)
        dia_completo = datetime.datetime(iano1,mes,dia,hora,minut)

        if i==1:
            d_ini = datetime.date(iano1, 1, 1) + datetime.timedelta(dj_end -7)
            d_end = datetime.date(iano1, 1, 1) + datetime.timedelta(dj_end +0)
             
        delta = datetime.timedelta(hours=6)
        dates = drange(d_ini, d_end, delta)

        dia_mes1.append(dia_completo)
        var_mes1.append(ivar1)
        var_mes2.append(ivar2)        
        var_mes3.append(ivar3)
        var_mes4.append(ivar4)        
        var_mes5.append(ivar5)
        var_mes6.append(ivar6)        
        var_mes7.append(ivar7)
        var_mes8.append(ivar8)        

 
    cont1 = 0
    d_ini=0
    d_end=0
    for line in f3:      
        cont1=cont1+1
        ano2 = f3[:,0] #ano inteiro
        dia2 = f3[:,6] #dia juliano
        hr2  = f3[:,3] #hora
        min2 = f3[:,4] #minuto
        
        var10 = f3[:,7]  #componente zonal u
        var11 = f3[:,8]  #componente meridional v
        var12 = f3[:,9]  #concentração CO2
        var13 = f3[:,10] #concentração vapor de água
        var14 = f3[:,11] #temperatura
        var15 = f3[:,12] #pressao
                
        dj_end  = f3[(cont1-1),6]
  

    for i in range(1, cont1):
        iano2 = int(ano2[i])
        idj2  = int(dia2[i])
        ihr2  = float(hr2[i])
        imin2 = float(min2[i])
        
        ivar10 = float(var10[i])
        ivar11 = float(var11[i])
        ivar12 = float(var12[i])
        ivar13 = float(var13[i])
        ivar14 = float(var14[i])
        ivar15 = float(var15[i])*10

# irgason
# variaveis termodinamicas        
        aux_e2=(ivar13/1000)*(461.5)*(ivar14+273.15);
        aux_es2=611.2*exp(17.67*ivar14/(ivar14+243.5));
        aux_ur2=aux_e2/aux_es2;
        ivar16=((0.622*aux_e2)/((ivar15*100)+(0.622-1)*aux_e2))*1000;
# velocidade vento medio
        ivar17=sqrt(ivar10**2+ivar11**2)
        
        
        d2    = datetime.date(iano2, 1, 1) + datetime.timedelta(idj2 - 1)
		
        dia  = d2.day
        mes  = d2.month
        ano  = d2.year
        hora = int(ihr2)
        minut= int(imin2)
        dia_completo = datetime.datetime(iano2,mes,dia,hora,minut)

        if i==1:
            d_ini = datetime.date(iano2, 1, 1) + datetime.timedelta(dj_end -7)
            d_end = datetime.date(iano2, 1, 1) + datetime.timedelta(dj_end +0)
             
        delta = datetime.timedelta(hours=6)
        dates = drange(d_ini, d_end, delta)

        dia_mes2.append(dia_completo)
        var_mes10.append(ivar10)
        var_mes11.append(ivar11)        
        var_mes12.append(ivar12)
        var_mes13.append(ivar13)        
        var_mes14.append(ivar14)
        var_mes15.append(ivar15)        
        var_mes16.append(ivar16)        
        var_mes17.append(ivar17)

        
# Temperatura do ar        
    fig = figure(2,figsize=(8.5,4))
    ax = fig.add_subplot(111)
    TP01 = ax.plot_date(dia_mes1, var_mes1,'o',xdate=True,ydate=False, lw=1, color='red',label='T')

    # this is superfluous, since the autoscaler should get it right, but
    # use date2num and num2date to to convert between dates and floats if
    # you want; both date2num and num2date convert an instance or sequence
    ax.set_xlim(d_ini, d_end)
    ax.set_ylim( 20, 35)
    ax.xaxis.set_major_locator( DayLocator() )
    ax.xaxis.set_minor_locator( HourLocator(arange(0,25,6)) )
    ax.xaxis.set_major_formatter(DateFormatter('%a\n%b-%d' ))

    ax.fmt_xdata = DateFormatter('%d/%m/%y %H:%M')
    #fig.autofmt_xdate()

    xlabel('Dia',fontsize=12, horizontalalignment='center',verticalalignment='top')
    ylabel('Temperatura do ar (°C)',fontsize=12, horizontalalignment='center',verticalalignment='center')
 
    text(1.,.95,dia_completo,fontsize=10,color='black',horizontalalignment='right',transform = ax.transAxes)
#    text(0.5, 0.55,'LabMiM & LaPO (IF) / LMAC (IM)',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes)

    text(0.5, 0.45,'UFBA',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes) 

    ax.xaxis.grid(True, linestyle='-', which='major', color='grey',alpha=0.5)

    savefig('E:/LABMIM/formatado/figuras/temperatura.png')
    
# Umidade relativa do ar
    fig = figure(3,figsize=(8.5,4))
    ax = fig.add_subplot(111)
    RH01 = ax.plot_date(dia_mes1, var_mes2,'o',xdate=True,ydate=False, lw=4, color='blue',label='2.2m')

    ax.set_xlim(d_ini, d_end)
    ax.set_ylim( 50, 100)
    ax.xaxis.set_major_locator( DayLocator() )
    ax.xaxis.set_minor_locator( HourLocator(arange(0,25,6)) )
    ax.xaxis.set_major_formatter(DateFormatter('%a\n%b-%d' ))

    ax.fmt_xdata = DateFormatter('%d/%m/%y %H:%M')

    xlabel('Dia',fontsize=12, horizontalalignment='center',verticalalignment='top')
    ylabel('Umidade relativa do ar (%)',fontsize=12, horizontalalignment='center',verticalalignment='center')
 
    text(0.5, 0.55,'LabMiM & LaPO (IF) / LMAC (IM)',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes)
    text(0.5, 0.45,'UFBA',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes) 

    ax.xaxis.grid(True, linestyle='-', which='major', color='grey',alpha=0.5)

    savefig('E:/LABMIM/formatado/figuras/umidade_relativa.png')


# velocidade do vento
    fig = figure(4,figsize=(8.5,4))
    ax = fig.add_subplot(111)
    V01 = ax.plot_date(dia_mes1, var_mes3,'-',xdate=True,ydate=False, lw=2, color='black',label='anemometro')
    V02 = ax.plot_date(dia_mes2, var_mes17,'.',xdate=True,ydate=False, lw=3, color='orange',label='sônico')
    
    ax.set_xlim(d_ini, d_end)
    ax.set_ylim( 0, 8)
    ax.xaxis.set_major_locator( DayLocator() )
    ax.xaxis.set_minor_locator( HourLocator(arange(0,25,6)) )
    ax.xaxis.set_major_formatter(DateFormatter('%a\n%b-%d' ))

    ax.fmt_xdata = DateFormatter('%d/%m/%y %H:%M')
    ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=3, mode="expand", borderaxespad=0.)
    ax.axhline(y=0, lw=1, color='black')

    xlabel('Dia',fontsize=12, horizontalalignment='center',verticalalignment='top')
    ylabel('Velocidade do vento (m/s)',fontsize=12, horizontalalignment='center',verticalalignment='center')
 
    text(0.5, 0.55,'LabMiM & LaPO (IF) / LMAC (IM)',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes)
    text(0.5, 0.45,'UFBA',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes) 

    ax.xaxis.grid(True, linestyle='-', which='major', color='grey',alpha=0.5)

    savefig('E:/LABMIM/formatado/figuras/velocidade.png')

# direcao do vento
    fig = figure(5,figsize=(8.5,4))
    ax = fig.add_subplot(111)
    D01 = ax.plot_date(dia_mes1, var_mes4,'*',xdate=True,ydate=False, lw=2, color='black',label='2.2m')

    ax.set_xlim(d_ini, d_end)
    ax.set_ylim( 0, 360)
    ax.xaxis.set_major_locator( DayLocator() )
    ax.xaxis.set_minor_locator( HourLocator(arange(0,25,6)) )
    ax.xaxis.set_major_formatter(DateFormatter('%a\n%b-%d' ))

    ax.fmt_xdata = DateFormatter('%d/%m/%y %H:%M')

    xlabel('Dia',fontsize=12, horizontalalignment='center',verticalalignment='top')
    ylabel('Direção do vento (°)',fontsize=12, horizontalalignment='center',verticalalignment='center')
 
    text(0.5, 0.55,'LabMiM & LaPO (IF) / LMAC (IM)',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes)
    text(0.5, 0.45,'UFBA',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes) 

    ax.xaxis.grid(True, linestyle='-', which='major', color='grey',alpha=0.5)

    savefig('E:/LABMIM/formatado/figuras/direcao.png')

# balanço radiacao
    fig = figure(6,figsize=(8.5,4))
    ax = fig.add_subplot(111)
    SW1 = ax.plot_date(dia_mes1, var_mes5,'v',xdate=True,ydate=False, lw=1, color='red',label='SW_dw')
    LW1 = ax.plot_date(dia_mes1, var_mes6,'.',xdate=True,ydate=False, lw=2, color='orange',label='LW_dw')
    RN1 = ax.plot_date(dia_mes1, var_mes7,'o',xdate=True,ydate=False, lw=1, color='blue',label='Rn')

    ax.set_xlim(d_ini, d_end)
    ax.set_ylim( 0.001, 1300)
    ax.xaxis.set_major_locator( DayLocator() )
    ax.xaxis.set_minor_locator( HourLocator(arange(0,25,6)) )
    ax.xaxis.set_major_formatter(DateFormatter('%a\n%b-%d' ))

    ax.fmt_xdata = DateFormatter('%d/%m/%y %H:%M')

    ax.legend(bbox_to_anchor=(0., 1., 1., .1), loc=3,ncol=3, mode="expand", borderaxespad=0.)
    ax.axhline(y=0, lw=1, color='black')

    xlabel('Dia',fontsize=12, horizontalalignment='center',verticalalignment='top')
    ylabel('Radiação (W/m2)',fontsize=12, horizontalalignment='center',verticalalignment='center')
 
    text(0.5, 0.55,'LabMiM & LaPO (IF) / LMAC (IM)',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes)
    text(0.5, 0.45,'UFBA',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes) 

    ax.xaxis.grid(True, linestyle='-', which='major', color='grey',alpha=0.5)

    savefig('E:/LABMIM/formatado/figuras/radiacao.png')

# radiação PAR
    fig = figure(7,figsize=(8.5,4))
    ax = fig.add_subplot(111)
    D01 = ax.plot_date(dia_mes1, var_mes8,'o',xdate=True,ydate=False, lw=2, color='green',label='2.2m')

    ax.set_xlim(d_ini, d_end)
    ax.set_ylim( 0, 600)
    ax.xaxis.set_major_locator( DayLocator() )
    ax.xaxis.set_minor_locator( HourLocator(arange(0,25,6)) )
    ax.xaxis.set_major_formatter(DateFormatter('%a\n%b-%d' ))

    ax.fmt_xdata = DateFormatter('%d/%m/%y %H:%M')

    xlabel('Dia',fontsize=12, horizontalalignment='center',verticalalignment='top')
    ylabel('Radiação PAR (W/m2)',fontsize=12, horizontalalignment='center',verticalalignment='center')
 
    text(0.5, 0.55,'LabMiM & LaPO (IF) / LMAC (IM)',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes)
    text(0.5, 0.45,'UFBA',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes) 

    ax.xaxis.grid(True, linestyle='-', which='major', color='grey',alpha=0.5)

    savefig('E:/LABMIM/formatado/figuras/radiacao_par.png')
    
# Concentração de CO2
    fig = figure(8,figsize=(8.5,4))
    ax = fig.add_subplot(111)
    D01 = ax.plot_date(dia_mes2, var_mes12,'o',xdate=True,ydate=False, lw=2, color='grey',label='2.2m')

    ax.set_xlim(d_ini, d_end)
    ax.set_ylim( 600, 800)
    ax.xaxis.set_major_locator( DayLocator() )
    ax.xaxis.set_minor_locator( HourLocator(arange(0,25,6)) )
    ax.xaxis.set_major_formatter(DateFormatter('%a\n%b-%d' ))

    ax.fmt_xdata = DateFormatter('%d/%m/%y %H:%M')

    xlabel('Dia',fontsize=12, horizontalalignment='center',verticalalignment='top')
    ylabel('Concentração CO2 (mg/m3)',fontsize=12, horizontalalignment='center',verticalalignment='center')
 
    text(0.5, 0.55,'LabMiM & LaPO (IF) / LMAC (IM)',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes)
    text(0.5, 0.45,'UFBA',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes) 

    ax.xaxis.grid(True, linestyle='-', which='major', color='grey',alpha=0.5)

    savefig('E:/LABMIM/formatado/figuras/co2.png')
    
# Pressão atmosférica
    fig = figure(9,figsize=(8.5,4))
    ax = fig.add_subplot(111)
    D01 = ax.plot_date(dia_mes2, var_mes15,'*',xdate=True,ydate=False, lw=2, color='blue',label='2.2m')

    ax.set_xlim(d_ini, d_end)
    ax.set_ylim( 1000, 1030)
    ax.xaxis.set_major_locator( DayLocator() )
    ax.xaxis.set_minor_locator( HourLocator(arange(0,25,6)) )
    ax.xaxis.set_major_formatter(DateFormatter('%a\n%b-%d' ))

    ax.fmt_xdata = DateFormatter('%d/%m/%y %H:%M')

    xlabel('Dia',fontsize=12, horizontalalignment='center',verticalalignment='top')
    ylabel('Pressão atmosférica (hPa)',fontsize=12, horizontalalignment='center',verticalalignment='center')
 
    text(0.5, 0.55,'LabMiM & LaPO (IF) / LMAC (IM)',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes)
    text(0.5, 0.45,'UFBA',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes) 

    ax.xaxis.grid(True, linestyle='-', which='major', color='grey',alpha=0.5)

    savefig('E:/LABMIM/formatado/figuras/pressao.png')    
    
# Umidade específica
    fig = figure(10,figsize=(8.5,4))
    ax = fig.add_subplot(111)
    D02 = ax.plot_date(dia_mes2, var_mes16,'o',xdate=True,ydate=False, lw=2, color='green',label='irgason')

    ax.set_xlim(d_ini, d_end)
    ax.set_ylim( 10, 25)
    ax.xaxis.set_major_locator( DayLocator() )
    ax.xaxis.set_minor_locator( HourLocator(arange(0,25,6)) )
    ax.xaxis.set_major_formatter(DateFormatter('%a\n%b-%d' ))

    ax.fmt_xdata = DateFormatter('%d/%m/%y %H:%M')

    xlabel('Dia',fontsize=12, horizontalalignment='center',verticalalignment='top')
    ylabel('Umidade específica (g/kg)',fontsize=12, horizontalalignment='center',verticalalignment='center')
 
    text(0.5, 0.55,'LabMiM & LaPO (IF) / LMAC (IM)',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes)
    text(0.5, 0.45,'UFBA',fontsize=16,color='#CFCFCF',horizontalalignment='center',transform = ax.transAxes) 

    ax.xaxis.grid(True, linestyle='-', which='major', color='grey',alpha=0.5)

    savefig('E:/LABMIM/formatado/figuras/umidade_especifica.png')    