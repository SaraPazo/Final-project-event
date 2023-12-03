import streamlit as st
import pandas as pd
from PIL import Image
import webbrowser
import base64
import io
import datetime
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import folium


st.set_page_config(page_title='Tu experiencia - Mapa', page_icon="🌍", layout="wide")

# ----- LOAD COSILLAS ---- 

poster_contact_form = Image.open('../imagenes/poster.jpeg')

# --- head ---


st.image(poster_contact_form, width = 200)

st.title('A dónde te gustaría ir?')

event_map = pd.read_csv('../mapa/csv_map/eventos_map.csv')
madrid_map = pd.read_csv('../mapa/csv_map/madrid_map.csv')
restaurantes_map = pd.read_csv('../mapa/csv_map/restaurantes_map.csv')

map, selection = st.columns(2)

with map:
    st.subheader("¿Tu ubicación en el mapa?")
    st.write("##")
    mapa = folium.Map(location=[40.416709, -3.690286], zoom_start=15)

    for i in range(0, len(restaurantes_map)):
        folium.Marker([float(restaurantes_map.lat[i]), float(restaurantes_map.long[i])], 
                popup=restaurantes_map.nombre[i],
                icon = folium.Icon(color='darkgreen')).add_to(mapa)

    for i in range(0, len(event_map)):
        folium.Marker([float(event_map.lat[i]), float(event_map.long[i])], 
                popup = event_map.nombre[i],
                icon = folium.Icon(color='red')).add_to(mapa)

    st_folium(mapa, height = 550, width = 1200)


with selection:
    
    st.header('¿Cuál es tu barrio favorito?')

    barrio, precio = st.columns(2)

    with barrio:
        sel1 = st.multiselect('Elige tu barrio', event_map.barrio.unique())

    with precio:
        sel2 = st.selectbox('Elige rango de precio', event_map.precio.unique())

    
    evento = event_map[(event_map.barrio.isin(sel1)) & (event_map.precio == sel2)]

    if not evento.empty:
        # Mostrar el DataFrame resultante
        def_event = evento[['nombre', 'barrio', 'precio']]
        st.dataframe(def_event, width = 700)

    else:
        # Mostrar un mensaje indicando que no hay resultados
        st.write("No hay eventos que cumplan con los criterios seleccionados.")


    st.write("----")        # Crea una linea divisoria

    barrio, precio = st.columns(2)

    rest = restaurantes_map[(restaurantes_map.barrio.isin(sel1))]

    with barrio:
        sel1 = st.multiselect('Elige tu barrio', restaurantes_map.barrio.unique())

    with precio:
        sel2 = st.selectbox('Elige rango de precio', restaurantes_map.precio.unique())

    restaurante = restaurantes_map[(restaurantes_map.barrio.isin(sel1)) & (restaurantes_map.precio == sel2)]

    if not restaurante.empty:
        # Mostrar el DataFrame resultante
        def_restaurante = restaurante[['nombre', 'barrio', 'precio']]
        st.dataframe(def_restaurante, width = 700)

    else:
        # Mostrar un mensaje indicando que no hay resultados
        st.write("No hay eventos que cumplan con los criterios seleccionados.")
    

