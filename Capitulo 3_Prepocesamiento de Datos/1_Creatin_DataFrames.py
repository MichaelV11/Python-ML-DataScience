import pandas as pd
import numpy as np

# From a dictionary
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c'],
})
print(df)

# From a list of dictionaries
df = pd.DataFrame([
    {'A': 1, 'B': 'a'},
    {'A': 2, 'B': 'b'},
    {'A': 3, 'B': 'c'},
])
print(df)

# From a 2D NumPy array
import numpy as np

array = np.array([[1, 'a'], [2, 'b'], [3, 'c']])
df = pd.DataFrame(array, columns=['A', 'B'])
print(df)