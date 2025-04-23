import menu
import juego1vs1
import reglas

menu.mostrarMenu()

opcion = input("Elige una opción: ")

if opcion == "1":
    juego1vs1.modo1vs1()
#elif opcion == "2":
  #opcion de modo por tiempo  
#elif opcion == "3":
    #opcion de ver el rankin
elif opcion == "4":
    reglas.mostrar_reglas()
elif opcion == "5":
    print("Saliendo del programa...")
else:
    print("Opción inválida. Por favor, elige una opción válida.")



