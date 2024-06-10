import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'key': ['K0', 'K1', 'K0', 'K1']
})

df2 = pd.DataFrame({
    'C': ['C0', 'C1'],
    'D': ['D0', 'D1']},
    index=['K0', 'K1']#Esto establece el índice del DataFrame df2 para que coincida con los valores proporcionados ('K0' y 'K1'). 
                      #Estos valores se utilizarán como claves para fusionar los DataFrames.
)

# Merge df1 and df2 on the 'key' column
merged = pd.merge(df1, df2, left_on='key', right_index=True) #Esto fusiona los DataFrames df1 y df2 en función de una columna ('key' en df1) y del índice de df2.
#Esto especifica que la columna 'key' en df1 se utilizará como clave para la fusión.
#Esto especifica que el índice de df2 se utilizará como clave para la fusión.
print(merged)