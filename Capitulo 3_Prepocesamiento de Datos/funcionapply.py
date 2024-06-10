import pandas as pd
"""df = pd.DataFrame({"Col1" : [1,2,3], "Col2":[5,6,7], "Col3":["Hugo","Paco","Luis"]}) #Creamos un diccionario, con columnas y 3 datos para cada columna
print(df)

print(df.apply(len)) #apply sirve par aplicar una función personalizada a cada columna (a cada dato de la columna) del DataFrame (todas las columnas). Función len() calcula la longitud de cada columna
print(df[["Col1", "Col2"]].apply(sum)) #se sumaron todas los número que estan en las columnas 1 y 2

print(df[["Col1", "Col2"]].apply(sum, axis=1)) #se sumaron todas los número que estan en las columnas 1 y 2 en forma horizontal "axis =1"

def cuadrado(num):
    if num % 2 ==0:
        return num**2
    else:
        return num

print(df["Col1"].apply(cuadrado))

print(df["Col2"].apply(lambda num: num**2 if num % 2 == 0 else num)) #lambda sirve para generar una función anonima
"""

df = pd.DataFrame({"Col3":["Hugo","Paco","Luis"], "Mate" : [8,5,7], "Esp":[10,10,5]})
print(df)

def califi(num):
    if num <6:
        return "Muy mal"
    elif (num>=6) & (num<9): #se pueden poner tantos elif para poner mas condiciones
        return "Regular"
    else:
        return "Excelente"
print(df["Mate"].apply(califi))

print(df["Esp"].apply(lambda num: "Muy mal" if num<6 else ("Regular" if (num>=6) & (num<9) else "Excelente")))


