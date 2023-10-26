from personajes import *
import os

def mostrar_nombre_personaje(lista_personajes):
    for personaje in lista_personajes:
        print(f"nombre: {personaje ['nombre']} ")

    
mostrar_nombre_personaje(lista_personajes)    


def mostrar_nombre_altura(lista_personajes):
    for personaje in lista_personajes:
        print(f"nombre: {personaje ['nombre']} altura {personaje['altura']}")

mostrar_nombre_altura(lista_personajes)


def mostrar_personaje_mas_alto(lista_personajes):
    altura_maxima=None
    heroe_mas_alto=""
    for personaje in lista_personajes:
        if altura_maxima==None or float(altura_maxima) <float(personaje['altura']):
           heroe_mas_alto=personaje['nombre']
           altura_maxima=personaje['altura']
    print(f"el heroe mas alto es {heroe_mas_alto} con una altura de {altura_maxima}")

mostrar_personaje_mas_alto(lista_personajes)   


def mostrar_personaje_mas_bajo(lista_personajes):
    altura_minima=None
    heroe_mas_bajo=""
    for personaje in lista_personajes:
        if altura_minima==None or float(altura_minima) > float(personaje['altura']):
           heroe_mas_bajo=personaje['nombre']
           altura_minima=personaje['altura']
    print(f"el heroe mas bajo es {heroe_mas_bajo} con una altura de {altura_minima}")

mostrar_personaje_mas_bajo(lista_personajes)   

def calcular_altura_promedio(lista_personajes):
    acumulador_alturas=0
    for personaje in lista_personajes:
        acumulador_alturas=acumulador_alturas+float(personaje['altura'])

    promedio_alturas=acumulador_alturas//len(lista_personajes) 
    print(f"el promedio de alturas es {promedio_alturas}")  

calcular_altura_promedio(lista_personajes)       


def calcular_mas_pesado(lista_personajes):
    mas_pesado=None
    heroe_mas_pesado=""
    for personaje in lista_personajes:
        if mas_pesado==None or float(mas_pesado) <float(personaje['peso']):
           heroe_mas_pesado=personaje['nombre']
           mas_pesado=personaje['peso']
    print(f"el heroe mas pesado es {heroe_mas_pesado} con un peso de {mas_pesado}")

calcular_mas_pesado(lista_personajes)   

def calcular_mas_liviano(lista_personajes):
    menos_pesado=None
    heroe_menos_pesado=""
    for personaje in lista_personajes:
        if menos_pesado==None or float(menos_pesado) > float(personaje['peso']):
           heroe_menos_pesado=personaje['nombre']
           menos_pesado=personaje['peso']
    print(f"el heroe mas pesado es {heroe_menos_pesado} con un peso de {menos_pesado}")

calcular_mas_liviano(lista_personajes)   


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

limpiar_pantalla()

def mostrar_menu ():
    menu = (
        "\n   *** Primera parte: ***   \n"
        "1. Nombres de los superheroes\n"
        "2. Altura de los superheroes\n"
        "3. Superheroe mas alto\n"
        "4. Superheroe mas bajo\n"
        "5. Promedio de altura de los superheroes\n"
        "6. Superheroe mas pesado\n"
        "7. Superheroe menos pesado\n"
    )
    print(menu)

# fin de la primera parte 

#comienzo de la segunda parte 


def genero_masculino(lista_personajes):
    for personaje in lista_personajes:
        if personaje['genero'] == "M":
            print(f"Nombre: {personaje['nombre']}")

genero_masculino(lista_personajes)

def genero_femenino(lista_personajes):
    for personaje in lista_personajes:
        if personaje['genero'] == "F":
            print(f"Nombre: {personaje['nombre']}")
genero_femenino(lista_personajes)

def mas_alto_masculino(lista_personajes):
    altura_max_m = None
    nombre_mas_alto_m = "" 
    for personaje in lista_personajes:
        if personaje['genero'] == "M":
            altura_actual = float(personaje['altura'])
            if altura_max_m is None or altura_actual > altura_max_m:
                altura_max_m = altura_actual
                nombre_mas_alto_m = personaje['nombre']
    
    if nombre_mas_alto_m:
        print(f"El personaje masculino más alto es: {nombre_mas_alto_m}, con una altura de: {altura_max_m} cm.")
mas_alto_masculino(lista_personajes)

def mas_alto_femenino (lista_personajes):
    altura_max_f = None
    nombre_mas_alto_f = ""
        
    for personaje in lista_personajes:
        if personaje['genero'] == "F":
            altura_actual = float(personaje['altura'])
            if altura_max_f is None or altura_actual > altura_max_f:
                altura_max_f = altura_actual
                nombre_mas_alto_f = personaje['nombre']
    
    if nombre_mas_alto_f:
        print(f"El personaje femenimo más alto es: {nombre_mas_alto_f}, con una altura de: {altura_max_f} cm.")

