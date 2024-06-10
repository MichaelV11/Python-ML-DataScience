import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a figure and a set of subplots
fig, axs = plt.subplots(2) #Crea una figura y un conjunto de subtramas, devolviendo una tupla que contiene la figura (fig) y un arreglo de los ejes de las subtramas (axs)
#El '2' especifica que queremos dos subplots uno encima del otro
#La figura y los ejes de las subtramas se asignan a las variables fig y axs, respectivamente.

# Create a line plot on the first subplot
axs[0].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])#Crea un gráfico de línea en el primer subplot (axs[0]). Se pasan listas de valores para los ejes x (izquierda) e y(derecha).
axs[0].set_title('Square Numbers') #Establece el título del primer subplot como "Square Numbers".

# Create a bar plot on the second subplot
axs[1].bar(['A', 'B', 'C'], [10, 20, 30]) #Crea un gráfico de barras en el segundo subplot (axs[1]). Se especifican las etiquetas del eje x(izquierda) y las alturas de las barras(derecha)
axs[1].set_title('Bar Plot') #Establece el título del segundo subplot como "Bar Plot".

# Display the figure and its subplots
plt.tight_layout() #Ajusta automáticamente los subplots de manera que no haya superposiciones entre ellos. 
#Esto asegura que los elementos de los subplots no se solapen y sean claramente visibles.
plt.show() #Muestra la figura y sus subplots. Es importante incluir esta línea al final para que la figura se muestre correctamente