# ==== FUNCIONES PARA ORDENAR PAÍSES ====
from Datos.api import paises
from src.validaciones import val_lista, val_num, val_opc_menu

# Función para ordenar los países según el campo
def mostrar_paises_ord(campo, i=0):
    if i == len(campo):
        return
    else:
        print(f'{campo[i]["nombre"]} | {campo[i]["población"]} | {campo[i]["superficie"]} | {campo[i]["continente"]}')
        ordenar_paises(campo, i+1)

# Funciones principal con menú y subfunciones
def ordenar_paises():
    if not val_lista(paises):
        return

    while True:
        print("\n-------------------------")
        print("   Ordenar países por:   ")
        print("-------------------------")
        print("1. Nombre")
        print("2. Población")
        print("3. Superficie")
        print("4. Volver")
        opc = input("Ingrese una opción(número): ")

        if val_num(opc):
            opc = int(opc)
            if val_opc_menu(opc):
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

                # Manejo de errores
                except ValueError:
                    print(f'❌¡Error! Ingrese un número.')
                except Exception as e:
                    print(f'❌¡Error inesperado! {e}.')