
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

st.set_page_config(page_title='Crea Tu Experiencia', page_icon="🥁", layout="wide")

# ----- LOAD COSILLAS ---- 


amanece_contact_form = Image.open('../imagenes/Amanece.jpg')
terraza_contact_form = Image.open('../imagenes/Terraza.jpg')


# ---- HEADER ---- 

st.image(amanece_contact_form, use_column_width = True)

st.title("Crea tu propia experiencia completa!")
st.subheader("En Madrid!")


# ---- Columas en las que hablaré sobre las múltiples opciones de ocio y disfrute gastronómico en Madrid ----


with st.container():
    st.write("----")        # Crea una linea divisoria

    left_column, right_column = st.columns(2)
    with left_column:
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



col1, col2 = st.columns(2)
with col1:
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
    
    st.image(amanece_contact_form)

    
with col2:
    st.image(terraza_contact_form)
    st.header('A los madrileños nos llaman Gatos')
    st.write('El motivo por el que nos llaman, o nos llamamos a nosotros mismos, gatos no es la presencia masiva de felinos en la ciudad. De hecho, no está del todo claro el por qué del nombre. Pero hay una leyenda que parece explicarlo. Se dice que los cristianos que, en el siglo XI, vinieron a conquistar la ciudad, en poder de los musulmanes, se valieron de la habilidad de un vecino que era capaz de trepar las murallas por la parte más complicada y por tanto menos vigilada. Tras silenciar a la guardia, el joven, apodado el Gato, abrió las puertas de la ciudad y facilitó la conquista. La palabra Gato cobró el significado de valiente y más tarde se asimiló con los nacidos en la ciudad. El muchacho adoptó la palabra Gato en su apellido y de él se derivó un linaje duradero y conocido en la villa.')

""""
LOGO ENTRADAS.COM
https://www.entradas.com/obj/media/ES-eventim/specialLogos/checkoutApp/logo.svg

"""
