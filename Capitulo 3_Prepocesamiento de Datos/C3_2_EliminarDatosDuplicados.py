import pandas as pd

# Create a DataFrame with duplicate rows
df = pd.DataFrame({
    'A': [1, 2, 2, 3, 3, 3],
    'B': [4, 5, 5, 6, 6, 6],
    'C': [7, 8, 8, 9, 9, 9]
})

print("Original DataFrame:")
print(df)

# Remove duplicate rows
df_deduplicated = df.drop_duplicates() #Crea un nuevo DataFrame llamado df_deduplicated eliminando todas las filas duplicadas del DataFrame original df.
print("\nDataFrame after removing duplicates:")
print(df_deduplicated)