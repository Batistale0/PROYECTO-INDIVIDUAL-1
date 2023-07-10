#Importamos librerias
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from fastapi import FastAPI

#Leemos el archivo csv
df = pd.read_csv('dfconcatenado.csv')


# http://127.0.0.1:8000/

app = FastAPI()




#Consulta 1 -- Debe devolver la cantidad de películas producidas en ese idioma.
@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma: str):
     # Contamos la cantidad de películas producidas en el idioma especificado
    cantidad = df['original_language'].value_counts()[idioma]
    #Retornamos la cantidad de películas producidas en el idioma especificado.
    return {'respuesta': f"{cantidad} peliculas fueron estrenadas en idioma {idioma}"}

#Consulta 2 -- Se ingresa una pelicula. Debe devolver la la duracion y el año.
@app.get('/peliculas_duracion/{Pelicula}')
def peliculas_duracion(Pelicula):
    ## filtramos para buscar la película específica y obtener su duración y año
    movies_title = df.loc[df['title'] == Pelicula]
    duracion = movies_title['runtime'].values[0]
    year = movies_title['release_year'].values[0]
    
    return {'respuesta': f"La pelicula {Pelicula} tiene una duración de {duracion}min y fue estrenada en el Año: {year}"}

#Consulta 3 -- Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
@app.get('/franquicia/{Franquicia}')
def franquicia(Franquicia: str):
    # Filtramos para buscar las películas de la franquicia específica y obtener la cantidad, la ganancia total y el promedio
    movies_collection = df.loc[df['belong_collection'] == Franquicia]
    cantidad = movies_collection.shape[0]
    ganancia_total = movies_collection['revenue'].sum()
    ganancia_promedio = movies_collection['revenue'].mean()
    
    return {'respuesta':f"La franquicia {Franquicia} posee {cantidad} películas, con una ganancia total de {ganancia_total} y una ganancia promedio de {ganancia_promedio}"}

#Consulta 4 -- Se ingresa un país, retornando la cantidad de peliculas producidas en el mismo.
@app.get('/pelicula_pais/{Pais}')
def peliculas_pais(Pais: str):
    #Filtramos las películas producidas en el país específico y obtenemos la cantidad de peliculas producidas
    countries = df.loc[df['production_countries'] == Pais]
    cantidad = countries.shape[0]

    return {'respuesta': f"Se produjeron {cantidad} películas en el país de {Pais}"}

#Consulta 5 -- Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo.
@app.get('/productoras_exitosas/{Productora}')
def productoras_exitosas(Productora: str):
    # Filtramos las películas de la productora y obtenemos la cantidad y la ganancia total
    production = df.loc[df['production_companie'] == Productora]
    cantidad = production.shape[0]
    ganancia_total = production['revenue'].sum()

    return {'respuesta': f"La productora {Productora} ha tenido una recaudación total de {ganancia_total} y ha realizado {cantidad} películas"}



#Consulta 6 -- #Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
#Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.
@app.get("/director/{nombre_director}")
def get_director(nombre_director: str):
    nombre_director = nombre_director.lower()  ##Para ignorar mayusculas y minusculas
    # Relleno los valores NaN en las columnas relevantes con valores adecuados para que no largue error
    df['creww'] = df['creww'].fillna('')
    df['return'] = df['return'].fillna(0)
    # Obtenemos el éxito del director, detalles de las películas, costo y ganancia
    director_names = df[df['creww'].str.contains(nombre_director, case=False)]
    return_total = director_names['return'].sum()
    peliculas = []

    for _, row in director_names.iterrows():
        pelicula = {
        'titulo':row['title'],
        "Anio": row['release_year'],
        "Retorno_pelicula": row['return'],
        "Budget_pelicula": row['budget'],
        "Revenue_pelicula": row['revenue']
        }
    
        peliculas.append(pelicula)

    respuesta = {
        'Director': nombre_director,
        'retorno total': return_total,
        'Películas': peliculas,
        
    }

    return respuesta



















