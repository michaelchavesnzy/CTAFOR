
"""
Importando Bibliotecas Necessárias
 
"""

from pandas import DataFrame
import pandas as pd
import numpy as np
from dbfread import DBF, FieldParser, InvalidValue
import os

#endereço do local das planilhas
path = r"C:\Users\MICHAEL\Desktop\CTAFOR\Dados_Anuais_Scoot_todas_as_variaveis\Dados Transcoot_todos os links 2017"
#seleciondo o arquivo (planilha)
file = os.listdir(os.path.join(path))
#lista que receberá todos os nomes das planilhas
files = []

#preenchendo a lista files com os nomes das planilhas
for f in file:
    if f.endswith('.xls'):
        files.append(f)
        
dicionario={}


"""
O trecho de código abaixo (da linha 29 à linha 61 ou comentário "início" e "fim") é responsável pela
leitura das planilhas, independente de erros (por causa da classe MyFielParser) e salvando todos os FLOW_M
num dicionário
"""
#início

class MyFieldParser(FieldParser): 
    def parse(self, field, data):
        try:
            return FieldParser.parse(self, field, data)
        except ValueError:
            return InvalidValue(data)
        


for f1 in files:
    print(f1)
    dbf = DBF(f1, parserclass=MyFieldParser)
    for i, record in enumerate(dbf):
        for name, value in record.items():
            if isinstance(value, InvalidValue):
                print('records[{}][{!r}] == {!r}'.format(i, name, value))

    frame_global = DataFrame(iter(dbf))
    di={}
    
    try:
        for i in range(np.shape(frame_global['FLOW_M'].tolist())[0]):  
            if i%10000==0  : 
                print(i)
            di[frame_global['DATA'][i],frame_global['HORA_I'][i]]=frame_global['FLOW_M'][i]
            
        dicionario[f1]=di  
        
    except KeyError:
        print("Arquivo dando erro! Será preenchido com NaN!")
        
 #fim       
        
    
"""
Convertendo o dicionário em DataFrames e organizando em dias crescentes do ano.
O DataFrame está organizado da seguinte forma:
    
Nas linhas tem todos os dias do ano, em ordem crescente (15 em 15 minutos), e nas colunas
são todos os sensores do seu respectivo ano
"""  
panda = pd.DataFrame(dicionario) 
panda = panda.sort_index(level = 0)  

panda2 = pd.DataFrame(dicionario) 
panda2 = panda2.sort_index(level = 0)

panda3 = pd.concat([panda,panda2])  #concatenando 2 dataframes


"""
Salvando os dataframes no HD
"""
panda = pd.read_pickle("./dataframe2017.pkl")

panda3 = pd.read_pickle("./dataframe2015.pkl")

