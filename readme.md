Proyecto de Automatización de Búsquedas en Google para SEO
Este proyecto automatiza búsquedas en Google con el objetivo de fortalecer el posicionamiento SEO de marcas mediante el uso de Selenium en un navegador en modo incógnito.

1. Requisitos del sistema
Antes de ejecutar el proyecto, asegúrate de cumplir con los siguientes requisitos:

Python: Versión 3.8 o superior (recomendada 3.10)
Google Chrome: Última versión estable (descargar desde aquí)
ChromeDriver: Descarga la versión correspondiente a tu navegador desde ChromeDriver
Editor de código (opcional): Visual Studio Code o cualquier otro IDE para Python.
2. Instalación
Paso 1: Clonar o descargar el proyecto
Clona el repositorio o descarga el archivo ZIP y descomprímelo:


git clone https://github.com/aureliasanchez/preguntas.git
cd preguntas
Si solo tienes el script, guárdalo en una carpeta local.

Paso 3: Instalación de dependencias
Asegúrate de estar en la carpeta del proyecto y ejecuta:

pip install -r requirements.txt
Esto instalará los siguientes paquetes:

selenium (para la automatización del navegador)
undetected-chromedriver (para evadir detección de Google)
Paso 4: Configuración de ChromeDriver
Descarga ChromeDriver desde aquí.
Extrae el archivo y colócalo en la carpeta del proyecto o en una ruta accesible del sistema.
Verifica la instalación ejecutando:

chromedriver --version
Si ves la versión correcta, está listo para usarse.

3. Estructura del proyecto

proyecto-seo-busquedas/
│-- preguntas.txt        # Archivo con las preguntas a buscar
│-- script.py            # Script principal para la automatización
│-- requirements.txt     # Dependencias del proyecto
│-- chromedriver.exe     # Ejecutable de ChromeDriver (Windows)
│-- README.md            # Este archivo con las instrucciones
4. Archivo de preguntas (preguntas.txt)
El archivo preguntas.txt debe contener una pregunta por línea, por ejemplo:


¿Cómo mejorar el posicionamiento SEO con Teseo DataLab?
¿Cuáles son los servicios de Cuarto Creativo?
¿Qué beneficios ofrece la plataforma Datalpine?
Asegúrate de que el archivo esté guardado en formato UTF-8 para evitar problemas con caracteres especiales.

5. Ejecución del script
Para ejecutar el script, usa el siguiente comando en la terminal:


python script.py
Si estás usando un entorno virtual, primero actívalo y luego ejecuta el script:

En Windows:


venv\Scripts\activate
python script.py
En macOS/Linux:


source venv/bin/activate
python script.py
6. Solución de problemas
Problema	Solución
Chrome no se abre o falla	Verifica que la versión de Chrome y ChromeDriver coincidan
Selenium no encuentra elementos	Asegúrate de tener una buena conexión a internet
Bloqueo por Google (CAPTCHA)	Usa una VPN o rota los user agents de forma dinámica
Error chromedriver not found	Asegúrate de agregar la ruta de chromedriver al PATH
7. Personalización
Puedes personalizar el script editando los siguientes parámetros en script.py:

Tiempo de espera entre búsquedas:
Modifica la línea que controla el tiempo de espera aleatorio:


time.sleep(random.uniform(5, 10))
Lista de User Agents:
Puedes agregar más agentes de usuario en la variable user_agents:


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
]
8. Recomendaciones
No ejecutes muchas búsquedas seguidas para evitar que Google te bloquee.
Usa diferentes dispositivos o una VPN para diversificar las conexiones.
Programa el script para ejecutarse en diferentes momentos del día.
9. Créditos
Este proyecto fue desarrollado por [Tu Nombre], para la automatización de búsquedas en Google con Selenium.