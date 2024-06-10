import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import preprocessing, model_selection, linear_model, metrics


# Create a linear regression model
model = linear_model.LinearRegression()

# Train the model
X = [[0, 0], [1, 1]]
y = [0, 1]
model.fit(X, y)

# Perform 5-fold cross-validation
scores = model_selection.cross_val_score(model, X, y, cv=5)#El parámetro cv=5 en la función cross_val_score indica el número de particiones que se utilizarán en la validación cruzada. 
#En este caso particular, cv=5 significa que se realizará una validación cruzada de 5 veces.

# Print cross-validation scores
print(scores)