mas_alto_femenino(lista_personajes)

def mas_bajo_masculino (lista_personajes):
    altura_min_m = None
    nombre_mas_bajo_m = ""
        
    for personaje in lista_personajes:
        if personaje['genero'] == "M":
            altura_actual = float(personaje['altura'])
            if altura_min_m is None or altura_actual < altura_min_m:
                altura_min_m = altura_actual
                nombre_mas_bajo_m = personaje['nombre']
    
    if nombre_mas_bajo_m:
        print(f"El personaje masculino más bajo es: {nombre_mas_bajo_m}, con una altura de: {altura_min_m} cm.")
mas_bajo_masculino(lista_personajes)

def mas_bajo_femenino (lista_personajes):
    altura_min_f = None
    nombre_mas_bajo_f = ""
        
    for personaje in lista_personajes:
        if personaje['genero'] == "F":
            altura_actual = float(personaje['altura'])
            if altura_min_f is None or altura_actual < altura_min_f:
                altura_min_f = altura_actual
                nombre_mas_bajo_f = personaje['nombre']
    
    if nombre_mas_bajo_f:
        print(f"El personaje femenino más bajo es: {nombre_mas_bajo_f}, con una altura de: {altura_min_f} cm.")
mas_bajo_femenino(lista_personajes)

def promedio_genero_masculino(lista_):
    acumulador_alturas_masculino=0
    for personaje in lista_personajes:
     if personaje['genero']=="M":
          acumulador_alturas_masculino=acumulador_alturas_masculino+float(personaje['altura'])

    promedio_alturas=acumulador_alturas_masculino//len(lista_personajes) 
    print(f"el promedio de alturas masaculino es {promedio_alturas}")  

promedio_genero_masculino(lista_personajes)

def promedio_genero_femenino(lista_):
    acumulador_alturas_femenino=0
    for personaje in lista_personajes:
     if personaje['genero']=="F":
          acumulador_alturas_femenino=acumulador_alturas_femenino+float(personaje['altura'])

    promedio_alturas=acumulador_alturas_femenino//len(lista_personajes) 
    print(f"el promedio de alturas femenino es {promedio_alturas}")  

promedio_genero_femenino(lista_personajes)

def contador_color_ojos(lista_personajes):
    contador_color_ojos = {}

    for personaje in lista_personajes:
        color_ojos = personaje['color_ojos']
        contador_color_ojos[color_ojos] = contador_color_ojos.get(color_ojos, 0) + 1

    print("Número de superhéroes por color de ojos:")
    for color in contador_color_ojos:
        count = contador_color_ojos[color]
        print(f"{color}: {count}")

contador_color_ojos(lista_personajes)

def contador_color_pelo(lista_personajes):
    contador_color_pelo = {}

    for personaje in lista_personajes:
        color_pelo = personaje['color_pelo']
        if color_pelo: 
            contador_color_pelo[color_pelo] = contador_color_pelo.get(color_pelo, 0) + 1

    print("\nNúmero de superhéroes por color de pelo:")
    for color in contador_color_pelo:
        count = contador_color_pelo[color]
        print(f"{color}: {count}")

contador_color_pelo(lista_personajes)

def contador_inteligencia(lista_personajes):
    contador_inteligencia = {}

    for personaje in lista_personajes:
        inteligencia = personaje.get('inteligencia', 'No Tiene')
        if inteligencia: 
            contador_inteligencia[inteligencia] = contador_inteligencia.get(inteligencia, 0) + 1

    print("\nNúmero de superhéroes por tipo de inteligencia:")
    for inteligencia, count in contador_inteligencia.items():
        print(f"{inteligencia}: {count}")

contador_inteligencia(lista_personajes)


def mostrar_segundo_menu():
    menu = (
        "\n   *** Segunda parte: ***   \n"
        "1. Nombres de los superheroes masculinos\n"
        "2. Nombres de los superheroes femeninos\n"
        "3. Mas alto del genero masculino\n"
        "4. Mas alto del genero femenino\n"
        "5. Mas bajo del genero masculino\n"
        "6. Mas bajo del genero femenino\n"
        "7. Altura promedio genero masculino\n"
        "8. Altura promedio genero femenino\n"
        "9. Cantidad de colores de ojos\n"
        "10. Cantidad de colores de pelo\n"
        "11. Tipos y cantidad de inteligencia\n"
    )
    print(menu)









        
         
         
         




        
        

        