import streamlit as st
import pandas as pd
from PIL import Image
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title='Tu experiencia - Mapa', page_icon="🌍", layout="wide")

# ----- LOAD COSILLAS ---- 
poster_contact_form = Image.open('./imagenes/poster.jpeg')
tripadvisor = Image.open('./imagenes/trip.jpeg')
estrella_contact_form = Image.open('./imagenes/estrella.jpeg')

event_map = pd.read_csv('./mapa/csv_map/eventos_map.csv')
madrid_map = pd.read_csv('./mapa/csv_map/madrid_map.csv')
restaurantes_map = pd.read_csv('./mapa/csv_map/restaurantes_map.csv')

# --- head ---
st.image(poster_contact_form, width=120)

# Título de la presentación
st.markdown(

    """
    <h1 style='font-size: 50px; color: #001F3F; opacity: 0.8;'>¡Dime a dónde vas, y te diré qué tenemos!
    </h1>
    """,
    unsafe_allow_html=True
)


st.write("##")
mapa = folium.Map(location=[40.416709, -3.690286], zoom_start=15)


selected_barrios = st.multiselect('Elige tu zona favorita', madrid_map.barrio.unique())

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

st_folium(mapa, height = 700, width=1700)

st.write("----")  # Crea una línea divisoria


# subtitulo
st.markdown(
    """
    <h5 style='font-size: 40px; color: #001F3F; opacity: 0.8;'>¿Qué tenemos disponible?
    </h5>
    """,
    unsafe_allow_html=True
)


eventos, espacio1, estrella, restaurantes, espacio2, trip = st.columns(6)
# Mostrar las imágenes en columnas


with eventos:
    # subtitulo
    st.markdown(
        """
        <h5 style='font-size: 30px; color: #001F3F; opacity: 0.8;'>¡Eventos disponibles!
        </h5>
        """,
        unsafe_allow_html=True
    )

with espacio1:
    st.write('##')
             
with estrella:
    st.image(estrella_contact_form, width=70)


with restaurantes:
    # subtitulo
    st.markdown(
        """
        <h5 style='font-size: 30px; color: #001F3F; opacity: 0.8;'>¡Restaurantes disponibles!
        </h5>
        """,
        unsafe_allow_html=True
    )

with espacio2:
    st.write('##')

with trip:
    st.image(tripadvisor, width = 100)



evento, restaurante = st.columns(2)

with evento:

    evento = event_map[event_map.barrio.isin(selected_barrios)]

    if not evento.empty:
        # Mostrar el DataFrame resultante
        def_event = evento[['nombre', 'barrio', 'local', 'precio']]
        st.dataframe(def_event, width=700)

    else:
        # Mostrar un mensaje indicando que no hay resultados
        st.write("No hay eventos que cumplan con los criterios seleccionados.")


with restaurante:

    rest = restaurantes_map[restaurantes_map.barrio.isin(selected_barrios)]

    if not rest.empty:
        # Mostrar el DataFrame resultante
        def_restaurante = rest[['nombre', 'barrio','gastronomia', 'precio']]
        st.dataframe(def_restaurante, width=700)

    else:
        # Mostrar un mensaje indicando que no hay resultados
        st.write("No hay restaurantes que cumplan con los criterios seleccionados.")
