# Proyect: Tu experiencia en Madrid

![imagen](https://github.com/SaraPazo/Final-project-event/blob/main/proyecto/imagenes/madrid.png)


## Indice:
1.[📜 Descripción](#descripcion)\
2.[💡 Estructura](#estructura)\
3.[⏳ Paso a paso](#pasos)\
4.[📈 Resultado](#resultado)\
5.[⏭️ Next Steps](#next)\
6.[📁 Estructura](#Estructura)




## Descripción: <a name="descripcion"/></a>

jhgvugvgjhjhgb


## Estructura: <a name="estructura"/></a>

1) Las carpetas **entradas** y **restaurantes**, son las principales para la ETL, ya que en estas se encuentra el código para la extracción de los datos, transformación y su limpieza.
2) La carpeta **proyecto** contiene lo siguiente:
- **.streamlit**: contiene la configuración de la web que se ha creado.
- **csv**: contiene los archivos .csv que han sido utilizados para la visualización.
- **imagenes**: las imágenes que han sido utilizadas.
- **mapa**

    - **csv_map**: contiene más archivos .csv que han sido utilizados para la visualización.
    - **barrios-madrid.geoson**: contiene un archivo geoson que he utilizado para encontrar las localizaciones exactas dentro de Madrid.
    - **folium** y **madrid**: código para la búsqueda y limpieza de los datos de mapas. 

- **paginas**: contiene el código utilizado para las distintas páginas de streamlit.


## Paso a paso: <a name="pasos"/></a>

### ETL

El proceso de extracción de datos se ha hecho a través de la técnica de webscraping combinando selenium y beautiful soup.

Los datos han sido recogidos en la web de entradas.com (para los **eventos**), y en tripadvisor.com (para la búsqueda de **restaurantes**).

Además, he utilizado también el método de webscraping para la búsqueda de las localizaciones, tanto de eventos como restaurantes, llamando al buscador principal de Google, por Ubicación.

Tras la extracción de los datos, se sigue con su limpieza, hasta conseguir unos datos en los que la relación principal entre tanto eventos como restaurantes tengan una columna común: el **barrio**. 


### VISUALIZACIÓN

He usado Streamlit 

--> subir el video de stream



## Next Steps: <a name="next"/></a>

Los siguientes avances para continuar y mejorar este proyecto son los siguientes:

- Ampliar los datos a partir de una extracción más amplia y efectiva, además de ampliar los filtros posibles.
- Mejorar la limpieza de localizaciones con la herramienta Geopy, tanto para restaurantes como para eventos.
- BONUS: Recomendación por usuarios con gustos similares. 