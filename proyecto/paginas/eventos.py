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

# Dynamic price range
price_min, price_max = event.precio.min(), event.precio.max()

barrio, precio, mes, dia = st.columns(4)

with barrio:
    sel1 = st.multiselect('Elige tu barrio', event.barrio.unique())

with precio:
    sel2 = st.slider('Rango de precio', price_min, price_max, (price_min, price_max))
                            
with mes:
    sel3 = st.selectbox('En qué mes estás pensando?', event.mes.unique())

with dia:
    sel4 = st.multiselect('Y... qué día te viene bien?', event.dia.unique().tolist())


evento = event[(event.barrio.isin(sel1)) & (event.precio.between(sel2[0], sel2[1])) & (event.mes == sel3) & (event.dia.isin(sel4))]

if not evento.empty:
    # Mostrar el DataFrame resultante
    def_event = evento[['nombre', 'local', 'barrio', 'ubicacion', 'precio', 'mes', 'dia', 'enlace']]

    # Crear una nueva columna con enlaces clicables utilizando Markdown
    def_event['enlace_clicable'] = def_event['enlace'].apply(lambda url:f"{url}")

    # Mostrar los enlaces clicables utilizando st.markdown
    #for enlace in def_event['enlace_clicable']:
       # st.markdown(enlace, unsafe_allow_html=True)

    # También puedes mostrar la tabla con los enlaces
    st.write(def_event[['nombre', 'local', 'barrio', 'ubicacion', 'precio', 'mes', 'dia', 'enlace_clicable']], unsafe_allow_html=True)

#html = f"<a href='{url}'><img src='data:image/png;base64,{plot_url}'></a>"
#st.markdown(html, unsafe_allow_html=True)


else:
    # Mostrar un mensaje indicando que no hay resultados
    st.write("No hay eventos que cumplan con los criterios seleccionados.")
