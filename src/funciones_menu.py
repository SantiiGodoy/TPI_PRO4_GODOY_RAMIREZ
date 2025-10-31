# ==================================
#   FUNCIONES PRINCIPALES DEL MENÚ
# ==================================
import csv
from Datos.api import paises

# ---- Función para buscar país ----
def buscar_paises():
    pais_b = input("Ingrese el país a buscar: ").capitalize()
    print("\n----------------------------")
    print(f' Información de {pais_b} ')

    try:
        encontrado = False
        for pais in paises: 
            if pais_b == pais.capitalize():
                print(f'{pais["nombre"]} | {pais["población"]} | {pais["superficie"]} | {pais["continente"]}')
                encontrado = True
        if not encontrado:
            print("❌¡País no encontrado!")

    # Manejo de errores
    except Exception as e:
        print(f'❌¡Error inesperado! {e}')


# ---- Función para filtrar países ---- ===SANTI===
def filtrar_cont():
    ord_cont = sorted(paises, key= lambda pais: pais["continente"])
    for pais in ord_cont:
        print(f'{pais["nombre"]} | {pais["población"]} | {pais["superficie"]} | {pais["continente"]}')


def rang_pobl():
    pais_menor = min(paises, key=lambda pais: pais["poblacion"])
    pais_mayor = max(paises, key=lambda pais: pais["poblacion"])

    print(" País con MENOR población:")
    print(f"- {pais_menor["nombre"]} = {pais_menor["poblacion"]:,} habitantes")

    print(" País con MAYOR población:")
    print(f"- {pais_mayor["nombre"]} = {pais_mayor["poblacion"]:,} habitantes")

def rango_sup():
    print("=== País con menor y mayor superficie ===")

    paises_con_area = [pais for pais in paises if pais.get("area") is not None]
    # Encontrar país con menor y mayor superficie
    pais_menor = min(paises_con_area, key=lambda pais: pais["area"])
    pais_mayor = max(paises_con_area, key=lambda pais: pais["area"])

    print("País con MENOR superficie:")
    print(f"- {pais_menor["nombre"]} = {pais_menor["area"]:,} km²")
    print(" País con MAYOR superficie:")
    print(f"- {pais_mayor["nombre"]} = {pais_mayor["area"]:,} km²")

def filtrar_paises():
    while True:
        print("\n-------------------------")
        print("    Filtrar países por:  ")
        print("1. Continente")
        print("2. Rango de población")
        print("3. Rango de superficie")
        print("4. Volver")
        opc = int(input("Ingrese una opción(número): "))

        try:
            if opc == 1:
                print("---- Filtrar por continentes ----")
                filtrar_cont()

            elif opc == 2:
                print("---- Filtrar por rango de población ----")
                rang_pobl()

            elif opc == 3:
                print("---- Filtrar por rango de superficie ----")
                rango_sup()
            
            elif opc == 4:
                print("Volviendo...")
                break

            else:
                print("❌¡Error! Ingrese una opción válida.")

        # Manejo de errores
        except ValueError:
            print("❌¡Error! Debe ingresar un número.")
        except Exception as e:
            print(f'❌¡Error inesperado! {e}')

# ---- Función para ordenar países ---- === FACU ===

# --- Función para ordenar los países según el campo
def mostrar_paises_ord(campo, i=0):
    if i == len(campo):
        return
    else:
        print(f'{campo[i]["nombre"]} | {campo[i]["población"]} | {campo[i]["superficie"]} | {campo[i]["continente"]}')
        ordenar_paises(campo, i+1)

def ordenar_paises(): # Función principal con menú y subfunciones
    while True:
        print("\n-------------------------")
        print("     Ordenar países por:   ")
        print("1. Nombre")
        print("2. Población")
        print("3. Superficie")
        print("4. Volver")
        opc = int(input("Ingrese una opción(número): "))

        try:
            if opc == 1:
                print("\n  Países ordenados por nombre  ")
                print("-------------------------------")
                paises_ord = sorted(paises)
                mostrar_paises_ord(paises_ord)

            elif opc == 2:
                print("\n  Países ordenados por población  ")
                print("----------------------------------")
                paises_por_p = sorted(paises, key= lambda pais: pais["poblacion"], reverse=True)
                ordenar_paises(paises_por_p)

            elif opc == 3:
                print("\n  Países ordenados por superficie  ")
                print("-----------------------------------")
                asc_des = input('Ingrese "A" (ascendente) o "D" (descendente) para filtrar: ').upper()
                try:
                    if asc_des == "A":
                        print("\n  Países por orden Ascendente  ")
                        print("-------------------------------")
                        paises_sup_asc = sorted(paises, key=lambda pais: pais["superficie"])
                        mostrar_paises_ord(paises_sup_asc)

                    elif asc_des == "D":
                        print("\n  Países por orden Descendente  ")
                        print("--------------------------------")
                        paises_sup_desc = sorted(paises, key=lambda pais: pais["superficie"], reverse=True)
                        mostrar_paises_ord(paises_sup_desc)
                    else:
                        print("❌¡Error! Ingrese una opción válida.")

                except Exception as e:
                    print(f'❌¡Error inesperado! {e}')
            elif opc == 4:
                print("Volviendo...")
                break
            else:
                print("❌¡Error! Ingrese una opción válida")
        
        # Manejo de errores
        except ValueError:
            print(f'❌¡Error! Ingrese un número.')
        except Exception as e:
            print(f'❌¡Error inesperado! {e}')


# ---- Función para mostrar estadísticas de países ---- === FACU ===
def mostrar_estadisticas():
    while True:
        print("\n------------------------")
        print("    Mostrar estadísticas  ")
        print("1. País con mayor población")
        print("2. País con menor población")
        print("3. Promedio de población")
        print("4. Promedio de superficie")
        print("5. Cantidad de países por continente")
        print("5. Volver")
        opc = int(input("Ingrese una opción(número): "))

        try:
            if opc == 1:
                print("\n  País con mayor población  ")
                print("----------------------------")
            elif opc == 2:
                print("\n  País con menor población  ")
                print("----------------------------")
            elif opc == 3:
                print("\n  Promedio de población  ")
                print("-------------------------")
            elif opc == 4:
                print("\n  Promedio de superficie  ")
                print("--------------------------")
            elif opc == 5:
                print("\n  Cantidad de países por continentes  ")
                print("--------------------------------------")
            elif opc == 6:
                print("\nVolviendo...")
                exit
            else:
                print("❌¡Error! Ingrese una opción válida.")

        # Manejo de errores
        except ValueError:
            print("❌¡Error! Ingrese un número")
        except Exception as e:
            print(f'❌¡Error inesperado! {e}')