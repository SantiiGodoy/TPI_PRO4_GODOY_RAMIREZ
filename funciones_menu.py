# ==================================
#   FUNCIONES PRINCIPALES DEL MENÚ
# ==================================
import csv

def buscar_paises():
    pais_b = input("Ingrese el pais a buscar: ")

    try:
        print("")
    except Exception as e:
        print(f'❌¡Error inesperado! {e}')

def filtrar_paises():
    print("\n-----------------------")
    print("    Filtrar países por:  ")
    print("1. Continente")
    print("2. Rango de población")
    print("3. Rango de superficie")
    filtrado = int(input("Ingrese una opción(número): "))

    try:
        print("")
    except ValueError:
        print("❌¡Error! Debe ingresar un número.")
    except Exception as e:
        print(f'❌¡Error inesperado! {e}')

def ordenar_paises():
    print("")

def mostrar_estadisticas():
    print("")