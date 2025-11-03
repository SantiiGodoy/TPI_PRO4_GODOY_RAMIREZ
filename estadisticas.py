# ==== FUNCIONES PARA MOSTRAR ESTADÍSTICAS DE PAÍSES ====
import api
from validaciones import val_lista, val_num, val_opc_menu

# Función para obtener estadísticas de población
def estadisticas_poblacion(opc):
    paises = api.paises
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
    paises = api.paises
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
    paises = api.paises
    america = 0
    europa = 0
    asia = 0
    oceania = 0
    africa = 0
    for pais in paises:
        if pais["continente"] == "América":
            america += 1
        elif pais["continente"] == "Europa":
            europa += 1
        elif pais["continente"] == "Asia":
            asia += 1
        elif pais["continente"] == "Oceanía":
            oceania += 1
        elif pais["continente"] == "África":
            africa += 1

    resultado = (
        "\n---------------------------------------------\n"
        f'  Cantidad de países en América: {america}  \n'
        "---------------------------------------------\n"
        f'  Cantidad de países en Europa: {europa}  \n'
        "---------------------------------------------\n"
        f'  Cantidad de países en Asia: {asia}  \n'
        "---------------------------------------------\n"
        f'  Cantidad de países en Oceanía: {oceania}  \n'
        "---------------------------------------------\n"
        f'  Cantidad de países en África: {africa}  \n'
        "---------------------------------------------\n"
        f'      ¡No hay países en la antártida!       \n'
        "---------------------------------------------\n"
    )

    return resultado
    

# Función principal de estadísticas
def mostrar_estadisticas():
    paises = api.paises
    if not val_lista(paises):
        return

    while True:
        print("\n------------------------")
        print("  Mostrar estadísticas  ")
        print("------------------------")
        print("1. País con mayor población")
        print("2. País con menor población")
        print("3. Promedio de población")
        print("4. Promedio de superficie")
        print("5. Cantidad de países por continente")
        print("6. Volver")
        opc = input("Ingrese una opción(número): ")

        if val_num(opc):
            opc = int(opc)
            if val_opc_menu(opc):
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
                        print(p_por_cont())
                    elif opc == 6:
                        print("\nVolviendo...")
                        break

                # Manejo de errores
                except ValueError:
                    print("❌¡Error! Ingrese un número.")
                except Exception as e:
                    print(f'❌¡Error inesperado! {e}.')