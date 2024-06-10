from sklearn.preprocessing import OrdinalEncoder

# Create a list of categories
categories = [['cold'], ['warm'], ['hot'], ['cold'], ['hot'], ['warm'], ['warm'], ['hot']]
#Crea una lista llamada categories que contiene las etiquetas de las categorías que queremos codificar. En este caso, las categorías son 'cold', 'warm' y 'hot'.

# Create an OrdinalEncoder
encoder = OrdinalEncoder(categories=[['cold', 'warm', 'hot']])
#Crea un objeto OrdinalEncoder llamado encoder. Este objeto se utilizará para transformar las etiquetas de las categorías en valores ordinales.
#Se proporciona una lista de listas que especifica el orden de las categorías. En este caso, 'cold' es el primer valor, 'warm' es el segundo y 'hot' es el tercero.

# Perform Ordinal Encoding
ordinal_encoded_categories = encoder.fit_transform(categories)
#Aplica la transformación de codificación ordinal a las categorías utilizando el método fit_transform del objeto encoder.
#Este método ajusta el codificador a las categorías y luego transforma las categorías en valores ordinales.

print(ordinal_encoded_categories)