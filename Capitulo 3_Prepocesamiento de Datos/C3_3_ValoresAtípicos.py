from scipy import stats
import numpy as np

# Create a numpy array with outliers
data = np.array([1, 2, 2, 2, 3, 1, 2, 3, 3, 4, 4, 4, 20])

# Calculate Z-scores
z_scores = stats.zscore(data)

# Get indices of outliers
outliers = np.abs(z_scores) > 2 #Creamos un arreglo booleano llamado outliers que indica True para los valores que son considerados outliers 
#(es decir, cuyos Z-scores absolutos son mayores que 2), y False para los valores que no son outliers

print(outliers)

# Remove outliers
data_clean = data[~outliers] #Creamos un nuevo arreglo llamado data_clean que contiene solo los valores que no son outliers.
#Usamos el operador ~ para negar la condición, seleccionando los valores que no cumplen con la condición de ser outliers.
print("Data after removing outliers:")
print(data_clean)
