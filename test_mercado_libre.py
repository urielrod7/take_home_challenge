# -*- coding: utf-8 -*-

# --- 1. IMPORTACIÓN DE LIBRERÍAS ---
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def prueba_mercado_libre():
    """
    Función principal de la prueba de automatización.
    """
    # --- 2. CONFIGURACIÓN DEL WEBDRIVER ---
    # Aquí configuramos el navegador Chrome para ser controlado por el script con la clase ChromeOptions de forma automática.
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Inicia el navegador maximizado.
    service = Service(ChromeDriverManager().install())

    # Método manual.
    #service = Service(executable_path="chromedriver.exe")
    
    # Pasamos los valores a la variable driver para que realice la conexión al navegador.
    driver = webdriver.Chrome(service=service, options=options)


    # Definimos una espera explícita global de 20 segundos. 
    # Si un elemento no aparece en ese tiempo, el script fallará.
    espera = WebDriverWait(driver, 20) 

    # --- 3. EJECUCIÓN DE LA PRUEBA ---
    # Usamos un bloque try...finally para asegurarnos de que, pase lo que pase,
    # el script imprima un mensaje final.
    try:
        # --- PASO 1 y 2: NAVEGACIÓN Y BÚSQUEDA ---
        # Ingresamos directamente a Mercado Libre México.
        driver.get("https://www.mercadolibre.com.mx/")

        # Intentamos cerrar los banners de cookies que puedan aparecer.
        try:
            # Banner de la página principal
            botón_cookie = espera.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Entendido')]")))
            botón_cookie.click()
            print("Cookie de consentimiento aceptada.")
        except Exception:
            print("No se encontró el banner de cookies inicial.")

        # Ingresamos y buscamos la cadena playstation 5.
        barra_busqueda = espera.until(EC.presence_of_element_located((By.ID, "cb1-edit")))
        barra_busqueda.send_keys("playstation 5")
        barra_busqueda.send_keys(Keys.ENTER)
        
        # --- MANEJO DE COOKIES (POST-BÚSQUEDA) ---
        # A veces, un segundo banner aparece después de la búsqueda, lo cerramos también.
        try:
            botón_banner = espera.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'cookie-consent-banner')]//button")))
            botón_banner.click()
            print("Segundo banner de cookies aceptado.")
        except Exception:
            print("No se encontró el segundo banner de cookies.")

        # --- PASO 3 y 4: APLICACIÓN DE FILTROS ---
        # Usamos PARTIAL_LINK_TEXT por ser el método más simple y robusto para encontrar enlaces.
        filtro_condición = espera.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Nuevo")))
        filtro_condición.click()

        # Adaptamos el script al filtro actual "Local", ya que "Cdmx" no existe.
        filtro_ubicación = espera.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Local")))
        filtro_ubicación.click()

        # --- PASO 5: ORDENAMIENTO ---
        # Localizamos el botón que abre el menú de ordenamiento por su clase.
        ordenar_por_botón = (By.CSS_SELECTOR, "button.andes-dropdown__trigger")
        ordenar_por_acción = espera.until(EC.element_to_be_clickable(ordenar_por_botón))
        # Usamos un clic de JavaScript por ser más potente y fiable que el clic normal.
        driver.execute_script("arguments[0].click();", ordenar_por_acción)
        
        # Espera inteligente: nos aseguramos de que el menú se haya abierto
        # antes de intentar hacer clic en una de sus opciones.
        espera.until(EC.text_to_be_present_in_element_attribute(ordenar_por_botón, "aria-expanded", "true"))

        # Una vez abierto el menú, hacemos clic en el botón "Mayor precio".
        option_mayor_precio = espera.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Mayor precio')]")))
        option_mayor_precio.click()
        
        # Espera inteligente: esperamos a que el primer resultado de la lista "vieja" 
        # desaparezca, lo que nos confirma que la página se ha recargado.
        primera_lista = espera.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.poly-card")))
        espera.until(EC.staleness_of(primera_lista))
        
        # --- PASO 6: EXTRACCIÓN DE DATOS ---
        print("\nObteniendo la información de los primeros 5 productos...\n")
        # Buscamos los contenedores de los productos. Usamos la clase más reciente.
        productos = driver.find_elements(By.CSS_SELECTOR, "div.poly-card")

        # Iteramos sobre los primeros 5 productos de la lista.
        for i, producto in enumerate(productos[:5]):
            try:
                # Extraemos el nombre y el precio usando las clases que identificamos en la captura.
                nombre = producto.find_element(By.CSS_SELECTOR, "h3.poly-component__title-wrapper").text
                precio = producto.find_element(By.CSS_SELECTOR, "span.andes-money-amount").text
                
                # Imprimimos los resultados.
                print(f"{nombre}")
                print(f"{precio}")
                print("-" * 20)
            except Exception:
                print(f"No se pudo obtener la información del producto #{i+1}.")
                
    except Exception as e:
        # Si ocurre cualquier error inesperado, lo imprimimos.
        print(f"\nOcurrió un error durante la prueba: {e}")
    finally:
        # --- 4. FINALIZACIÓN ---
        print("\nPrueba finalizada.")

# --- 5. EJECUCIÓN ---
# Se ejecuta la función.
if __name__ == "__main__":
    prueba_mercado_libre()
