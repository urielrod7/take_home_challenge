# Prueba de automatización para Mercado Libre

Este proyecto contiene un script de automatización en Python que realiza una serie de acciones en el sitio web de Mercado Libre México, de acuerdo con los requerimientos de la prueba técnica.

## 📝 Descripción

El script realiza los siguientes pasos:
1.  Navega al sitio de Mercado Libre México.
2.  Busca el término "playstation 5".
3.  Aplica el filtro de condición "Nuevo".
4.  Aplica el filtro de Origen del envío "Local".
5.  Ordena los resultados de "mayor a menor precio".
6.  Obtiene el nombre y el precio de los primeros 5 productos listados.
7.  Imprime los resultados en la consola.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.14.0
* **Framework de Automatización:** Selenium
* **Gestor de Drivers:** webdriver-manager

## ⚙️ Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

* **Python 3:** Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
* **Google Chrome:** El script está configurado para usar Chrome.

## 🚀 Cómo Ejecutar el Proyecto

Sigue estos pasos para configurar y correr la automatización:

**1. Clona el Repositorio**
```bash
git clone <URL_DE_TU_REPOSITORIO>
cd <NOMBRE_DEL_DIRECTORIO>
```

**2. (Opcional pero recomendado) Crea un Entorno Virtual**
```bash
# Para Windows
python -m venv venv
venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instala las Dependencias**
El proyecto requiere las librerías `selenium` y `webdriver-manager`. Puedes instalarlas usando pip:
```bash
pip install selenium webdriver-manager
```

**4. Ejecuta el Script**
Una vez instaladas las dependencias, simplemente ejecuta el archivo de Python desde tu terminal:
```bash
python test_mercado_libre.py
```

El script abrirá una ventana de Google Chrome, realizará todos los pasos de forma automática y finalmente imprimirá los resultados en la misma terminal desde la que lo ejecutaste.

## 🔧 Solución de Problemas (Troubleshooting)

Este script utiliza `webdriver-manager` para gestionar el driver de Chrome automáticamente. Sin embargo, en algunos sistemas con firewalls estrictos o ciertas configuraciones de red, este método puede fallar. El síntoma más común es un error que detiene el script al inicio con un mensaje vacío (`Message:`).

Si esto ocurre, el script se puede cambiar fácilmente a un **método manual** siguiendo estos pasos:

### 1. Descargar el `chromedriver.exe` Manualmente

1.  **Verifica tu versión de Chrome** (en **Ayuda > Acerca de Google Chrome**).
2.  Descarga el driver que coincida **exactamente** con tu versión desde el [Chrome for Testing Dashboard](https://googlechromelabs.github.io/chrome-for-testing/).
3.  Coloca el archivo `chromedriver.exe` en la misma carpeta que el script.

### 2. Modificar el Script
Abre el archivo `test_mercado_libre.py` y realiza los siguientes cambios:

```python
# Comenta estas dos líneas del método automático:
# from webdriver_manager.chrome import ChromeDriverManager
# service = Service(ChromeDriverManager().install())

# Y descomenta esta línea para activar el método manual:
service = Service(executable_path="chromedriver.exe")
```

## ✅ Salida Esperada

La salida en la consola se verá similar a esto (los nombres y precios variarán):

```
No se encontró el banner de cookies.
Segundo banner de cookies aceptado.

Obteniendo la información de los primeros 5 productos...

Playstation 5 Pro Playstation 5 Pro Sony 2024 Blanco
$
35,000
--------------------
Consola Sony Playstation 5 Digital Edición 30º Aniversario 1 Tb Gris Gris
$
34,999
--------------------
... (y así hasta 5 productos) ...

Prueba finalizada.
```
