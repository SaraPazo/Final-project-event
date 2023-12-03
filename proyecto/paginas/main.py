
import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import datetime
import time
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import folium


#find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(page_title='Crea Tu Experiencia', page_icon="😉", layout="wide")

# ----- LOAD COSILLAS ---- 

amanece_contact_form = Image.open('../imagenes/Amanece.jpeg')
terraza_contact_form = Image.open('../imagenes/Terraza.jpeg')
paella_contact_form = Image.open('../imagenes/paella.jpeg')
madrid_contact_form = Image.open('../imagenes/madrid.jpeg')
spainPost_contact_form = Image.open('../imagenes/SpainPostcard.jpeg')
spain_contact_form = Image.open('../imagenes/Spain.jpeg')


# ---- HEADER ---- 

st.image(spainPost_contact_form , use_column_width = True)

st.sidebar.header('Menu Lateral')

st.title("Welcome to Madrid!")


# ---- Columas en las que hablaré sobre las múltiples opciones de ocio y disfrute gastronómico en Madrid ----


with st.container():
    st.write("----")        # Crea una linea divisoria

text, imagen = st.columns(2)

with text:
    st.header("¿Te gusta disfrutar de tu tiempo libre y estás en Madrid?")
    st.write("##")
    st.write(
        """
        Madrid es una ciudad llena de culturas
        mucho ocio 
        restauracion
        gente
        ganas de pasarlo bien

        ¿Suena interesante? 

        ¡¡Te invito a comenzar conmigo la búsqueda de tu experiencia perfecta!!
        """)
    st.header('Madrid también tiene una estatua de la Libertad')
    
    st.write('Es verdad y se trata de una de las curiosidades de Madrid más sorprendentes. Madrid tiene una estatua de la libertad, creada por el escultor aragonés Ponciano Ponzano, el mismo que esculpió los leones del Congreso. La creó en 1853. Es decir, unos veinte años antes de la de Frédéric Auguste Bartholdi, que acabó siendo un regalo del gobierno francés a los Estados Unidos. La estatua de la libertad española es más pequeña, de unos dos metros de altura, y toda de mármol blanco. Para verla sólo hay que entrar al Panteón de Hombres Ilustres, uno de los museos más curiosos de la ciudad.')
    
    st.image(paella_contact_form, width=500)


with imagen:
    st.header('A los madrileños nos llaman Gatos')
    st.image(amanece_contact_form, width=600)


""""
LOGO ENTRADAS.COM
https://www.entradas.com/obj/media/ES-eventim/specialLogos/checkoutApp/logo.svg

"""



import pandas as pd

# Supongamos que tienes un DataFrame llamado 'datos'
datos = pd.read_csv('../csv/restaurante_fin.csv')

# Insertar y hacer selecciones de filas en una columna específica
columna_seleccionada = st.multiselect('Selecciona la columna', datos.gastronomia)
valor_seleccionado = st.multiselect(f'Selecciona un valor en {columna_seleccionada}', datos[columna_seleccionada].unique())

# Filtrar el DataFrame basado en la selección
datos_filtrados = datos[datos[columna_seleccionada] == valor_seleccionado]

# Mostrar el DataFrame resultante
st.dataframe(datos_filtrados)
