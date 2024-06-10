import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a scatter plot with a regression line
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [1, 4, 9, 16, 25]
})
sns.regplot(x='x', y='y', data=df) #Esto crea un gráfico de dispersión con una línea de regresión utilizando Seaborn.
#Especifica el DataFrame df que contiene los datos que se utilizarán en el gráfico.
plt.show() # Esto muestra el gráfico en una ventana emergente. Es importante incluir esta línea al final para que el gráfico se muestre correctamente.




