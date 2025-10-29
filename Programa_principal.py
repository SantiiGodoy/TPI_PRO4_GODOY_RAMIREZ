print("==============================")
print("  GESTIÓN DE DATOS DE PAÍSES  ")
print("==============================\n")

print("==== MENÚ ====")
print("1. Buscar país por nombre.")
print("2. Filtrar países.")
print("3. Ordenar países.")
print("4. Mostrar estadísticas")
opc = int(input("Ingrese una opción (número correspondiente): "))

try:
    print("")
except ValueError:
    print("❌ ¡Error! ")
