from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Create a list of categories
categories = [['red'], ['blue'], ['green'], ['red'], ['green'], ['blue'], ['blue'], ['green']]

# Convert the list of lists into a 2D numpy array
categories_array = np.array(categories).reshape(-1, 1)

# Create a OneHotEncoder
encoder = OneHotEncoder(sparse=False)

# Perform One-Hot Encoding
onehot_encoded_categories = encoder.fit_transform(categories)

print(onehot_encoded_categories)

#pendiente 

#Notas, si una columna tiene el numero 1 significa que tiene ese valor asignado, si tiene un 0 no tiene ese valor
#Cada columna se convierte en categorias 
