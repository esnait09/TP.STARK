from funciones import *
from personajes import*
import os


menu = input("Elija un menu (1 o 2): ")
if menu == "1":
    while True:
        mostrar_menu()
        opcion = input("Elija una opción (1-7, o 8 para salir): ")

        if opcion == '1':
            limpiar_pantalla()
            mostrar_nombre_personaje(lista_personajes)
        elif opcion == '2':
            limpiar_pantalla()
            mostrar_nombre_altura(lista_personajes)
        elif opcion == '3':
            limpiar_pantalla()
            mostrar_personaje_mas_alto(lista_personajes)
        elif opcion == '4':
            limpiar_pantalla()
            mostrar_personaje_mas_bajo(lista_personajes)
        elif opcion == '5':
            limpiar_pantalla()
            calcular_altura_promedio(lista_personajes)
        elif opcion == '6':
            limpiar_pantalla()
            calcular_mas_pesado(lista_personajes)
        elif opcion == '7':
            limpiar_pantalla()
            calcular_mas_liviano(lista_personajes)
        elif opcion == '8':
            limpiar_pantalla()
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Elija una opción del 1 al 8.")
            input("Presione Enter para continuar...")

else:
    while True:
        mostrar_segundo_menu()
        opcion = input("Elija una opción (1-11, o 12 para salir): ")

        if opcion == '1':
            limpiar_pantalla()
            genero_masculino(lista_personajes)
        elif opcion == '2':
            limpiar_pantalla()
            genero_femenino(lista_personajes)
        elif opcion == '3':
            limpiar_pantalla()
            mas_alto_masculino(lista_personajes)
        elif opcion == '4':
            limpiar_pantalla()
            mas_alto_femenino(lista_personajes)
        elif opcion == '5':
            limpiar_pantalla()
            mas_bajo_masculino(lista_personajes)
        elif opcion == '6':
            limpiar_pantalla()
            mas_bajo_femenino(lista_personajes)
        elif opcion == '7':
            limpiar_pantalla()
            promedio_genero_masculino(lista_personajes)
        elif opcion == '8':
            limpiar_pantalla()
            promedio_genero_femenino (lista_personajes)
        elif opcion == '9':
            limpiar_pantalla()
            contador_color_ojos(lista_personajes)
        elif opcion == '10':
            limpiar_pantalla()
            contador_color_pelo(lista_personajes)
        elif opcion == '11':
            limpiar_pantalla()
            contador_inteligencia(lista_personajes)
        elif opcion == '12':
            limpiar_pantalla()
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Elija una opción del 1 al 8.")
            input("Presione Enter para continuar...")





