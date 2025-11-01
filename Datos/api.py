# =====================
# = LLAMADAS A LA API = 
# =====================

import requests #---Importamos e instalamos requests---/Comando pip install requests\
import csv # Importamos librería CSV
import os # Importamos librería OS

# --- Configuración de la API ---
URL_API = "https://restcountries.com/v3.1/all?fields=name,population,area,region,translations"

def datos_api():
    lista_paises = []
    if os.path.exists("paises.csv") and os.path.getsize("paises.csv") != 0 and len(lista_paises) != 0: # Si el csv y la lista ya están cargados
        print("✅¡Los datos ya están cargados!")

    elif os.path.exists("paises.csv") and len(lista_paises) == 0: # Si el csv está cargado pero la lista no
        try:
            with open("paises.csv", "r", encoding="utf-8") as paises:
                datos = csv.DictReader(paises)
            for fila in datos:
                nombre = fila.get("translations", {}).get("spa", {}).get("common", fila.get("name", {}).get("common", "Desconocido"))
                poblacion = fila.get("population", "Desconocida")
                superficie = fila.get("area", "Desconocida")
                continente = fila.get("region", "Desconocido")

                lista_paises.append({
                    "nombre":nombre,
                    "poblacion":int(poblacion),
                    "superficie":float(superficie),
                    "continente":continente
                })

            print("✅ Países cargados correctamente.")
            return lista_paises
        
        except Exception as e:
            print(f'❌¡Error inesperado! {e}.')

    else: # Si no está cargado el csv ni la lista
        print(" Carga inicial de datos de TODOS los países...")
        try:
            respuesta = requests.get(URL_API)
            respuesta.raise_for_status() #Lanza ERROR si el estado no es 200.
            datos = respuesta.json()
            print(f"✅ Se cargaron correctamente países.")
            with open("paises.csv", "w", encoding="utf-8") as paises_csv:
                campos = ["nombre", "poblacion","superficie","continente"]
                writer = csv.DictWriter(paises_csv,fieldnames=campos)
                writer.writeheader()
                for pais in datos:
                    # Llamamos campos de la API.
                    nombre = pais.get("translations", {}).get("spa", {}).get("common", pais.get("name", {}).get("common", "Desconocido"))
                    poblacion = pais.get("population", "Desconocida")
                    superficie = pais.get("area", "Desconocida")
                    continente = pais.get("region", "Desconocido")
                    writer.writerow({ #Agregamos datos al CSV.
                        "nombre": nombre,
                        "poblacion": int(poblacion),
                        "superficie": float(superficie),
                        "continente": continente
                        })
                    lista_paises.append({ #Agregamos diccionario con datos a la lista.
                        "nombre":nombre,
                        "poblacion":int(poblacion),
                        "superficie":float(superficie),
                        "continente":continente
                    })
                print("✅ Países cargados correctamente.")
                return lista_paises
        except requests.exceptions.RequestException as e:
            print(f"❌ Error de red o conexión: {e}") # Error de solicitud.
        except ValueError:
            print("❌ ¡Error! La respuesta no tiene formato JSON válido.") #Error json.