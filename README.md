# 🌎 Gestión de Datos de Países 🌎

### Integrantes

- Godoy Santino
- Facundo Ramírez

### Docene Tutor

- Cinthia Rigoni

#

Este proyecto se desarrolló como parte del Trabajo Práctico Integrador de la materia Programación I, de la **Tecnicatura Universitaria en Programación** de la **Facultad Tecnológica Nacional (UTN)**.

Con el objetivo de crear un programa que permita gestionar información sobre distintos países a partir de un archivo CSV. De esta manera, el usuario. puede buscar, filtrar y ordenar tanto datos como estádisticas sobre éstos. Lo cual se logró mediante diferentes estructuras como listas, diccionarios y funciones.

## objetivos

- Afianzar el uso de estructura de datos como **listas y diccionarios**.
- **Modularizar el código** mediante funciones obteniendo un código más claro y prolijo.
- Implementar **filtrado, ordenamiento y análisis estádistico** de la información.
- Realizar la lectura y gestión de datos mediante **archivos CSV**.
- Lograr el desarrollo de un programa **legible, documentado correctamente y funcional**.

## Conceptos claves

El proyecto se desarrolló en los siguientes conceptos:

- **Listas:** para almacenar múltiples registros de países.
- **diccionarios:** para guardar y ordenar la información de cada país.
- **Funciones:** con el fin de modularizar tareas específicas.
- **Condicionales:** para validar entradas y controlar el flujo del programa.
- **Estructuras repetitivas:** para recorrer y procesar los datos.
- **Ordenamiento:** por nombre, población o superficie.
- **Estadísticas:** cálculo de promedios, conteos por continente, máximos y mínimos.
- **Archivos CSV:** lectura estructurada de datos externos.

## Requisitos Técnicos

- **Lenguaje:** Python 3.x
- **Librerías estándar utilizadas:**
  - `csv` Para la lectura de archivos
  - `os` Para verificar la existencia del archivo
- **Ejecución:** programa mostrado en consola

## Estructura del proyecto

📁 TPI_PRO4_GODOY_RAMIREZ/  
|--- Datos/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- api.py # Función que llama a la API para completar el CSV.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- paises.csv # Archivo CSV con la información de los países.  
|--- src/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- main.py # Archivo con el programa principal (menú principal).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- funciones_menu.py # Archivo con las funciones y subfunciones del menú.

## ¿Cómo usar el programa?

1. **Clonar el repositorio (en la carpeta donde se desea clonar)**  
   &nbsp;&nbsp;&nbsp;git clone https://github.com/SantiiGodoy/TPI_PRO4_GODOY_RAMIREZ.git  
   &nbsp;&nbsp;&nbsp;cd TPI_PRO4_GODOY_RAMIREZ
2. **Asegurarse de tener instalado Python 3.**
3. **Instalar el paquete Requests para enviar peticiones a la API:**  
   &nbsp;&nbsp;&nbsp;pip install requests # Ya que usaremos la API de "https://restcountries.com/"
4. **Ejecutar el programa:**  
   &nbsp;&nbsp;&nbsp;python main.py
5. **Seguir las opciones indicadas en el menú:**  
   &nbsp;&nbsp;&nbsp;1 - Buscar país por nombre.  
   &nbsp;&nbsp;&nbsp;2 - Filtrar países.  
   &nbsp;&nbsp;&nbsp;3 - Ordenar países.  
   &nbsp;&nbsp;&nbsp;4 - Mostrar estadísticas.  
   &nbsp;&nbsp;&nbsp;5 - Salir del programa  
   &nbsp;&nbsp;&nbsp;Ingrese una opción (número correspondiente):
