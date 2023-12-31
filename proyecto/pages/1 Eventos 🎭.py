import streamlit as st
import pandas as pd
from PIL import Image
import webbrowser
import base64
import io
import datetime


st.set_page_config(page_title='Tu experiencia - Eventos', page_icon="🎭", layout="wide")


# ----- LOAD COSILLAS ---- 

entradas_contact_form = Image.open('./imagenes/entradas.jpeg')
estrella_contact_form = Image.open('./imagenes/estrella.jpeg')

# --- head ---


# Imagen a la izquierda
st.image(entradas_contact_form, width=200)


# Título de la presentación
st.markdown(

    """
    <h1 style='font-size: 50px; color: #001F3F; opacity: 0.8;'>¿ Qué te gustaría ver ?
    </h1>
    """,
    unsafe_allow_html=True
)


event = pd.read_csv('./csv/eventos_fin.csv')

# Dynamic price range
price_min, price_max = event.precio.min(), event.precio.max()

barrio, precio, mes, dia = st.columns(4)

barrio_ordenado = sorted(event.barrio.unique())
meses_ordenados = sorted(event.mes.unique())
dias_ordenados = sorted(event.dia.unique().tolist())

with barrio:
    sel1 = st.multiselect('Elige tu barrio', barrio_ordenado)

with precio:
    sel2 = st.slider('Rango de precio', price_min, price_max, (price_min, price_max))
                            
with mes:
    sel3 = st.selectbox('En qué mes estás pensando?', meses_ordenados)

with dia:
    sel4 = st.multiselect('Y... qué día te viene bien?', dias_ordenados)



evento = event[(event.barrio.isin(sel1)) & (event.precio.between(sel2[0], sel2[1])) & (event.mes == sel3) & (event.dia.isin(sel4))]

if not evento.empty:
    # Mostrar el DataFrame resultante
    def_event = evento[['nombre', 'local', 'barrio', 'ubicacion', 'precio', 'mes', 'dia', 'enlace']]

    # Crear columna de enlaces clicables
    def_event['enlace_clicable'] = def_event['enlace'].apply(lambda url: f'[{url}]({url})')

    # Mostrar DataFrame usando st.write y Markdown
    st.write(def_event[['nombre', 'local', 'barrio', 'ubicacion', 'precio', 'mes', 'dia', 'enlace_clicable']].to_markdown(index=False), unsafe_allow_html=True)


else:
    # Mostrar un mensaje indicando que no hay resultados
    st.write("No hay eventos que cumplan con los criterios seleccionados.")

