import streamlit as st
import pandas as pd
from PIL import Image
import webbrowser
import base64
import io
import datetime


st.set_page_config(page_title='Tu experiencia - Eventos', page_icon="🎭", layout="wide")


# ----- LOAD COSILLAS ---- 

entradas_contact_form = Image.open('../imagenes/entradas.jpeg')

# --- head ---


st.image(entradas_contact_form, width = 200)

st.title('¿Qué te gustaría hacer?')

event = pd.read_csv('../csv/eventos_fin.csv')

barrio, mes, dia = st.columns(3)

with barrio:
    sel1 = st.multiselect('Elige tu barrio', event.barrio.unique())

with mes:
    sel2 = st.selectbox('En qué mes estás pensando?', event.mes.unique())

with dia:
    sel3 = st.multiselect('Y... qué día te viene bien?', event.dia.unique().tolist())


evento = event[(event.barrio.isin(sel1)) & (event.mes == sel2) & (event.dia.isin(sel3))]

if not evento.empty:
    # Mostrar el DataFrame resultante
    def_event = evento[['nombre', 'local', 'barrio', 'ubicacion', 'precio', 'mes', 'dia', 'enlace']]

    # Crear una nueva columna con enlaces clicables
    def_event['enlace_clicable'] = def_event['enlace'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')

    # Mostrar el DataFrame con la columna de enlaces clicables
    st.write(def_event[['nombre', 'local', 'barrio', 'ubicacion', 'precio', 'mes', 'dia', 'enlace_clicable']], unsafe_allow_html=True)
else:
    # Mostrar un mensaje indicando que no hay resultados
    st.write("No hay eventos que cumplan con los criterios seleccionados.")
