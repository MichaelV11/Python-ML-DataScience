import pandas as pd
import numpy as np  #def remove_negative_value(df,colum):

df = pd.read_csv("tratamiento_datos.csv", index_col = 0)
print(df)
print(df.describe()) #nos describe para columnas con numeros la cantidad total de datos, min, max, la media, etc
print(df.info()) #nos describe para todas las columnas la cantidad de datos totales y el tipo de dato(dtypes: int,object,etc) 

#Conocer cuantas categorias tenemos en cada columna (de 7 columnas pero usaremos las categorias con letras)
#Set sirve para imprimir valores de la lista no repetidos (coleciones desordenadas de objetos únicos)

set_gen = set(df["Género"].to_list()) #de la tabla general "df" sacamos solo la columna Género
set_edu = set(df["Nivel_Educación"].to_list())
set_ciu = set(df["Ciudad"].to_list())
#print(set_gen)
#print(set_edu)
#print(set_ciu)

#Proceder al tratamiento de datos (arreglar los datos para que sean coherentes)

#1. Tratamiento de datos negativos 


