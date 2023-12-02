
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

# ---- HEADER ---- 

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


