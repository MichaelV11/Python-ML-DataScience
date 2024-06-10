import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#Ejercicio 1 
'''
# Create a DataFrame with missing values
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan]
})

# Your code here
df_filled = df.fillna(0)
print(df_filled)
'''

#Ejercicio 2
'''
# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 4, 5, 6],
    'C': [3, 4, 5, 6, 7]
})

# Your code here
df['Producto'] = df['A']*df['B']*df['C']
print(df)
'''
#Ejercicio 3

# Create a DataFrame
df = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'red', 'blue']
})

# Perform one-hot encoding
df_encoded = pd.get_dummies(df, columns=['color'], dtype=int) # Utiliza la función get_dummies() de Pandas para realizar la codificación one-hot en la columna 'color' del DataFrame df.
#columns=['color']: Este argumento especifica qué columnas del DataFrame df se deben codificar utilizando one-hot encoding. En este caso, solo queremos codificar la columna 'color'.
#dtype=int: Este parámetro opcional especifica el tipo de datos que se utilizará en las columnas codificadas.
#Al establecerlo en int, Pandas creará columnas con valores 0 y 1, en lugar del tipo de datos predeterminado uint8. Esto garantiza que los valores codificados sean enteros en lugar de enteros sin signo de 8 bits.
print(df_encoded)

#Ejercicio 4

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
})

# Create a StandardScaler
scaler = StandardScaler()

# Perform standardization
df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
#Utiliza el método fit_transform() del objeto scaler para estandarizar las características del DataFrame df. Luego, se crea un nuevo DataFrame llamado df_standardized con los datos estandarizados.
#Los nombres de las columnas del DataFrame estandarizado se mantienen iguales que las del DataFrame original df, lo que se logra con columns=df.columns.

print(df_standardized)

#Ejercicio 5

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
})

# Create a target variable
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]#Crea una lista y que contiene los valores de la variable objetivo

# Perform train-test split
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.3, random_state=42)
#test_size=0.3: Este argumento especifica el tamaño del conjunto de prueba, que es el 30% de los datos totales.
print("X_train:")
print(X_train)
print("\nX_test:")
print(X_test)
print("\ny_train:")
print(y_train)
print("\ny_test:")
print(y_test)