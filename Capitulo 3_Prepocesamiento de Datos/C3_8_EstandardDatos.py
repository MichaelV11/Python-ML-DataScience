from sklearn.preprocessing import StandardScaler
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})

# Create a StandardScaler
scaler = StandardScaler()

# Perform standardization
df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns) #Estandariza los datos del DataFrame df utilizando el método fit_transform del objeto scaler. Este método primero ajusta el escalador a los datos 
#(calculando la media y la desviación estándar) y luego transforma los datos para que tengan una media de cero y una desviación estándar de uno.

#columns=df.columns: Establece los nombres de las columnas del nuevo DataFrame 

print(df_standardized)