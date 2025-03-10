from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ruta del driver
driver_path = './chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Navegar a la página de IMDb con el top 250 de películas
    driver.get("https://www.imdb.com/chart/top/")

    # Esperar a que los títulos estén presentes
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ipc-title-link-wrapper"))
    )

    # Obtener todos los elementos con la clase especificada
    movie_elements = driver.find_elements(By.CLASS_NAME, "ipc-title-link-wrapper")

    # Imprimir el texto de cada película
    for movie in movie_elements:
        title = movie.find_element(By.CLASS_NAME, "ipc-title__text").text
        print(title)

finally:
    # Cerrar el navegador
    driver.quit()
