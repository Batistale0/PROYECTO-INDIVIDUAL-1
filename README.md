##    PROYECTO-INDIVIDUAL-1 DATA SCIENCES


![What_is_Data_Science-1080x675](https://github.com/Batistale0/PROYECTO-INDIVIDUAL-1/assets/123607264/45b14c46-bf89-432c-a142-da63fce19198)


## ¡Bienvenidos al primer proyecto individual de la etapa de labs! En esta ocasión, tuvimos que hacer un trabajo situándonos en el rol de un MLOps Engineer.

### Descripicon de los distintos archivos y carpetas:
### Datos:
- En la carpeta datasets estan los 2 archivos cvs que nos otorgaron para la realización del proyecto (movies.csv y credits.csv)

### Extraccion, Transformacion y Carga: Extraccion, Transformacion y Carga:
- movies.ipynb, y credits.ipynb se encuentra todo lo relacionado con la extracción, la transformación y la carga de los datos.

### Análisis exploratorio de los datos(EDA):
- Implica el uso de gráficos y visualizaciones para explorar y analizar un conjunto de datos. El objetivo es explorar, investigar y aprender (EDA.ipynb).

### Desarrollo API:
Nos proponen disponibilizar los datos de la empresa usando el framework FastAPI. Las consultas que nos proponen son las siguientes:

Deben crear 6 funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).

Todas las funciones se encuentran en (main.py).


### Descripción del problema (Contexto y rol a desarrollar):

### Contexto:
Tienes tu modelo de recomendación dando unas buenas métricas, y ahora, cómo lo llevas al mundo real? 

El ciclo de vida de un proyecto de Machine Learning debe contemplar desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.

### Rol que debiamos desarrollar:

Empezaste a trabajar como Data Scientist en una start-up que provee servicios de agregación de plataformas de streaming. El mundo es bello y vas a crear tu primer modelo de ML que soluciona un problema de negocio: un sistema de recomendación que aún no ha sido puesto en marcha!

Vas a sus datos y te das cuenta que la madurez de los mismos es poca (ok, es nula. Datos anidados, sin transformar, no hay procesos automatizados para la actualización de nuevas películas o series, entre otras cosas…. haciendo tu trabajo imposible.

Debes empezar desde 0, haciendo un trabajo rápido de Data Engineer y tener un MVP (Minimum Viable Product) para el cierre del proyecto! Tu cabeza va a explotar 🤯, pero al menos sabes cual es, conceptualmente, el camino que debes de seguir :exclamation:. Así que te espantas los miedos y te pones manos a la obra.


## Propuesta de trabajo (requerimientos de aprobación):

**Transformaciones: Para este MVP no necesitas perfección, ¡necesitas rapidez! ⏩ Vas a hacer estas, y solo estas, transformaciones a los datos:**

- Algunos campos, como belongs_to_collection, production_companies y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, ¡deberán desanidarlos para poder y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien buscar la manera de acceder a esos datos sin desanidarlos.

- Los valores nulos de los campos revenue, budget deben ser rellenados por el número 0.

- Los valores nulos del campo release date deben eliminarse.

- De haber fechas, deberán tener el formato AAAA-mm-dd, además deberán crear la columna release_year donde extraerán el año de la fecha de estreno.

- Crear la columna con el retorno de inversión, llamada return con los campos revenue y budget, dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.

- Eliminar las columnas que no serán utilizadas, video,imdb_id,adult,original_title,poster_path y homepage.

**Desarrollo API: Propones disponibilizar los datos de la empresa usando el framework FastAPI. Las consultas que propones son las siguientes:**

**Deben crear 6 funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).****

- def peliculas_idioma( Idioma: str ): Se ingresa un idioma. Debe devolver la cantidad de películas producidas en ese idioma.
                    Ejemplo de retorno: X cantidad de películas fueron estrenadas en idioma

- def peliculas_duracion( Pelicula: str ): Se ingresa una pelicula. Debe devolver la la duracion y el año.
                    Ejemplo de retorno: X . Duración: x. Año: xx

- def franquicia( Franquicia: str ): Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
                    Ejemplo de retorno: La franquicia X posee X peliculas, una ganancia total de x y una ganancia promedio de xx

- def peliculas_pais( Pais: str ): Se ingresa un país, retornando la cantidad de peliculas producidas en el mismo.
                    Ejemplo de retorno: Se produjeron X películas en el país X

- def productoras_exitosas( Productora: str ): Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo.
                    Ejemplo de retorno: La productora X ha tenido un revenue de x

- def get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.

**Deployment: Conoces sobre Render y tienes un tutorial de Render que te hace la vida mas facil. Tambien podrias usar Railway, o cualquier otro servicio que permita que la API pueda ser consumida desde la web.**


**Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA)**

Ya los datos están limpios, ahora es tiempo de investigar las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías (que no tienen que ser errores necesariamente), y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior. Las nubes de palabras dan una buena idea de cuáles palabras son más frecuentes en los títulos, ¡podría ayudar al sistema de recomendación! En esta ocasión vamos a pedirte que no uses librerías para hacer EDA automático ya que queremos que pongas en practica los conceptos y tareas involucrados en el mismo. Puedes leer un poco más sobre EDA.

**Sistema de recomendación:**

Una vez que toda la data es consumible por la API, está lista para consumir por los departamentos de Analytics y Machine Learning, y nuestro EDA nos permite entender bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas. El EDA debería incluir gráficas interesantes para extraer datos, como por ejemplo una nube de palabras con las palabras más frecuentes en los títulos de las películas. Éste consiste en recomendar películas a los usuarios basándose en películas similares, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas, se ordenarán según el score de similaridad y devolverá una lista de Python con 5 valores, cada uno siendo el string del nombre de las películas con mayor puntaje, en orden descendente. Debe ser deployado como una función adicional de la API anterior y debe llamarse:

- def recomendacion( titulo ): Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.
