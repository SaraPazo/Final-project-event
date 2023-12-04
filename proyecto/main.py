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
import toml
import importlib


st.set_page_config(page_title='Crea Tu Experiencia', page_icon="😉", layout="wide")

#find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/


# ----- LOAD COSILLAS ---- 

amanece_contact_form = Image.open('../proyecto/imagenes/Amanece.jpeg')
terraza_contact_form = Image.open('../proyecto/imagenes/Terraza.jpeg')
paella_contact_form = Image.open('../proyecto/imagenes/paella.jpeg')
madrid_contact_form = Image.open('../proyecto/imagenes/madrid.png')
spainPost_contact_form = Image.open('../proyecto/imagenes/SpainPostcard.jpeg')


# ---- MENU ---- 


def main():
    # Cargar la configuración desde el archivo TOML
    config = toml.load(".streamlit/pages.toml")

    # Barra lateral como menú de navegación
    st.sidebar.title('Menú de Navegación')

    # Mostrar el menú con las páginas definidas en el archivo TOML
    seleccion_pagina = st.sidebar.radio('Ir a:', [pagina["name"] for pagina in config["pages"]])

    # Importar y mostrar la página seleccionada
    for pagina in config["pages"]:
        if pagina["name"] == seleccion_pagina:
            modulo = importlib.import_module(pagina["path"].replace(".py", "").replace("/", "."))
            modulo.mostrar_pagina()

if __name__ == '__main__':
    main()

# ---- HEADER ---- 

st.image(spainPost_contact_form , use_column_width = True)

st.sidebar.header('Menu Lateral')

# Título de la presentación
st.title('Explora Madrid: Eventos y Gastronomía')

# Introducción
st.markdown(
    """
    Madrid, la capital de España, es una ciudad rica en cultura, historia y, por supuesto, gastronomía. 
    En esta presentación, te llevaremos a un viaje por la vibrante escena de eventos y restaurantes de Madrid, 
    permitiéndote crear tu plan perfecto para disfrutar al máximo de esta maravillosa ciudad.
    """
)
historia, imagen = st.columns(2)

with historia:
    # Breve Historia
    st.header('Historia del Ocio y Gastronomía en Madrid')

    st.markdown(
        """
        Madrid ha sido durante mucho tiempo un epicentro de actividad cultural y gastronómica en España. 
        Desde sus animadas plazas hasta sus estrechas calles llenas de historia, la ciudad ha sido testigo 
        de eventos que han dejado una marca indeleble en su paisaje cultural.

        La cultura del tapeo, donde disfrutar de pequeñas porciones de deliciosa comida con amigos, es una 
        tradición arraigada en la vida madrileña. Los bares y tabernas ofrecen una amplia variedad de tapas, 
        desde clásicas como la tortilla española hasta creaciones modernas que fusionan sabores tradicionales 
        con toques contemporáneos.

        En cuanto a eventos, Madrid acoge festivales, conciertos y exposiciones a lo largo del año. Desde la 
        Feria del Libro en el Parque del Retiro hasta conciertos en el Teatro Real, hay algo para todos los gustos 
        y preferencias culturales.

        Acompáñanos en este recorrido virtual por los barrios de Madrid, donde descubrirás eventos emocionantes 
        y restaurantes encantadores que te permitirán sumergirte en la rica vida nocturna y gastronómica de la ciudad.
        """
    )

with imagen:
    st.header('A los madrileños nos llaman Gatos')
    st.image(amanece_contact_form, width=600)


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

