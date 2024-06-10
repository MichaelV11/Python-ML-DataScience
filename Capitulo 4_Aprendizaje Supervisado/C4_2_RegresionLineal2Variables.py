from sklearn.linear_model import LinearRegression
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 4, 5, 6],
    'C': [3, 4, 5, 6, 7]
})

# Create a LinearRegression model
model = LinearRegression()

# Fit the model
model.fit(df[['A', 'B']], df['C'])#fit para entrenar el modelo, nos dara los coeficientes que faltan en la formula
#Utiliza el método fit() del objeto model para entrenar el modelo de regresión lineal.
#df[['A', 'B']] representa las características de entrada variables (en este caso, las columnas 'A' y 'B') y df['C'] representa el resultado Y (en este caso, la columna 'C').

# Predict new values
predictions = model.predict(df[['A', 'B']])
#Utiliza el método predict() del objeto model para hacer predicciones.
#Aquí, estamos haciendo predicciones para las mismas características de entrada que se utilizaron para entrenar el modelo (las columnas 'A' y 'B').
print(predictions)
#El resultado predice los valores que estan fuera de la linea de regresion. Cuanto mas cerca esten los puntos reales de la linea de regresion
#mejor sera el modelo