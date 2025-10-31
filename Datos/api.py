# =====================
# = LLAMADAS A LA API = 
# =====================

import requests #---Importamos e instalamos requests---/Comando pip install requests\
import csv # Importamos librería CSV
import os # Importamos librería OS

# --- Configuración de la API ---
URL_API = "https://restcountries.com/v3.1/all?fields=name,population,area,region,translations"

if os.path.exists("paises.csv") or os.path.getsize("paises.csv") != 0:
    print("✅¡Los datos ya están cargados!")
else:
    def datos_api():
        print(" Carga inicial de datos de TODOS los países...")

        lista_paises = []

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