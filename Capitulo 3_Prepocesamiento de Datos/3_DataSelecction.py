import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c'],
})

# Select a column
print(df['A'])

# Select multiple columns
print(df[['A', 'B']])

# Select a row by label = seleccionar una fila por etiqueta
print(df.loc[0]) #Esto imprime la fila con etiqueta (índice) 0 del DataFrame. .loc[] se utiliza para seleccionar filas por sus etiquetas.

# Select a row by number
print(df.iloc[0]) #Esto imprime la primera fila del DataFrame. .iloc[] se utiliza para seleccionar filas por su posición numérica en el DataFrame.

# Select a specific value
print(df.loc[0, 'A'])#Esto imprime el valor en la fila con etiqueta 0 y columna 'A'. Se usa .loc[] con dos argumentos, el primero es la etiqueta de la fila y el segundo es el nombre de la columna.
print(df.iloc[0, 0]) # Esto imprime el valor en la primera fila y primera columna del DataFrame. Se usa .iloc[] con dos argumentos, ambos son índices numéricos.






