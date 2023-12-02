import requests as req
import pandas as pd
import numpy as np
import re
import statistics as stats

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
PATH = 'driver/chromedriver'

import tqdm
from bs4 import BeautifulSoup
import time
import re
import json

import warnings
warnings.filterwarnings('ignore')


def df_event(lst):
    # Lista para almacenar los datos
    data = []

    # Iterar sobre la lista principal
    for eventos in lst:
        # Iterar sobre cada sublista de eventos
        for evento in eventos:
            # Desglosar la información del evento
            for i in range(len(evento[0])):
                nombre = evento[0][i]
                fecha = evento[1][i]
                ubicacion = evento[2][i]
                precio = evento[3][i]
                enlace = evento[4][i]

                # Crear un diccionario con la información del evento
                evento_dict = {
                    'Nombre': nombre,
                    'Fecha': fecha,
                    'Ubicacion': ubicacion,
                    'Precio': precio,
                    'Enlace': enlace
                }

                # Agregar el diccionario a la lista de datos
                data.append(evento_dict)

    return data