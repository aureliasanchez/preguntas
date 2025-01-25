import time
import random
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

# Configuración del navegador
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Modo incógnito
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    #chrome_options.add_argument("--headless")  # Si no quieres ver el navegador
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-extensions")

    # Lista de User Agents simulando distintos dispositivos
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
    ] 

    # Aplicando un user-agent aleatorio correctamente
    chrome_options.add_argument(f'--user-agent="{random.choice(user_agents)}"')

    driver = uc.Chrome(options=chrome_options)
    return driver

# Leer preguntas desde un archivo CSV o TXT
def read_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        questions = [line.strip() for line in f.readlines()]
    return questions

# Realizar la búsqueda
def search_google(driver, query):
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(random.uniform(5, 10))  # Simulación de tiempo de lectura

# Automatizar múltiples búsquedas
def automate_search(file_path):
    driver = setup_driver()
    queries = read_questions(file_path)

    for query in queries:
        print(f"Buscando: {query}")
        search_google(driver, query)

        # Borrar cookies para evitar seguimiento
        driver.delete_all_cookies()
        
        # Espera entre búsquedas para parecer humano
        time.sleep(random.uniform(10, 20))

    driver.quit()
    print("Búsquedas completadas.")

# Ruta del archivo con preguntas
file_path = "preguntas.txt"
automate_search(file_path)
