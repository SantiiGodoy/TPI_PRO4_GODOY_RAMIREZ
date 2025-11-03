# ==== FUNCIONES PARA FILTRAR PAÍSES ==== 
import api
from validaciones import val_lista, val_num, val_opc_menu

# Función para filtrar países por continente
def filtrar_cont():
    paises = api.paises
    if not val_lista(paises):
        return
    
    ord_cont = sorted(paises, key=lambda pais: pais["continente"])

    while True:
        print("\n  Elija un continente  ")
        print("-----------------------")
        print("1. América")
        print("2. Europa")
        print("3. Asia")
        print("4. África")
        print("5. Oceanía")
        print("6. Antártida")
        print("7. volver")
        opc_cont = input("Ingrese una opción (número): ")
        
        if val_num(opc_cont):
            opc_cont = int(opc_cont)
            if val_opc_menu(opc_cont):
                try:
                    if opc_cont == 1:
                        print("\n--------------------------")
                        print("    Países de América    ")
                        print("-------------------------")
                        for pais in ord_cont:
                            if pais["continente"] == "América":
                                print(f'{pais["nombre"]} | {pais["poblacion"]} | {pais["superficie"]} | {pais["continente"]}')
                            else:
                                pass
                    elif opc_cont == 2:
                    
                        print("\n--------------------------")
                        print("    Países de Europa     ")
                        print("-------------------------")
                        for pais in ord_cont:
                            if pais["continente"] == "Europa":
                                print(f'{pais["nombre"]} | {pais["poblacion"]} | {pais["superficie"]} | {pais["continente"]}')
                            else:
                                pass
                            
                    elif opc_cont == 3:
                        print("\n--------------------------")
                        print("     Países de Asia      ")
                        print("-------------------------")
                        for pais in ord_cont:
                            if pais["continente"] == "Asia":
                                print(f'{pais["nombre"]} | {pais["poblacion"]} | {pais["superficie"]} | {pais["continente"]}')
                            else:
                                pass
                    elif opc_cont == 4:
                        print("\n--------------------------")
                        print("    Países de África    ")
                        print("-------------------------")
                        for pais in ord_cont:
                            if pais["continente"] == "África":
                                print(f'{pais["nombre"]} | {pais["poblacion"]} | {pais["superficie"]} | {pais["continente"]}')
                            else:
                                pass
                    elif opc_cont == 5:
                        print("\n--------------------------")
                        print("    Países de Oceanía    ")
                        print("-------------------------")
                        for pais in ord_cont:
                            if pais["continente"] == "Oceanía":
                                print(f'{pais["nombre"]} | {pais["poblacion"]} | {pais["superficie"]} | {pais["continente"]}')
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
    paises = api.paises
    pais_menor = min(paises, key=lambda pais: pais["poblacion"])
    pais_mayor = max(paises, key=lambda pais: pais["poblacion"])

    print(" País con MENOR población:")
    print(f"- {pais_menor["nombre"]} = {pais_menor["poblacion"]:,} habitantes")

    print(" País con MAYOR población:")
    print(f"- {pais_mayor["nombre"]} = {pais_mayor["poblacion"]:,} habitantes")

# Función para obtener el rango de la superficie
def rango_sup():
    paises = api.paises
    print("=== País con menor y mayor superficie ===")

    paises_con_area = []
    for pais in paises:
        sup = pais.get("superficie", None)
        if sup is None:
            sup = pais.get("area", None)
        try:
            sup_val = float(sup)
        except (TypeError, ValueError):
            continue
        p = pais.copy()
        p["area_val"] = sup_val
        paises_con_area.append(p)

    if not paises_con_area:
        print("❌¡Error! No hay datos de superficie disponibles.")
        return

    # Encontrar país con mayor y menor superficie
    pais_menor = min(paises_con_area, key=lambda pais: pais["area_val"])
    pais_mayor = max(paises_con_area, key=lambda pais: pais["area_val"])

    print("País con MENOR superficie:")
    print(f"- {pais_menor['nombre']} = {int(pais_menor['area_val']):,} km²")
    print("País con MAYOR superficie:")
    print(f"- {pais_mayor['nombre']} = {int(pais_mayor['area_val']):,} km²")

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

        # Manejo de errores
        except ValueError:
            print("❌¡Error! Debe ingresar un número.")
        except Exception as e:
            print(f'❌¡Error inesperado! {e}.')