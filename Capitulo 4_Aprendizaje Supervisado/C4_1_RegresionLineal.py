from sklearn.linear_model import LinearRegression
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 4, 5, 4, 5]
})

# Create a LinearRegression model
model = LinearRegression()

# Fit the model Y(B) = mX(A) + b
model.fit(df[['A']], df['B']) #Utiliza el método fit() del objeto model para entrenar el modelo de regresión lineal. 
#df[['A']] representa las características de entrada (en este caso, solo la columna 'A') y df['B'] representa el resultado Y (en este caso, la columna 'B').

# Predict new values
predictions = model.predict(df[['A']])
#Utiliza el método predict() del objeto model para hacer predicciones.
#Aquí, estamos haciendo predicciones para las mismas características de entrada que se utilizaron para entrenar el modelo (solo la columna 'A').
print(predictions)