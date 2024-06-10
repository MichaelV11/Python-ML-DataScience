from sklearn import preprocessing, model_selection, linear_model, metrics

# Create a StandardScaler
scaler = preprocessing.StandardScaler()#Crea un objeto StandardScaler del módulo preprocessing. 
#StandardScaler es una clase que se utiliza para estandarizar características eliminando la media y escalando a la varianza unitaria

# Fit the StandardScaler to the data
data = [[0, 0], [0, 0], [1, 1], [1, 1]]#Define una lista de listas llamada data que contiene datos de ejemplo. Cada lista interior representa una observación con dos características.
scaler.fit(data) #Ajusta el StandardScaler al conjunto de datos proporcionado data. En este caso, data es una lista de listas que contiene datos de ejemplo.

# Transform the data
scaled_data = scaler.transform(data)#ransforma los datos data utilizando el StandardScaler ajustado previamente (scaler). 
#Esto aplica la estandarización a los datos. La transformación estandariza cada característica restando la media y dividiendo por la desviación estándar.
print(scaled_data)

#estandarizacion de datos