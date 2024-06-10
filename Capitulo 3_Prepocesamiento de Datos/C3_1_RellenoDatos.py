import pandas as pd
import numpy as np

# Create a DataFrame with missing values
df = pd.DataFrame({
    'A': [1, 2, np.nan], #np.nan representa un valor faltante o nulo
    'B': [4, np.nan, 6],
    'C': [7, 8, 9]
})

print("Original DataFrame:")
print(df)

# Remove rows with missing values
df_dropped = df.dropna() #Crea un nuevo DataFrame llamado df_dropped eliminando todas las filas que contienen valores faltantes (NaN) en alguna de sus columnas.
print("\nDataFrame after dropping rows=eliminar filas with missing values:")
print(df_dropped)

# Fill=Llenar missing values with a specific value
df_filled = df.fillna(0) #Crea un nuevo DataFrame llamado df_filled llenando todos los valores faltantes (NaN) con el valor 0.
print("\nDataFrame after filling missing values with 0:")
print(df_filled)

# Fill missing values with mean=media of the column
df_filled_mean = df.fillna(df.mean()) #Crea un nuevo DataFrame llamado df_filled_mean llenando los valores faltantes (NaN) en cada columna con la media de esa columna.
print("\nDataFrame after filling missing values with mean of the column:")
print(df_filled_mean)