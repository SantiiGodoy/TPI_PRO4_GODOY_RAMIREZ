# ==================================
#     FUNCIONES Y SUB-FUNCIONES
# ==================================
from Datos.api import paises

# ==== FUNCIÓN PARA BUSCAR PAÍS POR NOMBRE ====
def buscar_paises():
    pais_b = input("Ingrese el país a buscar: ").strip().capitalize()

    try:
        encontrado = False

        for pais in paises:
            nombre_pais = pais["nombre"]
            #====Buscar de manera excata====
            if pais_b == pais.capitalize():
                print("\n----------------------------")
                print(f' Información de {pais_b} ')
                print("---------------------------")
                print(f'{pais["nombre"]} | {pais["población"]} | {pais["superficie"]} | {pais["continente"]}')
                encontrado = True

            elif pais_b in nombre_pais.capitalize():
                print("\n----------------------------")
                print(f' Coincidencia parcial: {nombre_pais} ')
                print("----------------------------")
                print(f'{nombre_pais} | {pais["población"]} | {pais["superficie"]} | {pais["continente"]}')
                encontrado = True

        if not encontrado:
            print("❌¡País no encontrado!")

    # Manejo de errores
    except Exception as e:
        print(f'❌¡Error inesperado! {e}.')


# ==== FUNCIONES PARA FILTRAR PAÍSES ==== 
# Función para filtrar países por continente
def filtrar_cont():
    ord_cont = sorted(paises, key=lambda pais: pais["continente"])
    while True:
        print("  Elija un continente  ")
        print("-----------------------")
        print("1. América")
        print("2. Europa")
        print("3. Asia")
        print("4. África")
        print("5. Oceanía")
        print("6. Antártida")
        print("7. volver")
        opc_cont = int(input("Ingrese una opción (número): "))

        try:
            if opc_cont == 1:
                print("\n--------------------------")
                print("    Países de América    ")
                print("-------------------------")
                for pais in ord_cont:
                    if pais["continente"] == "america":
                        print(f'{pais["nombre"]} | {pais["población"]} | {pais["superficie"]} | {pais["continente"]}')
                    else:
                        pass
            elif opc_cont == 2:

                print("\n--------------------------")
                print("    Países de Europa     ")
                print("-------------------------")
                for pais in ord_cont:
                    if pais["continente"] == "europa":
                        print(f'{pais["nombre"]} | {pais["población"]} | {pais["superficie"]} | {pais["continente"]}')
                    else:
                        pass

            elif opc_cont == 3:
                print("\n--------------------------")
                print("     Países de Asia      ")
                print("-------------------------")
                for pais in ord_cont:
                    if pais["continente"] == "asia":
                        print(f'{pais["nombre"]} | {pais["población"]} | {pais["superficie"]} | {pais["continente"]}')
                    else:
                        pass
            elif opc_cont == 4:
                print("\n--------------------------")
                print("    Países de África    ")
                print("-------------------------")
                for pais in ord_cont:
                    if pais["continente"] == "africa":
                        print(f'{pais["nombre"]} | {pais["población"]} | {pais["superficie"]} | {pais["continente"]}')
                    else:
                        pass
            elif opc_cont == 5:
                print("\n--------------------------")
                print("    Países de Oceanía    ")
                print("-------------------------")
                for pais in ord_cont:
                    if pais["continente"] == "oceania":
                        print(f'{pais["nombre"]} | {pais["población"]} | {pais["superficie"]} | {pais["continente"]}')
                    else:
                        pass
            elif opc_cont == 6:
                print("\n------------------------------------")
                print("  ¡No hay países en la Antártida!  ")
                print("-----------------------------------")

            elif opc_cont == 7:
                print("Volviendo al menú anterior...")
                break
            else:
                print("❌¡Error! Ingrese una opción válida")
                
        # Manejo de errores
        except ValueError:
            print("❌¡Error! Por favor ingrese un número.")
        except Exception as e:
            print(f'❌¡Error inesperado! {e}.')

# Función para obtener el rango de la población
def rang_pobl():
    pais_menor = min(paises, key=lambda pais: pais["poblacion"])
    pais_mayor = max(paises, key=lambda pais: pais["poblacion"])

    print(" País con MENOR población:")
    print(f"- {pais_menor["nombre"]} = {pais_menor["poblacion"]:,} habitantes")

    print(" País con MAYOR población:")
    print(f"- {pais_mayor["nombre"]} = {pais_mayor["poblacion"]:,} habitantes")

# Función para obtener el rango de la superficie
def rango_sup():
    print("=== País con menor y mayor superficie ===")

    paises_con_area = [pais for pais in paises if pais.get("area") is not None]

    # Encontrar país con mayor y menor superficie
    pais_menor = min(paises_con_area, key=lambda pais: pais["area"])
    pais_mayor = max(paises_con_area, key=lambda pais: pais["area"])

    print("País con MENOR superficie:")
    print(f"- {pais_menor["nombre"]} = {pais_menor["area"]:,} km²")
    print(" País con MAYOR superficie:")
    print(f"- {pais_mayor["nombre"]} = {pais_mayor["area"]:,} km²")

