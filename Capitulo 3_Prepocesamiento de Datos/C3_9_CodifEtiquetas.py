from sklearn.preprocessing import LabelEncoder #LabelEncoder se utiliza para transformar las etiquetas de las categorías en valores numéricos.

# Create a list of categories
categories = ['red', 'blue', 'green', 'red', 'green', 'blue', 'blue', 'green']
#Crea una lista llamada categories que contiene las etiquetas de las categorías que queremos codificar. En este caso, las categorías son 'red', 'blue' y 'green'.

# Create a LabelEncoder
encoder = LabelEncoder() #Crea un objeto LabelEncoder llamado encoder. Este objeto se utilizará para transformar las etiquetas de las categorías en valores numéricos.

# Perform Label Encoding
encoded_categories = encoder.fit_transform(categories)#Aplica la transformación de codificación de etiquetas a las categorías utilizando el método fit_transform del objeto encoder. 
#Este método ajusta el codificador a las categorías y luego transforma las categorías en valores numéricos.

print(encoded_categories)#Imprime los valores numéricos resultantes después de la codificación de etiquetas. 
#Estos valores representan las categorías codificadas como números enteros únicos. Cada valor numérico corresponde a una categoría única en la lista categories.