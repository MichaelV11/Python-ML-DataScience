import pandas as pd
import numpy as np

df=pd.DataFrame("tratamiento_datos.csv", index_col = 0)

def remove_negative_values(df, column):
    df[column] = df[column].apply(lambda x: np.nan if x < 0 else x)
    return df

def remove_outliers_with_zscore(df,column,threshold = 2):
    column_mean = df[column].mean() #calculo de la media
    column_std = df[column].std() #calculo de la desviación estandar (S), es la desviación numerica entre un conujnto de datos
    df[column] = df[column].mask(((df[column]-column_mean)/column_std).abs()>threshold, column_mean) #se usa la formula para sacar la Z
    return df