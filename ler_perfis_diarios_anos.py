
"""
Importando Bibliotecas Necessárias
 
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

"""
DataFrames Anuais Salvos e seus respectivos Shapes.
dataframe2012 - (20418, 780)
dataframe2013 - (33528, 771)
dataframe2014 - (8873, 720) 
dataframe2015 - (49468, 737)
dataframe2016 - (34833, 712)
dataframe2017 - (33899, 705)

""" 
#Lendo os DataFrames Anuais diretamente do HD
panda = pd.read_pickle("C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/DataFrames_anuais/dataframe2014.pkl")
panda_media = panda.mean(axis = 1) #média de todos os sensores 


inicio=dt.date(2014, 1, 6) #primeiro dia da semana ou fim de semana do ano (alterável)
fim=dt.date(2014, 12, 31) #último dia do ano (constante)


tab=[] #lista que irá amarzenar, por exemplo, todas as segundas-feiras do ano.
for i in range(0,(fim-inicio).days, 7): #laço que preencherá a lista tab com todos os dias que se quiser.
    tab.append(str("{:%Y%m%d}".format(inicio + dt.timedelta(days=i))))

"""
cada componente da lista mat será um array (uma segunda-feira, por exemplo), em que nesse array terão 96 valores 
de fluxo de carros.
O total de componentes da lista mat (seu shape) corresponde à 52, ou seja, 52 segundas-feiras no ano.

"""
mat=[] 
for i in tab:
    try:
        mat.append(panda_media[i].values)
    except KeyError:
        print("A seguinte data ", i, "não tem nos dados")



"""
Há dias do ano em que não há os 96 valores de fluxo de carros. Alguns dias apresentam shape (92,), ou seja,
faltam 4 valores. 
Para esses dias, foi adicionado "nan" para que no final todos os 52 dias tenham o mesmo shape.

"""    
for i in range(len(mat)):
    nans = []
    if len(mat[i]) != 96:
        
        dif = 96 - len(mat[i])
        for j in range(dif):
            nans.append(np.nan)
    mat[i] = np.append(mat[i], nans)
        
#testando se todos os arrays apresentam o mesmo shape
shapes = []
for i in range(len(mat)):
    shapes.append(mat[i].shape)
    
""" 
DIAS DA SEMANA sendo salvos
arrays shapes (52, 92) 
"""
array_domingos_horarios_2016 = np.stack(mat)
array_segundas_horarios_2016 = np.stack(mat)
array_tercas_horarios_2016 = np.stack(mat)
array_quartas_horarios_2016 = np.stack(mat)
array_quintas_horarios_2016 = np.stack(mat)
array_sextas_horarios_2016 = np.stack(mat)
array_sabados_horarios_2016 = np.stack(mat)    

np.save('C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/perfis_dia_da_semana/2016/array_domingos_horarios_2016.npy', array_domingos_horarios_2016)  
np.save('C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/perfis_dia_da_semana/2016/array_segundas_horarios_2016.npy', array_segundas_horarios_2016)  
np.save('C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/perfis_dia_da_semana/2016/array_tercas_horarios_2016.npy', array_tercas_horarios_2016) 
np.save('C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/perfis_dia_da_semana/2016/array_quartas_horarios_2016.npy', array_quartas_horarios_2016)    
np.save('C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/perfis_dia_da_semana/2016/array_quintas_horarios_2016.npy', array_quintas_horarios_2016)     
np.save('C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/perfis_dia_da_semana/2016/array_sextas_horarios_2016.npy', array_sextas_horarios_2016)    
np.save('C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/perfis_dia_da_semana/2016/array_sabados_horarios_2016.npy', array_sabados_horarios_2016)    


""" 
DIAS DA SEMANA sendo carregados
PRESTE ATENCAO NO ANO SEU ANIMAL! s2
arrays shapes (52, 92) 
"""
array_domingos_horarios = np.load("C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/perfis_dia_da_semana/2016/array_domingos_horarios_2016.npy")
array_segundas_horarios = np.load("C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/perfis_dia_da_semana/2016/array_segundas_horarios_2016.npy")
array_tercas_horarios = np.load("C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/perfis_dia_da_semana/2016/array_tercas_horarios_2016.npy")
array_quartas_horarios = np.load("C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/perfis_dia_da_semana/2016/array_quartas_horarios_2016.npy")
array_quintas_horarios = np.load("C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/perfis_dia_da_semana/2016/array_quintas_horarios_2016.npy")
array_sextas_horarios = np.load("C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/perfis_dia_da_semana/2016/array_sextas_horarios_2016.npy")
array_sabados_horarios = np.load("C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/perfis_dia_da_semana/2016/array_sabados_horarios_2016.npy")

     
           
"""
PLOTANDO OS PERFIS DIÁRIOS

