# =====================
#   LLAMADAS A LA API
# =====================

import requests
import json

# --- Configuración de la API ---
URL_API_ALL = "https://restcountries.com/v3.1/all"

print(" Carga inicial de datos de TODOS los países...")

# 1. Realizar la solicitud GET inicial para obtener todos los países
try:
    respuesta = requests.get(URL_API_ALL)
    
    if respuesta.status_code == 200:
        datos_completos = respuesta.json()
        print(f"✅ Se cargaron países. ¡Listo para buscar!")
        
    else:
        print(f"❌ Error al conectar con la API. Código: {respuesta.status_code}")
        exit()
        
except requests.exceptions.RequestException as e:
    print(f"❌ Error de red o conexión: {e}")
    exit() # Error de conexión