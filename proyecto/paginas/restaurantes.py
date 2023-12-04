import streamlit as st
import pandas as pd
from PIL import Image
import webbrowser
import base64
import io
import datetime



st.set_page_config(page_title='Tu experiencia - Restaurantes', page_icon="🍽️", layout="wide")


# ----- LOAD COSILLAS ---- 

tripadvisor = Image.open('../imagenes/trip.jpeg')

# --- head ---

st.image(tripadvisor, width = 150)

st.title('¿Dónde comemos?')

rest = pd.read_csv('../csv/restaurante_fin.csv')

barrio, gastronomia, precio  = st.columns(3)

with barrio:
    sel1 = st.multiselect('Elige barrio', rest.barrio.unique())

with gastronomia:
    sel2 = st.multiselect('Elige estilo de comida', rest.gastronomia.unique())

with precio:
    sel3 = st.selectbox('Elige rango de precio', rest.precio.unique())


restaurante = rest[(rest.barrio.isin(sel1)) & (rest.gastronomia.isin(sel2)) & (rest.precio == sel3)]

def_rests = restaurante[['restaurante','barrio','ubicacion', 'precio', 'reseña']]

# Mostrar DataFrame con ancho personalizado
st.dataframe(def_rests, width=700)

