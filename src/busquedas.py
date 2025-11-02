# ==== FUNCIÓN PARA BUSCAR PAÍS POR NOMBRE ====
from Datos.api import paises
from src.validaciones import val_nom, val_lista

def buscar_paises():
    if not val_lista(paises):
        return
    
    pais_b = input("Ingrese el país a buscar: ").strip()
    if not val_nom(pais_b):
        return

    try:
        p_encontrados = []

        # Búsqueda exacta 
        for pais in paises:
            if pais_b.lower() == pais["nombre"].lower():
                p_encontrados.append(pais)

        # Búsqueda parcial
        if not p_encontrados:
            for pais in paises:
                if pais_b.lower() in pais["nombre"].lower():
                    p_encontrados.append(pais)
        
        if p_encontrados:
            print("\n--------------------------")
            print("  País(es) encontrado(s)  ")
            print("--------------------------")
            for pais in p_encontrados:
                print(f'{pais["nombre"]} | {pais["población"]} | {pais["superficie"]} | {pais["continente"]}')
        else:
            print("❌¡Error! País no encontrado.")

    # Manejo de errores
    except Exception as e:
        print(f'❌¡Error inesperado! {e}.')