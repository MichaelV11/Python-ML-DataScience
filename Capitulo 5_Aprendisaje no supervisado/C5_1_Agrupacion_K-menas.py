from sklearn.cluster import KMeans
import numpy as np

# Create a random dataset
X = np.random.rand(100, 2)
#X = np.random.rand(100, 2): Genera un conjunto de datos aleatorio de 100 puntos, cada uno con 2 características (dimensiones). 
#np.random.rand(100, 2) crea una matriz de tamaño 100x2 con valores aleatorios en el rango [0, 1).

# Create a KMeans instance with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=0)
#Crea una instancia del modelo K-Means configurada para encontrar 3 clusters. 
#n_clusters=3 especifica que queremos dividir los datos en 3 grupos. random_state=0 fija la semilla del generador de números aleatorios para que los resultados sean reproducibles

# Fit the model to the data
kmeans.fit(X)
#Ajusta el modelo K-Means a los datos X. Esto significa que el algoritmo encuentra las posiciones 
#de los centros de los clusters que minimizan la suma de las distancias al cuadrado entre los puntos de datos y los centros de los clusters.

# Get the cluster assignments for each data point
labels = kmeans.labels_
#Ajusta el modelo K-Means a los datos X. Esto significa que el algoritmo encuentra las posiciones de los centros 
#de los clusters que minimizan la suma de las distancias al cuadrado entre los puntos de datos y los centros de los clusters.

# Get the coordinates of the cluster centers
cluster_centers = kmeans.cluster_centers_
#Obtiene las etiquetas de los clusters para cada punto de datos en X. 
#kmeans.labels_ es un array donde cada elemento es el índice del cluster al que pertenece el correspondiente punto de datos.

print("Cluster labels:", labels)
print("Cluster centers:", cluster_centers)

#print("Cluster labels:", labels): Imprime las etiquetas de los clusters asignadas a cada punto de datos. Esto muestra a qué cluster pertenece cada punto.
#print("Cluster centers:", cluster_centers): Imprime las coordenadas de los centros de los clusters. Esto muestra las ubicaciones de los centros de los clusters encontrados por el algoritmo.

