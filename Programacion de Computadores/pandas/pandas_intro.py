import pandas as pd

#Hay que hacer columnas por tipo de dato, ya sea str, int, float, bool


# Crear las series de datos
names = pd.Series(['John', 'Alice', 'Michael', 'Emma', 'David'])
ages = pd.Series([25, 30, 35, 28, 32])
heights = pd.Series([170, 165, 180, 175, 185])
weights = pd.Series([70, 60, 80, 75, 90])

#Los Data frames son combinaciones de series. 

dataframe = pd.DataFrame({'Nombres':names,'Edades':ages})

print(dataframe)

