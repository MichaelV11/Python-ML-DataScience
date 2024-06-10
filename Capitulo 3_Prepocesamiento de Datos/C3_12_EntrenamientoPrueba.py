from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
})

# Create a target variable
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] #Crea una lista llamada y que contiene la variable objetivo, en este caso, una lista de valores binarios que representan las clases a predecir.

# Perform a train-test split
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=42)
#Utiliza la función train_test_split para dividir los datos en conjuntos de entrenamiento y prueba. X_train y X_test son los conjuntos de características de entrenamiento y prueba, 
#respectivamente, mientras que y_train y y_test son los conjuntos de etiquetas de entrenamiento y prueba, respectivamente.
#test_size=0.2: Especifica el tamaño del conjunto de prueba, que en este caso es el 20% del total de los datos.

#random_state=42: Establece una semilla aleatoria para garantizar la reproducibilidad de la división.
#La misma semilla garantiza que cada vez que se ejecute el código, la división sea la misma.

print("X_train:")
print(X_train)
print("\nX_test:")
print(X_test)
print("\ny_train:")
print(y_train)
print("\ny_test:")
print(y_test)

# Gráfico de dispersión para las características X_train y X_test
plt.scatter(X_train['A'], X_train['B'], c='blue', label='X_train')#plt.scatter: Esta función de matplotlib se utiliza para crear un gráfico de dispersión.
#X_train['A'] y X_train['B']: Estas son las características del conjunto de entrenamiento X_train. 
#Se pasan como argumentos para los ejes x e y del gráfico de dispersión, respectivamente.
plt.scatter(X_test['A'], X_test['B'], c='red', label='X_test')
plt.xlabel('Feature A')
plt.ylabel('Feature B')
plt.title('Scatter Plot of Features X_train and X_test')
plt.legend()
plt.show()

#pendiente de repasar

#plt.scatter(X_train['A'],y_train)
#plt.scatter(X_test,y_test) 