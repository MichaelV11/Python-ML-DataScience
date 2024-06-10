import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'age': [5, 15, 25, 35, 45, 55]
})

# Define bins
bins = [0, 18, 35, 60, 100] #Define los límites de los INTERVÁLOS para la discretización de las edades. Estos límites definen los límites de cada grupo de edad.
#Tenemos 4 interválos de edades. Del 0-18, 18-35, etc.

# Define labels
labels = ['child', 'young adult', 'adult', 'senior'] #Define las etiquetas que se asignarán a cada grupo de edad. 
#Estas etiquetas se utilizarán para etiquetar los intervalos resultantes después de la discretización.

# Perform binning
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels) #Crea una nueva columna en el DataFrame llamada 'age_group', 
#que contendrá las etiquetas de grupo de edad resultantes después de la discretización de la columna 'age'.
#pd.cut() se utiliza para discretizar una columna en intervalos basados en los límites definidos en bins, y labels se utiliza para asignar etiquetas a cada intervalo.

print(df)

 