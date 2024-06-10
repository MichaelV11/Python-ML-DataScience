import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': np.random.randn(8), #Esta es la especificación de la columna 'C', que contiene valores generados aleatoriamente de una distribución normal utilizando la función np.random.randn()
    'D': np.random.randn(8)
})
