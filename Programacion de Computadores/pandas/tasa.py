import pandas as pd

movies = pd.read_csv("/home/sebas/Practice/Python_Practicesp3767/pandas/movies.csv", index_col="Title" )

#Los primeros resultados.
print(movies.head())
#Los ultimos.
print(movies.tail())

#Te permite ver la cardinalidad de la columna.
print(len(movies))

#Te permite ver la cantidad de columnas que hay.
print(movies.shape)

#Extraccion de columnas. 
print(movies["Gross"])

print(movies[["Gross","Year"]])

#Ver valores por Columna especifica.
print(movies["Year"].value_counts().sort_index(ascending=False))

print(movies["Year"].value_counts())

#Ejemplos
pelis_2015 = movies["Year"] == 2015
pelis_2015_fox = movies["Studio"] == "Fox"

count = 0
for i in range (len(movies)):
    if movies["Year"][i] == 2015 and movies["Studio"][i] == "Fox":
        count += 1

print(count)

#Existe, max, min, mean
print(min(movies["Year"]))
print(movies.groupby("Studio"))

