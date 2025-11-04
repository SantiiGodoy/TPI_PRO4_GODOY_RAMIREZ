# 🌎 Gestión de Datos de Países 🌎

### Integrantes

GRUPO 9:  
&nbsp;&nbsp;&nbsp;- Godoy Santino  
&nbsp;&nbsp;&nbsp;- Ramírez Facundo

### Docene Tutor

- Cinthia Rigoni

## Descripción del programa

Este proyecto se desarrolló como parte del Trabajo Práctico Integrador de la materia Programación I, de la **Tecnicatura Universitaria en Programación** de la **Facultad Tecnológica Nacional (UTN)**.

Con el objetivo de crear un programa que permita gestionar información sobre distintos países a partir de la la información traída desde la **API pública de RestCountries** (`https://restcountries.com`) que luego se almacenó en un archivo CSV para conseguir la permanencia de estos datos. De esta manera, el usuario puede buscar, filtrar y ordenar tanto datos como estádisticas sobre éstos sin la necesidad de llamar a la función y cargar los datos nuevamente cada vez que se inicia el programa. Esto se logró mediante diferentes estructuras como listas, diccionarios y funciones junto con el correcto manejo de errores y mensajes claros para que el usuario entienda los procesos o errores que devolvía el programa.

## Estructura del proyecto

📁 TPI_PRO4_GODOY_RAMIREZ/  
|--- Datos/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- api.py # Función que llama a la API para completar el CSV.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- paises.csv # Archivo CSV con la información de los países.  
|--- src/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- busquedas.py # Archivo donde se buscan países de forma exacta o parcial.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- estadisticas.py # Archivo donde se ven las estadísticas según el criterio elegido.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- filtros.py # Archivo donde se ordenan y muestran países según el criterio elegido.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- main.py # Archivo con el programa principal (menú principal).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- ordenamiento.py # Archivo donde se ordena información según el criterio elegido.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- validaciones.py # Archivo con validaciones para el correcto funcionamiento del programa.

## ¿Cómo usar el programa?

1. **Clonar el repositorio (en la carpeta donde se desea clonar)**  
   &nbsp;&nbsp;&nbsp;git clone https://github.com/SantiiGodoy/TPI_PRO4_GODOY_RAMIREZ.git  
   &nbsp;&nbsp;&nbsp;cd TPI_PRO4_GODOY_RAMIREZ
2. **Asegurarse de tener instalado Python 3.**
3. **Instalar el paquete Requests para enviar peticiones a la API:**  
   &nbsp;&nbsp;&nbsp;pip install requests # Ya que usaremos la API de "https://restcountries.com/"
4. **Ejecutar el programa:**  
   &nbsp;&nbsp;&nbsp;python src/main.py
5. **Seguir las opciones indicadas en el menú:**  
   &nbsp;&nbsp;&nbsp;1 - Buscar país por nombre.  
   &nbsp;&nbsp;&nbsp;2 - Filtrar países.  
   &nbsp;&nbsp;&nbsp;3 - Ordenar países.  
   &nbsp;&nbsp;&nbsp;4 - Mostrar estadísticas.  
   &nbsp;&nbsp;&nbsp;5 - Salir del programa  
   &nbsp;&nbsp;&nbsp;Ingrese una opción (número correspondiente):

## Ejemplo de entrada y salida

### Buscar país por nombre

#### Entrada:

Ingrese el país a buscar: Argentina

#### Salida:

`--------------------------`  
 País(es) encontrado(s)  
`--------------------------`  
Argentina | 45,808,747 | 2,780,400.0 | América

#### Entrada (búsqueda parcial):

Ingrese el país a buscar: un

#### Salida (coincidencias parciales):

`--------------------------`  
País(es) encontrado(s)  
`--------------------------`  
Reino Unido | 67,508,936 | 243,610.0 | Europa  
Hungría | 9,689,010 | 93,028.0 | Europa

### Mostrar estadísticas

#### Entrada:

Opción 3: Promedio de población

#### Salida:

El promedio de población es de 38,245,912 habitantes.

#### Entrada:

Opción 5: Cantidad de países por continente

#### Salida:

`-----------------------------------`  
Cantidad de países en América: 56  
`-----------------------------------`  
Cantidad de países en Europa: 44  
`-----------------------------------`  
Cantidad de paises en Asia: 50  
`-----------------------------------`  
Cantidad de países en Oceanía: 14  
`-----------------------------------`  
Cantidad de países en África: 54  
`-----------------------------------`  
¡No hay países en la antártida!  
`-----------------------------------`

## Participación de los integrantes

El proyecto fue desarrollado de manera colaborativa en todas las etapas.

Trabajamos juntos en la implementación del archivo api.py y así, conseguir la conexión con la API de RestCountries, la descarga de datos y la creación del archivo paises.csv. Asimismo, hicimos la estructura principal del programa main.py, armando la estructura del menú y la lógica de ejecución del programa.

Para el desarrollo de las funciones y subfunciones del menú, nos dividimos las tareas en partes iguales, de manera que cada integrante se encargó de crear y probar un conjunto de funciones (búsqueda, filtrado, ordenamiento, estadísticas), asegurando que todo el código mantuviera coherencia y consistencia. Esta división del trabajo se hizo sin dejar de lado la comunicación entre los dos ya que estuvimos haciéndo consultas y ayudando al otro en su código si había un problema constantemente.

Para conseguir esta comunicación entre nosotros, optamos por usar un repositorios con 3 ramas: la rama principal(main) y dos ramas más(rama_santino y rama_ramirez) para que cada uno pueda trabajar en el código tranquilamente sin tener un problema en la rama principal. Luego de que cada uno "pusheara" sus cambios a su rama correspondiente en el repositorio remoto, se hacían los "merges" correspondientes para fusionar las ramas y que todo el código finalmente quede en la rama principal.

Link del video explicativo: `https://drive.google.com/file/d/1EnoxqcbZwKQwL_q816uenf_2ugBUJXPw/view?usp=sharing`