"""   
#obtendo a lista de horas do dia em 3 em 3 horas para nomear o eixo x
delta = dt.timedelta(hours = 3)
lista_de_horas_dia = ['00:00']

for i in range(0, 24, 3):
    time = dt.time(i,0)
    horas = (dt.datetime.combine(dt.date(1,1,1),time) + delta).time()
    horas = horas.strftime("%H:%M")
    lista_de_horas_dia.append(horas)    
 
""" 

UM A UM
 
"""
 

#DOMINGO           
plt.plot(np.nanmean(array_domingos_horarios, axis=0), linewidth = 2)
plt.xticks(range(0, 96, 12), lista_de_horas_dia)
plt.xlabel('Horas', fontsize=13)
plt.ylabel('Volume de tráfego', fontsize=14)
plt.title("Perfil do Domingo do ano 2016", fontsize=15)
plt.legend(['Domingo'])

#SEGUNDA
plt.plot(np.nanmean(array_segundas_horarios, axis=0), linewidth = 2)
plt.xticks(range(0, 96, 12), lista_de_horas_dia)
plt.xlabel('Horas', fontsize=13)
plt.ylabel('Volume de tráfego', fontsize=14)
plt.title("Perfil da Segunda-feira do ano 2016", fontsize=15)
plt.legend(['Segunda'])

#TERÇA
plt.plot(np.nanmean(array_tercas_horarios, axis=0), linewidth = 2)
plt.xticks(range(0, 96, 12), lista_de_horas_dia)
plt.xlabel('Horas', fontsize=13)
plt.ylabel('Volume de tráfego', fontsize=14)
plt.title("Perfil da Terça-feira do ano 2016", fontsize=15)
plt.legend(['Terça'])

#QUARTA
plt.plot(np.nanmean(array_quartas_horarios, axis=0), linewidth = 2)
plt.xticks(range(0, 96, 12), lista_de_horas_dia)
plt.xlabel('Horas', fontsize=13)
plt.ylabel('Volume de tráfego', fontsize=14)
plt.title("Perfil da Quarta-feira do ano 2016", fontsize=15)
plt.legend(['Quarta'])

#QUINTA
plt.plot(np.nanmean(array_quintas_horarios, axis=0), linewidth = 2)
plt.xticks(range(0, 96, 12), lista_de_horas_dia)
plt.xlabel('Horas', fontsize=13)
plt.ylabel('Volume de tráfego', fontsize=14)
plt.title("Perfil da Quinta-feira do ano 2016", fontsize=15)
plt.legend(['Quinta'])

#SEXTA
plt.plot(np.nanmean(array_sextas_horarios, axis=0), linewidth = 2)
plt.xticks(range(0, 96, 12), lista_de_horas_dia)
plt.xlabel('Horas', fontsize=13)
plt.ylabel('Volume de tráfego', fontsize=14)
plt.title("Perfil da Sext-feira do ano 2016", fontsize=15)
plt.legend(['Sexta'])


#SABADO
plt.plot(np.nanmean(array_sabados_horarios, axis=0), linewidth = 2)
plt.xticks(range(0, 96, 12), lista_de_horas_dia)
plt.xlabel('Horas', fontsize=13)
plt.ylabel('Volume de tráfego', fontsize=14)
plt.title("Perfil do Sábado do ano 2016", fontsize=15)
plt.legend(['Sábado'])



""" 

TUDIN DUMA LAPADA SÓ
 
"""

#DOMINGO           
plt.plot(np.nanmean(array_domingos_horarios, axis=0), linewidth = 2)
#SEGUNDA
plt.plot(np.nanmean(array_segundas_horarios, axis=0), linewidth = 2)
#TERCA
plt.plot(np.nanmean(array_tercas_horarios, axis=0), linewidth = 2)
#QUARTA
plt.plot(np.nanmean(array_quartas_horarios, axis=0), linewidth = 2)
#QUINTA
plt.plot(np.nanmean(array_quintas_horarios, axis=0), linewidth = 2)
#SEXTA
plt.plot(np.nanmean(array_sextas_horarios, axis=0), linewidth = 2)
#SABADO
plt.plot(np.nanmean(array_sabados_horarios, axis=0), linewidth = 2)


#Detalhes do gráfico (eixos, legenda)
plt.xticks(range(0, 96, 12), lista_de_horas_dia)
plt.xlabel('Horas', fontsize=13)
plt.ylabel('Volume de tráfego', fontsize=14)
plt.title("Perfil Médio de Tráfego dos dias da semana do ano 2016", fontsize=15)
plt.legend(['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'])




array_segundas_horarios_2014 = np.stack(mat)

#SEGUNDA 2016
plt.plot(np.nanmean(array_segundas_horarios, axis=0), linewidth = 2)
#SEGUNDA 2014
plt.plot(np.nanmean(array_segundas_horarios_2014, axis=0), linewidth = 2)