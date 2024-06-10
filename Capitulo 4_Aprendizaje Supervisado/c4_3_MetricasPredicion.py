from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
#Importa algunas funciones de métricas de regresión del módulo metrics de scikit-learn.
#Estas funciones se utilizan para calcular el error absoluto medio (MAE), el error cuadrático medio (MSE), el error cuadrático medio (RMSE) y el coeficiente de determinación (R-cuadrado).
import numpy as np
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 4, 5, 4, 5]
})

# Create a LinearRegression model
model = LinearRegression()

# Fit the model
model.fit(df[['A']], df['B'])

# Predict new values
predictions = model.predict(df[['A']])

# Calculate MAE
mae = mean_absolute_error(df['B'], predictions)

# Calculate MSE
mse = mean_squared_error(df['B'], predictions)

# Calculate RMSE
rmse = np.sqrt(mse)

# Estas funciones calculan respectivamente el error absoluto medio (MAE), el error cuadrático medio (MSE) y 
#el coeficiente de determinación (R-cuadrado) entre las etiquetas verdaderas df['B'] y las predicciones predictions.
#np.sqrt(): Calcula la raíz cuadrada del MSE para obtener el RMSE

# Calculate R-squared
r2 = r2_score(df['B'], predictions)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R-squared:", r2)#Tiene una escala de valores en 1 y 0. Valor 1 significa una predicción perfecta.