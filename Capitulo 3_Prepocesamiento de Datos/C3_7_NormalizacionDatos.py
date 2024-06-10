from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})

# Create a MinMaxScaler
scaler = MinMaxScaler()#escala (0,1)

# Perform normalization
df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns) #Escala los datos del DataFrame df utilizando el método fit_transform del objeto scaler.
#Este método primero ajusta el escalador a los datos (calculando los mínimos y máximos de las características) y luego transforma los datos según la escala especificada.
#Establece los nombres de las columnas del nuevo DataFrame 

print(df_normalized) 