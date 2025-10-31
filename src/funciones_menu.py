# ==================================
#   FUNCIONES PRINCIPALES DEL MENÚ
# ==================================
import csv

# ---- Función para buscar país ----
def buscar_paises():
    pais_b = input("Ingrese el país a buscar: ")
    print("\n----------------------------")
    print(f' Información de {pais_b} ')

    try:
        print("")

    # Manejo de errores
    except Exception as e:
        print(f'❌¡Error inesperado! {e}')


# ---- Función para filtrar países ----
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

            elif opc == 2:
                print("---- Filtrar por rango de población ----")

            elif opc == 3:
                print("---- Filtrar por rango de superficie ----")
            
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

# ---- Función para ordenar países ----
def ordenar_paises():
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

            elif opc == 2:
                print("\n  Países ordenados por población  ")
                print("----------------------------------")

            elif opc == 3:
                print("\n  Países ordenados por superficie  ")
                print("-----------------------------------")
                asc_des = input('Ingrese "A" (ascendente) o "D" (descendente) para filtrar: ').upper()
                try:
                    if asc_des == "A":
                        print("")

                    elif asc_des == "D":
                        print("")
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


# ---- Función para mostrar estadísticas de países ----
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