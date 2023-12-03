import streamlit as st
import pandas as pd
from PIL import Image
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title='Tu experiencia - Mapa', page_icon="🌍", layout="wide")

# ----- LOAD COSILLAS ---- 

poster_contact_form = Image.open('../imagenes/poster.jpeg')

# --- head ---
st.image(poster_contact_form, width=200)
st.title('A dónde te gustaría ir?')

event_map = pd.read_csv('../mapa/csv_map/eventos_map.csv')
madrid_map = pd.read_csv('../mapa/csv_map/madrid_map.csv')
restaurantes_map = pd.read_csv('../mapa/csv_map/restaurantes_map.csv')

map, selection = st.columns(2)


st.subheader("¿Tu ubicación en el mapa?")
st.write("##")
mapa = folium.Map(location=[40.416709, -3.690286], zoom_start=15)

selected_barrios = st.selectbox('Elige tu barrio', event_map.barrio.unique())

markers = []

for i in range(0, len(restaurantes_map)):
    if restaurantes_map.barrio[i] in selected_barrios:
        popup_text = f"{restaurantes_map.nombre[i]}\nPrecio: {restaurantes_map.precio[i]}"
        folium.Marker([float(restaurantes_map.lat[i]), float(restaurantes_map.long[i])],
                        popup=folium.Popup(popup_text, parse_html=True),
                        icon=folium.Icon(color='green')).add_to(mapa)
        markers.append([float(restaurantes_map.lat[i]), float(restaurantes_map.long[i])])

for i in range(0, len(event_map)):
    if event_map.barrio[i] in selected_barrios:
        popup_text = f"{event_map.nombre[i]}\nPrecio: {event_map.precio[i]}"
        folium.Marker([float(event_map.lat[i]), float(event_map.long[i])],
                        popup=folium.Popup(popup_text, parse_html=True),
                        icon=folium.Icon(color='blue')).add_to(mapa)
        markers.append([float(event_map.lat[i]), float(event_map.long[i])])

if markers:
    # Calcular el centroide de los marcadores seleccionados
    center_lat = sum(coord[0] for coord in markers) / len(markers)
    center_long = sum(coord[1] for coord in markers) / len(markers)

    # Ajustar la ubicación del mapa al centroide
    mapa.location = [center_lat, center_long]

st_folium(mapa, height=650, width=1700)
