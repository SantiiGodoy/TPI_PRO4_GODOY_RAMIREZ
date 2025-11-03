# =====================
# = LLAMADAS A LA API = 
# =====================

# Importaciones necesarias
import requests #---Importamos e instalamos requests---/Comando pip install requests\
import csv # Importamos librería CSV
from validaciones import val_csv, val_lista

paises = []

# --- Configuración de la API ---
URL_API = "https://restcountries.com/v3.1/all?fields=name,population,area,region,translations"
REGION_ES = {"Americas":"América","Europe":"Europa","Asia":"Asia","Africa":"África","Oceania":"Oceanía","Antarctic":"Antártida"}
def datos_api():
    global paises
    archivo = "paises.csv"
    if val_csv(archivo):
        try:
            with open("paises.csv", "r",newline="" ,encoding="utf-8") as archivo:
                datos = csv.DictReader(archivo)
                for fila in datos:
                    nombre = fila["nombre"]
                    poblacion = fila["poblacion"]
                    superficie = fila["superficie"]
                    continente = fila["continente"]

                    paises.append({
                        "nombre":nombre,
                        "poblacion":int(poblacion),
                        "superficie":float(superficie),
                        "continente":continente
                    })

            if val_lista(paises):
                print("✅ Países cargados correctamente.")
                return paises
            else:
                print("❌¡Error! el archivo no contiene datos válidos.")

        except Exception as e:
            print(f'❌¡Error inesperado! {e}.')
            return []

    else: # Si no está cargado el csv ni la lista
        print(" Carga inicial de datos de TODOS los países...")
        try:
            respuesta = requests.get(URL_API)
            respuesta.raise_for_status() #Lanza ERROR si el estado no es 200.
            datos = respuesta.json()
            print(f"✅ Se cargaron correctamente países.")
            with open("paises.csv", "w",newline="", encoding="utf-8") as paises_csv:
                campos = ["nombre", "poblacion","superficie","continente"]
                writer = csv.DictWriter(paises_csv,fieldnames=campos)
                writer.writeheader()
                paises.clear()
                for pais in datos:
                    # Llamamos campos de la API.
                    nombre = pais.get("translations", {}).get("spa", {}).get("common", pais.get("name", {}).get("common", "Desconocido"))
                    poblacion = pais.get("population", "Desconocida")
                    superficie = pais.get("area", "Desconocida")
                    region = pais.get("region", "Desconocido")
                    continente = REGION_ES.get(region, "Desconocido")

                    pais = {
                        "nombre": nombre,
                        "poblacion": poblacion,
                        "superficie": superficie,
                        "continente": continente
                    }
                    writer.writerow(pais)
                    paises.append(pais)
                
            if val_lista(paises):
                print("✅ Países cargados correctamente.")
            else:
                print("❌¡Error! No se pudo cargar la información de los países.")
            return paises
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error de red o conexión: {e}") # Error de solicitud.
        except ValueError:
            print("❌ ¡Error! La respuesta no tiene formato JSON válido.") #Error json.