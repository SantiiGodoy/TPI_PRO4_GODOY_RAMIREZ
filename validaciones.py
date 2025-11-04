# ======================
# ==== VALIDACIONES ====
# ======================
import os

# ---- Validaciones del csv ----
def val_csv(archivo):
    if not os.path.exists(archivo):
        print(f'❌¡El archivo "paises.csv" no existe!')
        print("Creando nuevo archivo...")
        return False
    
    elif os.path.getsize(archivo) == 0:
        print(f'❌¡El archivo "paises.csv" se encuentra vacío!')
        print(f'Cargando información a "paises.csv".')
        return False
    else:
        return True

# ---- Validación opc del menú principal ----
def val_opc_menu(opc):
    opc_disp = [1,2,3,4,5,6,7]
    if opc not in opc_disp:
        print("❌¡Error! Ingrese una opción válida.")
        return False
    else:
        return True

# ---- Validación nombre del país ----
def val_nom(nombre):
    if nombre.strip() == "":
        print("❌¡Error! El nombre no puede estar vacío.")
        return False
    else:
        return True

# ---- Validación lista de países ----
def val_lista(paises):
    if len(paises) == 0:
        print("❌¡Error! No hay datos cargados.")
        return False
    else:
        return True

# ---- Validación de entradas numéricas ----
def val_num(numero):
    try:
        int(numero)
        return True
    except ValueError:
        print("❌¡Error! Debe ingresar un número.")