# Función principal para filtrar países
def filtrar_paises():
    while True:
        print("\n-------------------------")
        print("  Filtrar países por:  ")
        print("-----------------------")
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
            print(f'❌¡Error inesperado! {e}.')


# ==== FUNCIONES PARA ORDENAR PAÍSES ====
# Función para ordenar los países según el campo
def mostrar_paises_ord(campo, i=0):
    if i == len(campo):
        return
    else:
        print(f'{campo[i]["nombre"]} | {campo[i]["población"]} | {campo[i]["superficie"]} | {campo[i]["continente"]}')
        ordenar_paises(campo, i+1)

# Funciones principal con menú y subfunciones
def ordenar_paises():
    while True:
        print("\n-------------------------")
        print("   Ordenar países por:   ")
        print("-------------------------")
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
                paises_por_p = sorted(paises, key=lambda pais: pais["poblacion"], reverse=True)
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
                    print(f'❌¡Error inesperado! {e}.')
            elif opc == 4:
                print("Volviendo...")
                break
            else:
                print("❌¡Error! Ingrese una opción válida.")
        
        # Manejo de errores
        except ValueError:
            print(f'❌¡Error! Ingrese un número.')
        except Exception as e:
            print(f'❌¡Error inesperado! {e}.')


# ==== FUNCIONES PARA MOSTRAR ESTADÍSTICAS DE PAÍSES ====

# Función para obtener estadísticas de población
def estadisticas_poblacion(opc):
    if opc == "mayor":
        p_mayor = 0
        for pais in paises:
            if pais["población"] > p_mayor:
                mayor_pob = pais
            else:
                pass
        return print(f'El país con mayor población es {mayor_pob["nombre"]} con {mayor_pob["poblacion"]} habitantes.')
    elif opc == "menor":
        p_menor = 0
        for pais in paises:
            if pais["poblacion"] < p_menor:
                menor_pob = pais
            else:
                pass
        return print(f'El país con menor población es {menor_pob["nombre"]} con {menor_pob["poblacion"]} habitantes.')
    
# Función para obtener promedios
def obtener_promedio(opc):
    if opc == "promedio":
        sum_p = 0
        for pais in paises:
            sum_p += pais["poblacion"]
        promedio_p = float(sum_p / len(paises))
        return print(f'El promedio de población es de {promedio_p} habitantes.')
    elif opc == "superficie":
        sum_sup = 0
        for pais in paises:
            sum_sup += pais["superficie"]
        promedio_s = float(sum_sup / len(paises))
        return print(f'El promedio de la superficie es de {promedio_s:.2f} km².')

# Función para obtener cantidad de países por continente
def p_por_cont():
    america = 0
    europa = 0
    asia = 0
    oceania = 0
    africa = 0
    for pais in paises:
        if pais["continente"] == "america":
            america += 1
        elif pais["continente"] == "europa":
            europa += 1
        elif pais["continente"] == "asia":
            asia += 1
        elif pais["continente"] == "oceania":
            oceania += 1
        elif pais["continente"] == "africa":
            africa += 1

    resultado = (
        "\n---------------------------------------------"
        f'  Cantidad de países en América: {america}  '
        "---------------------------------------------"
        f'  Cantidad de países en Europa: {europa}  '
        "---------------------------------------------"
        f'  Cantidad de países en Asia: {asia}  '
        "---------------------------------------------"
        f'  Cantidad de países en Oceanía: {oceania}  '
        "---------------------------------------------"
        f'  Cantidad de países en África: {africa}  '
        "---------------------------------------------"
        f'      ¡No hay países en la antártida!       '
        "---------------------------------------------"
    )

    return resultado
    

# Función principal de estadísticas
def mostrar_estadisticas():
    while True:
        print("\n------------------------")
        print("  Mostrar estadísticas  ")
        print("------------------------")
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
                opc_eleg = "mayor"
                estadisticas_poblacion(opc_eleg)
            elif opc == 2:
                print("\n  País con menor población  ")
                print("----------------------------")
                opc_eleg = "menor"
                estadisticas_poblacion(opc_eleg)
            elif opc == 3:
                print("\n  Promedio de población  ")
                print("-------------------------")
                opc_eleg = "población"
                obtener_promedio(opc_eleg)
            elif opc == 4:
                print("\n  Promedio de superficie  ")
                print("--------------------------")
                opc_eleg = "superficie"
                obtener_promedio(opc_eleg)
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
            print("❌¡Error! Ingrese un número.")
        except Exception as e:
            print(f'❌¡Error inesperado! {e}.')