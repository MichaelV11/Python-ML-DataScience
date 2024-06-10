import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Set the plot style to 'whitegrid'
sns.set_style('whitegrid') #Establece el estilo de la trama como 'whitegrid'. 
#Seaborn proporciona varios estilos estéticos para las tramas, y 'whitegrid' es uno de ellos. Este estilo agrega líneas de cuadrícula blancas al fondo de la trama.

# Create a scatter plot with a regression line
df = pd.DataFrame({#Crea un DataFrame de Pandas llamado df.
#{...}: Dentro del constructor pd.DataFrame(), se proporciona un diccionario donde las claves son los nombres de las columnas 
#y los valores son las listas de datos correspondientes a esas columnas.
    'x': [1, 2, 3, 4, 5], 
    'y': [1, 4, 9, 16, 25]
})
sns.regplot(x='x', y='y', data=df) # Crea un gráfico de dispersión con una línea de regresión utilizando Seaborn.
#data=df: Especifica el DataFrame df que contiene los datos que se utilizarán en el gráfico.
plt.show()