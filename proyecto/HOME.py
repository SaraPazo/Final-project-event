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



# Configuración de la página
st.set_page_config(
    page_title='Crea Tu Experiencia',
    page_icon="😉",
    layout="wide",
    initial_sidebar_state="expanded")


# ----- LOAD IMAGENES ---- 

amanece_contact_form = Image.open('../proyecto/imagenes/Amanece.jpeg')
madrid_contact_form = Image.open('../proyecto/imagenes/madrid.png')
spainPost_contact_form = Image.open('../proyecto/imagenes/SpainPostcard.jpeg')
conci_contact_form = Image.open('../proyecto/imagenes/conci.png')
paella2_contact_form = Image.open('../proyecto/imagenes/paella.jpeg')


# ---- HEADER ---- 

st.image(madrid_contact_form , width = 1300)

# Título de la presentación
st.markdown(

    """
    <h1 style='font-size: 60px; color: #001F3F; opacity: 0.8;'>¿QUIERES DISEÑAR TU PROPIA EXPERIENCIA?
    </h1>
    """,
    unsafe_allow_html=True
)


# Introducción
st.header("##")

st.markdown(

    """
    <h5 style='font-size: 20px; color: #333333;'>Madrid, la capital de España, es una ciudad rica en cultura, historia y, por supuesto, gastronomía. 
    En esta presentación, te llevaremos a un viaje por la vibrante escena de eventos y restaurantes de Madrid, 
    permitiéndote crear tu plan perfecto para disfrutar al máximo de esta maravillosa ciudad.
    </h5>
    """,
    unsafe_allow_html=True
)

# ------ HISTORIA ------

historia, imagen = st.columns(2)

with historia:
    st.header('##')
    # subtitulo
    st.markdown(
        """
        <h5 style='font-size: 40px; color: #001F3F; opacity: 0.8;'>Historia del Ocio y Gastronomía en Madrid
        </h5>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h6 style='font-size: 18px; color: #666666; text-align: justify;'>Madrid ha sido durante mucho tiempo un epicentro de actividad cultural y gastronómica en España. 
        Desde sus animadas plazas hasta sus estrechas calles llenas de historia, la ciudad ha sido testigo 
        de eventos que han dejado una marca indeleble en su paisaje cultural.
        </h6>
        <h6 style='font-size: 18px; color: #666666; text-align: justify;'>La cultura del tapeo, donde disfrutar de pequeñas porciones de deliciosa comida con amigos, es una 
        tradición arraigada en la vida madrileña. Los bares y tabernas ofrecen una amplia variedad de tapas, 
        desde clásicas como la tortilla española hasta creaciones modernas que fusionan sabores tradicionales 
        con toques contemporáneos.
        </h6>
        <h6 style='font-size: 18px; color: #666666; text-align: justify;'> En cuanto a eventos, Madrid acoge festivales, conciertos y exposiciones a lo largo del año. Desde la 
        Feria del Libro en el Parque del Retiro hasta conciertos en el Teatro Real, hay algo para todos los gustos 
        y preferencias culturales.
        </h6>
        """,
        unsafe_allow_html=True
    )

with imagen:
    st.header('##')
    st.header('##')
    st.image(amanece_contact_form, width=650)


# ---- Columas en las que hablaré sobre las múltiples opciones de ocio y disfrute gastronómico en Madrid ----


imagen, eventos = st.columns(2)

with eventos:
    st.header('##')
    # subtitulo
    st.markdown(
        """
        <h5 style='font-size: 35px; color: #001F3F; opacity: 0.8;'>¿Te gusta disfrutar de tu tiempo libre y estás en Madrid?
        </h5>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h6 style='font-size: 18px; color: #666666; text-align: justify;'>¡Bienvenido a la experiencia de Madrid como nunca antes! ¿Te imaginas tener acceso a los eventos más vibrantes de la ciudad al alcance de un clic? Con nuestra herramienta, explorar y comprar entradas en entradas.com se convierte en una emocionante travesía. Desde conciertos íntimos hasta festivales épicos, podrás descubrir y asegurar tus boletos para los eventos más exclusivos de Madrid. ¡Tu entrada a la diversión comienza aquí!
        <h6>
        """,
        unsafe_allow_html=True
    )

with imagen:
    st.image(conci_contact_form, width = 650)


rest, imagen = st.columns(2)

with rest:
    st.write("##")
    # subtitulo
    st.markdown(
        """
        <h5 style='font-size: 35px; color: #001F3F; opacity: 0.8;'>¿Y si te ofrezco un antes o un después gastronómico?
        </h5>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h6 style='font-size: 18px; color: #666666; text-align: justify;'>Mientras esperas, o al terminar el evento, embárcate en un viaje culinario a través de la rica escena gastronómica de Madrid con nuestra herramienta. Nos asociamos con TripAdvisor.com para llevarte a los restaurantes y bares más elogiados de la ciudad. Desde acogedores rincones locales hasta restaurantes de renombre, cada elección es una promesa de delicias para tu paladar. ¡Deja que Madrid te conquiste a través de su sabor, y nosotros te guiamos en cada exquisita elección!"
        <h6>
        <h6 style='font-size: 18px; color: #666666; text-align: justify;'>Acompáñanos en este recorrido virtual por los barrios de Madrid, donde descubrirás eventos emocionantes 
        y restaurantes encantadores que te permitirán sumergirte en la rica vida cultural y gastronómica de la ciudad.
        </h6>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
    """
    <h6 style='font-size: 25px; color: #666666;'>¿Suena interesante? ¡¡Te invito a comenzar conmigo la búsqueda de tu experiencia perfecta!!
    <h6>
    """,
    unsafe_allow_html=True
    )

with imagen:
    st.image(paella2_contact_form, width=630)
    