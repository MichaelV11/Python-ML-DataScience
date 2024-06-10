from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd

# Load the Boston Housing dataset
boston = load_boston()

# Create a DataFrame
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['MEDV'] = boston.target

# Create a LinearRegression model
model = LinearRegression()

# Fit the model
model.fit(df[['RM']], df['MEDV'])

# Predict new values
predictions = model.predict(df[['RM']])

# Calculate metrics
mae = mean_absolute_error(df['MEDV'], predictions)
mse = mean_squared_error(df['MEDV'], predictions)
rmse = np.sqrt(mse)
r2 = r2_score(df['MEDV'], predictions)

print("MAE:", mae)#Error absoluto medio. Es el promediode la diferencia absoluta entre los valores predichos y el valor observado
print("MSE:", mse)
print("RMSE:", rmse)#Error cuadratico medio. Los valores más bajos indican un mejor ajuste del modelo de predicción
print("R-squared:", r2)