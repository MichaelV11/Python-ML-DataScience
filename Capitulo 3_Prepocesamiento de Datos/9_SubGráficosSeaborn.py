import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")#Carga el conjunto de datos "iris" proporcionado por Seaborn.
#Este conjunto de datos contiene mediciones de longitud y ancho del sépalo y pétalo de tres especies de iris.
g = sns.FacetGrid(iris, col="species") # Crea un objeto FacetGrid de Seaborn llamado g. FacetGrid se utiliza para visualizar la distribución de una variable 
#(en este caso, la longitud del sépalo) a través de múltiples subconjuntos de datos (en este caso, las especies de iris). 
#El parámetro col="species" indica que se crearán columnas separadas en la cuadrícula para cada especie de iris.
g.map(plt.hist, "sepal_length")#Mapea un histograma de la longitud del sépalo ("sepal_length") en cada una de las columnas de la cuadrícula. 
#g.map() se utiliza para aplicar una función a cada uno de los subconjuntos de datos en FacetGrid. En este caso, la función 
#plt.hist se utiliza para crear un histograma de la longitud del sépalo.

plt.show()
