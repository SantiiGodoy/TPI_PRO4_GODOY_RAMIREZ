import csv
from funciones_menu import * # Importamos funciones principales del menú

print("==============================")
print("  GESTIÓN DE DATOS DE PAÍSES  ")
print("==============================\n")

print("==== MENÚ ====")
print("1. Buscar país por nombre.")
print("2. Filtrar países.")
print("3. Ordenar países.")
print("4. Mostrar estadísticas")
print("5. Salir del programa")
opc = int(input("Ingrese una opción (número correspondiente): "))

# Llamamos a la función correspondiente según la opción elegida
try:
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
        exit
    else:
        print("❌¡Error! Ingrese una opción válida")

except ValueError:
    print("❌¡Error! Para elegir la opción debe ingresar el número correspondiente.")
except Exception as e:
    print(f'❌¡Error inesperado! {e}')