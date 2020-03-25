# -*- coding: utf-8 -*-

#2012 - 3% de nans
#2013 - 4% de nans
#2014 - 5% de nans
#2015 - 48% de nans
#2016 - 14% de nans OK!!!
#2017 - 26% de nans OK!!!


import pickle
import pandas as pd
import numpy as np
import os

##gerando df a partir do arquivo que contém todos os sensores do trecho aldeota em csv
sensores_aldeota = pd.read_csv(r"C:\Users\MICHAEL\Desktop\CTAFOR\Bloco Aldeota\sensores_aldeota.txt", delimiter = ";")
##obter somente a coluna "Nome do sensor" do df acima 
serie_sensores = sensores_aldeota["Nome Sensor"]
##converter a serie acima em lista
lista_sensores = serie_sensores.tolist()


##camimnho dos dataframes anuais de todos os sensores. OBS: importante alterar dependendo de onde for rodar
path = ("C:/Users/MICHAEL/Desktop/CTAFOR/objetos_salvos/DataFrames_anuais")

#lista com todos os arquivos do diretório dataframes_anuais
lista_todos_arquivos = os.listdir(path)

#lista que receberá somente o nome dos dataframes anuais de todos os sensores
nome_lista_df = []

#iteração para obter somente os arquivos com final .pkl, representando somente os df mencionados acima.
for file in lista_todos_arquivos:
    if file.endswith(".pkl"):
        nome_lista_df.append(file)
        
#interção que abre os dataframes anuais de todos os sensores e filtra somente os sensores da aldeota e por mim salva os df filtrados.
for name in nome_lista_df: 
    ## os.path.join(path + "/", name)
    panda = pd.read_pickle(os.path.join(path + "/", name))
    panda_filtrado = panda.ix[:, lista_sensores]
    panda_filtrado.to_pickle(path + "/" "filtrado" + name) ##checar onde irá salvar os df filtrados
    
## OS 16 Sensores foram localizados nos respectivos dataframes com todos os sensores

##abrindo os dataframes filtrados (checar caminho)      
panda2012filtrado = pd.read_pickle("./filtradodataframe2012.pkl")
panda2013filtrado = pd.read_pickle("./filtradodataframe2013.pkl")    
panda2014filtrado = pd.read_pickle("./filtradodataframe2014.pkl")
panda2015filtrado = pd.read_pickle("./filtradodataframe2015.pkl")
panda2016filtrado = pd.read_pickle("./filtradodataframe2016.pkl")
panda2017filtrado = pd.read_pickle("./filtradodataframe2017.pkl")
