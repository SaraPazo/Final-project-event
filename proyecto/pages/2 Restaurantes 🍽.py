import streamlit as st
import pandas as pd
from PIL import Image
import webbrowser
import base64
import io
import datetime



st.set_page_config(page_title='Tu experiencia - Restaurantes', page_icon="🍽️", layout="wide")


# ----- LOAD COSILLAS ---- 

tripadvisor = Image.open('./imagenes/trip.jpeg')

# --- head ---

st.image(tripadvisor, width = 120)

# Título de la presentación
st.markdown(

    """
    <h1 style='font-size: 50px; color: #001F3F; opacity: 0.8;'>Y, ¿ dónde quieres comer ?
    </h1>
    """,
    unsafe_allow_html=True
)



rest = pd.read_csv('./csv/restaurante_fin.csv')


barrio, gastronomia, precio  = st.columns(3)

barrio_ordenado = sorted(rest.barrio.unique())
gastro_ordenado = sorted(rest.gastronomia.unique())

rest['precio_orden'] = rest['precio'].map({'Bajo': 1, 'Medio': 2, 'Alto': 3})
precio_ordenado = sorted(rest['precio'].unique(), key=lambda x: rest['precio_orden'][rest['precio'] == x].iloc[0])


with barrio:
    sel1 = st.multiselect('Elige barrio', barrio_ordenado)

with gastronomia:
    sel2 = st.multiselect('Elige estilo de comida', gastro_ordenado)

with precio:
    sel3 = st.multiselect('Elige rango de precio', precio_ordenado)


restaurante = rest[(rest.barrio.isin(sel1)) & (rest.gastronomia.isin(sel2)) & (rest.precio.isin(sel3))]


if not restaurante.empty:

    def_rests = restaurante[['restaurante','barrio', 'gastronomia', 'ubicacion', 'precio', 'reseña']].to_markdown(index=False)

    # Mostrar DataFrame con ancho personalizado
    st.write(def_rests, width=1000)

else:
    # Mostrar un mensaje indicando que no hay resultados
    st.write("No hay restaurantes que cumplan con los criterios seleccionados.")

