import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'height': [5.0, 6.1, 5.6, 5.8, 6.0],
    'width': [3.5, 3.0, 3.2, 3.7, 3.3]
})

# Create a new interaction feature 'area'. Se crea una nueva característica de interacción llamada area
#df['area'] = ...: Crea una nueva columna en el DataFrame llamada 'area'.
df['area'] = df['height'] * df['width']
#Multiplica los valores de la columna 'height' por los valores de la columna 'width' elemento a elemento, 
#generando así una nueva serie de datos que representan el área de cada observación.

print(df)