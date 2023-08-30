import pandas as pd

            #######  Datos de: https://www.kaggle.com/datasets/victorsoeiro/amazon-prime-tv-shows-and-movies  #######

df  = pd.read_csv("titles.csv") 
df.info                                         #Información del archivo
df.head()                                       #Entrega datos de las columnas de hasta arriba (por defecto las primeras 5)
df.tail()                                       #Entrega los datos de las columnas de hasta abajo (por defecto las primeras 5)
df['title']                                     #Entrega una o varias columnas en especifico
print(df.columns)                               #Entrega las columnas

df.loc[[10,11,12], 'title']                     #Imprime filas y columnas especificas      
df.loc[62:70, ['title','genres']]               #Se le pueden entregar rangos

df['release_year'].value_counts()               #Cuenta cuantos valores hay de cada tipo en una columna

df.loc[5093]                                    #Imprime todos los atributos de una fila
df['genres'] == "['drama']"                     #Devuelve true si la condición se cumple, false si no

filtro = (df['genres'] == "['drama']"
         )&(df['release_year']==2000)           #Se pueden encapsular varias condiciones dentro de una varible

print(df.loc[filtro,'genres'])                  #Devuelve todas las filas que pasen el filtro y se le añade que muestre una columna
df.loc[-filtro]                                 #Devuelve todas las filas que no pasen el filtro

filtro2 = df['genres'].str.contains('horror')   #Filtrará todas las peliculas que en genero contengan 'terror' pero no 
                                                #unicamente terror (necesariamente)
print(df.loc[filtro2,'genres'])

df.sort_values(by=['genres','runtime'], ascending=[True, False], inplace = True)   #Ordenar con dos columnas
print(df[['runtime', 'genres']].head(10))

df.drop(columns=['age_certification'], inplace = True)      #Eliminar una columna
df.drop(index=1)                                            #Borrar una fila
df.drop(index=df[df['imdb_score']==9.3].index)              #Borrar filas con una caracteristica especifica