from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import webbrowser
import time
from datetime import date
#Driver:
driver_path = './chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Navegar a la página de inicio de sesión de Twitter
driver.get('https://x.com/login')
# Especificar el hashtag que deseas rastrear
hashtag = 'nvidia'

# Esperar a que aparezca el campo de nombre de usuario
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="text"][autocomplete="username"]'))
)

# Ingresar el nombre de usuario
username_field.send_keys("v3rky_")
# Encontrar y hacer clic en el botón "Siguiente" para iniciar sesión
login_button = driver.find_element(By.XPATH, '//span[contains(text(), "Siguiente")]')
login_button.click()
time.sleep(2)

# Encontrar el campo de contraseña
password_input = driver.find_element(By.XPATH, '//input[@autocomplete="current-password"]')

# Completar el campo de contraseña con tu valor deseado
password_input.send_keys("")
time.sleep(10)
#iniciar:
# Encontrar el botón "Iniciar sesión"
password_input.send_keys(Keys.ENTER)
# Hacer clic en el botón "Iniciar sesión"
# Esperar a que se inicie sesión correctamente
WebDriverWait(driver, 3).until(
    EC.url_contains('https://x.com/home')
)

# Navegar a la página de búsqueda de Twitter para el hashtag dado
driver.get(f'https://twitter.com/hashtag/{hashtag}?lang=en')
time.sleep(3)
# Obtener la altura actual de la ventana del navegador
last_height = driver.execute_script("return document.body.scrollHeight")
# Desplazarse hacia abajo un máximo de 7 veces
scroll_count = 0
max_scroll_count = 23

tweet_texts = []  # Lista para almacenar los textos de los tweets
while scroll_count < max_scroll_count:
    # Desplazarse hacia abajo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Esperar un breve tiempo para que la página se cargue después de desplazarse
    time.sleep(2)
    
    # Encontrar los elementos <div> con el atributo data-testid="tweetText"
    div_elements = driver.find_elements("xpath", '//div[@data-testid="tweetText"]')
    
    # Recorrer los elementos y agregar los textos a la lista
    for div_element in div_elements:
        tweet_texts.append(div_element.text)
    
    # Incrementar el contador de desplazamiento
    scroll_count += 1

#Borrar twits duplicados
tweet_texts = list(set(tweet_texts))  # Eliminar duplicados
msg()
print(tweet_texts)  # Imprimir la lista sin duplicados