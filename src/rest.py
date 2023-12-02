def extraer(url):

    global table

    while True:
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(4)

        print('entro')

        # paso 2: cookies
        time.sleep(2)

        try:
            aceptar = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
            aceptar.click()
        except:
            print('ok')

        # paso 3: obtener tabla

        time.sleep(4)

        print('0')

        cartas = []

        try:
            for e in range(len(driver.find_elements((By.XPATH, './/div[@class="yJIls z y M0"]')))):
                box = driver.find_elements(By.XPATH, './/div[@class="yJIls z y M0"]')[e].text.split('\n')
                cartas.append(box)

            print('1')

        except:
            print('Algo falló en la obtención de las tablas')


        # paso 4: concatenamos las tablas
        if cartas:
            table += cartas
            break  

        else:
            print('La lista "cartas" está vacía, se vuelve a abrir la URL.')

    driver.quit()




def precio(tipo):
    if isinstance(tipo, str):
        if '€€€€' in tipo:
            return 'Alto'
        elif '€€ - €€€' in tipo:
            return 'Medio'
        elif '€' in tipo:
            return 'Bajo'
    return ''
    




# Funcion para las ubicaciones de los restaurantes

def obtener_ubicacion_restaurante(restaurante):
    ubicacion_dict = {}

    # Realizar búsqueda en Google y obtener el primer resultado
    query = f"{restaurante} ubicación"
    url = f"https://www.google.com/search?q={query}"

    # Realizar la solicitud HTTP y analizar el contenido con Beautiful Soup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraer la ubicación si está presente
    ubicacion = soup.find('div', class_='BNeawe iBp4i AP7Wnd').get_text(strip=True) if soup.find('div', class_='BNeawe iBp4i AP7Wnd') else None

    # Almacenar en el diccionario
    ubicacion_dict[restaurante] = ubicacion

    return ubicacion_dict


