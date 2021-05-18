# Librerías
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# Opciones de navegación
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver_path = 'D:\\PROYECTOS PYTHON\\WEB DRIVER\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, options=options)

# Inicializar el navegador

driver.get('https://servicioscf.afip.gob.ar/Facturacion/facturasApocrifas/default.aspx')

# Lista de cuits a buscar / proceso completo

numeros = [27209139516, 30637767336, 33692148229, 30709447846]

for item in numeros:
    textbox = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div/div/div/form/div[3]/div[1]/input')
    textbox.send_keys(item)
    consultar = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div/div/div/form/div[3]/div[2]/input[1]')
    consultar.click()
    time.sleep(2)
    WebDriverWait(driver, 5) \
        .until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[7]/div/div/div/form/div[5]'))) \
    filename = str(item)+'.png'
    driver.save_screenshot(filename) \
    element = driver.find_element_by_xpath('//*[@id="btnLimpiar"]') \
    element.click()

driver.close()
