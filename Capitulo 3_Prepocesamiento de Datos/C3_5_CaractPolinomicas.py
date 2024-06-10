from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

# Create a PolynomialFeatures object
poly = PolynomialFeatures(2)

# Create a DataFrame
df = pd.DataFrame({
    'height': [5.0, 6.1, 5.6, 5.8, 6.0],
    'width': [3.5, 3.0, 3.2, 3.7, 3.3]
})

# Create polynomial features

#df_poly = poly.fit_transform(df): Crea un nuevo DataFrame llamado df_poly que contiene las características polinómicas generadas a partir de las características originales del DataFrame df.
#fit_transform es un método de PolynomialFeatures que ajusta el modelo y transforma las características originales en características polinómicas.
df_poly = poly.fit_transform(df)

# Get the feature names
feature_names = poly.get_feature_names_out(input_features=['height', 'width']) #Obtiene los nombres de las características polinómicas generadas por PolynomialFeatures a partir de las características originales 'height' y 'width'.
#Esto es útil para asignar nombres a las columnas del DataFrame resultante.

# Create a DataFrame with the polynomial features and set the column names
df_poly_named = pd.DataFrame(df_poly, columns=feature_names) #Crea un nuevo DataFrame llamado df_poly_named con las características polinómicas generadas, 
#utilizando los nombres de las características obtenidos anteriormente. Estos nombres se asignan como nombres de las columnas del DataFrame.

print(df_poly_named)