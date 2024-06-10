from sklearn import preprocessing, model_selection, linear_model, metrics
import matplotlib.pyplot as plt
import seaborn as sns

# Create a linear regression model
model = linear_model.LinearRegression()

# Train the model
X = [[0, 0], [1, 1], [20,21]]
y = [0, 1, 20.5]
model.fit(X, y)#Entrena el modelo de regresión lineal utilizando los datos X e y. 
#Esto ajusta los parámetros del modelo para minimizar la suma de los cuadrados de las diferencias entre las observaciones reales y las predicciones del modelo.

# Make predictions
X_new = [[2, 2]] #dos muestras para el valor X
y_new = model.predict(X_new) #predición de Y que la regresión lineal da para valores de X
print(y_new)

X_new2 = [[10, 10]]
Y_new2 = model.predict(X_new2)
print(Y_new2)

# Calculate the mean squared error of the predictions
y_true = [1]  # Define los valores reales de las etiquetas y_true para las observaciones en X_new. En este caso, y_true contiene una única etiqueta.
#y_pred = model.predict(X_new): Realiza predicciones y_pred para los datos X_new utilizando el modelo entrenado
y_pred = model.predict(X_new)
mse = metrics.mean_squared_error(y_true, y_pred) #Calcula el error cuadrático medio (MSE) entre las etiquetas reales y_true y las predicciones del modelo y_pred. 
#El error cuadrático medio es una métrica comúnmente utilizada para evaluar la calidad de las predicciones de un modelo de regresión.
print(mse)#Imprime el valor del error cuadrático medio. Cuanto más cercano a cero sea el valor, mejor será el ajuste del modelo.

print(model.coef_)
print(model.intercept_)

plt.plot(X,y)
plt.plot(X_new2,Y_new2)
plt.grid()

plt.show()