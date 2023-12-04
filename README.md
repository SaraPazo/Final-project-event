# Proyect: Tu experiencia en Madrid

![imagen](https://github.com/SaraPazo/Final-project-event/blob/main/proyecto/imagenes/madrid.png)


## Indice:
1.[📝 Descripción](#descripcion)\
2.[🏛 Estructura](#estructura)\
3.[📈 Resultado](#resultado)\
4.[🔮 Next Steps](#next)\


## 1. Descripción: <a name="descripcion"/></a>

El objetivo de mi proyecto final es crear una herramienta que disponga al consumidor información sobre los eventos y restaurantes en los diferentes barrios de Madrid, con el objetivo de facilitar a los usuarios la planificación de una experiencias completa totalmente personalizada.

Esta aplicación mostrará la opción de saber qué eventos hay disponibles en el barrio que el consumidor elija, y dónde puede reservar para comer, cenar o tomar algo en el mismo barrio donde se lleva a cabo el evento escogido!

La solución que aporta esta herramienta:

- ¿A qué evento deseas acudir?
- ¿Qué restaurantes o bares tendrás cerca del evento al que vas a acudir?

## 2. Estructura: <a name="estructura"/></a>

a) Las carpetas **entradas** y **restaurantes**, son las principales para la ETL, ya que en estas se encuentra el código para la extracción de los datos, transformación y su limpieza.

b) La carpeta **proyecto** contiene lo siguiente:
- **.streamlit**: contiene la configuración de la web que se ha creado.
- **csv**: contiene los archivos .csv que han sido utilizados para la visualización.
- **imagenes**: las imágenes que han sido utilizadas.
- **mapa**

    - **csv_map**: contiene más archivos .csv que han sido utilizados para la visualización.
    - **barrios-madrid.geoson**: contiene un archivo geoson que he utilizado para encontrar las localizaciones exactas dentro de Madrid.
    - **folium** y **madrid**: código para la búsqueda y limpieza de los datos de mapas. 

- **paginas**: contiene el código utilizado para las distintas páginas de streamlit.


## 3. Paso a paso: <a name="pasos"/></a>

### ETL

El proceso de extracción de datos se ha hecho a través de la técnica de webscraping combinando selenium y beautiful soup.

Los datos han sido recogidos en la web de entradas.com (para los **eventos**), y en tripadvisor.com (para la búsqueda de **restaurantes**).

Además, he utilizado también el método de webscraping para la búsqueda de las localizaciones, tanto de eventos como restaurantes, llamando al buscador principal de Google, por Ubicación.

Tras la extracción de los datos, se sigue con su limpieza, hasta conseguir unos datos en los que la relación principal entre tanto eventos como restaurantes tengan una columna común: el **barrio**. 


### VISUALIZACIÓN

He usado Streamlit como herramienta de uso para que el consumidor pueda crear su experiencia completa. 

- **main**: muestra una breve descripción de Madrid centrado en su ocio y gastronomía.

- **Eventos 🎭**: proporciona al consumidor la selección de:
    
    - Barrio en el que le interesa buscar un evento.
    - Rango de precio que está dispuesto a pagar.
    - Mes
    - Día

    Mediante esta selección, podrá observar los **eventos** disponibles, el **local** en el que se celebra, así como su **ubicación** exacta y el **precio** de salida de las entradas. Además, se le dispone el **link** a la página donde directamente puede realizar su compra. 

- **Restaurantes 🍽️**: proporciona al consumidor la selección de:

    - Barrio en el que le interesa buscar un restaurante ó bar. 
    - Estilo de comida.
    - Rango de precio que está dispuesto a pagar.

    Mediante esta selección, podrá observar los **restaurantes** disponibles, el **estilo** de comida el **barrio** en el que se encuentra, así como su **ubicación** exacta y el **rango de precio** . Además, se le dispone el **link** a la página donde directamente puede realizar su compra. 

- **Mapas 🌍**: proporciona al consumidor la selección de:

    - Barrio en el que le interesa crear su experiencia al completo! 

   Mediante esta selección, se podrán observar los **eventos** disponibles, el **local** en el que se celebra y el **rango de precio** de salida de las entradas. 

   Por otro lado, se podrán observar los **restaurantes** disponibles en el mismo barrio, el **estilo gastronómico** y el **rango de precio**. 

**¡De esta forma, el usuario puede realmente crear su experiencia al completo de forma rápida y sencilla!**



--> subir el video de streamlit



## 4. Next Steps: <a name="next"/></a>

Los siguientes avances para continuar y mejorar este proyecto son los siguientes:

- Ampliar los datos a partir de una extracción más amplia y efectiva, además de ampliar los filtros posibles.
- Mejorar la limpieza de localizaciones con la herramienta Geopy, tanto para restaurantes como para eventos.
- BONUS: Recomendación por usuarios con gustos similares. 