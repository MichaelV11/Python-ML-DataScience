import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': ['a', 'b', 'c'],
})
#Dos formas de rellenar valores faltantes
# Fill missing values
df_filled = df.fillna(0) #Esto llena los valores faltantes (NaN)/(np.nan) en el DataFrame con el valor especificado, en este caso, 0. El método fillna() es utilizado para rellenar los valores faltantes.
print(df_filled)

# Replace values
df_replaced = df.replace(np.nan, 0)#Esto reemplaza todos los valores NaN en el DataFrame con el valor especificado, en este caso, 0. El método replace() es utilizado para reemplazar valores en el DataFrame.
print(df_replaced)

print(df['A'].describe()) #La función describe() calcula una variedad de estadísticas resumidas sobre una columna, como la media, el max, el min, valores totales,etc