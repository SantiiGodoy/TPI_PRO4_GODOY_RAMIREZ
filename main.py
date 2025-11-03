# Importaciones al menú principal
import api
from busquedas import buscar_paises 
from filtros import filtrar_paises
from ordenamiento import ordenar_paises
from estadisticas import mostrar_estadisticas
from validaciones import val_opc_menu, val_num

# Llamamos a la función para cargar el csv y la lista con la API
api.datos_api()

while True:
    print("\n==============================")
    print("  GESTIÓN DE DATOS DE PAÍSES  ")
    print("==============================\n")

    print("==== MENÚ ====")
    print("1. Buscar país por nombre.")
    print("2. Filtrar países.")
    print("3. Ordenar países.")
    print("4. Mostrar estadísticas")
    print("5. Salir del programa")
    opc = input("Ingrese una opción (número correspondiente): ")



    if val_num(opc):
        opc = int(opc)
        if val_opc_menu(opc):
            try: # Llamamos a la función correspondiente según la opción elegida
                if opc == 1:
                    buscar_paises()
                elif opc == 2:
                    filtrar_paises()
                elif opc == 3:
                    ordenar_paises()
                elif opc == 4:
                    mostrar_estadisticas()
                elif opc == 5:
                    print("Saliendo del programa...")
                    break

            # Manejo de errores
            except ValueError:
                print("❌¡Error! Para elegir la opción debe ingresar el número correspondiente.")
            except Exception as e:
                print(f'❌¡Error inesperado! {e}')