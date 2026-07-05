from funciones_aux import *
from colorama import init, Fore, Back, Style


init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + "Bienvenido al Sistema de Gestión de Productos.")

while True:
    opcion = input(Fore.LIGHTBLUE_EX + "Por favor, elige una opción numérica del menú para continuar:\n1. Agregar producto\n2. Mostrar productos\n3. Buscar producto\n4. Eliminar producto\n5. Modificar producto\n6. Consultar productos por nivel de stock\n7. Salir\n" + Fore.LIGHTRED_EX + "Ingresa el número de la opción que deseas ejecutar: ")
    if not opcion.isdigit():
        print(Fore.RED + "Por favor, ingresa un valor numérico válido." + Style.RESET_ALL)
        continue
    opcion = int(opcion)
    match opcion:
        # Agregar producto
        case 1:
            agregar_producto()
        # Mostrar productos    
        case 2:
            consultar_productos()
        # Buscar producto
        case 3:
            buscar_producto()
        # Eliminar producto
        case 4:
            eliminar_producto()
        # Modificar producto
        case 5:
            modificar_producto()
        # Consultar productos por nivel de stock
        case 6:
            reporte_bajo_stock()
        # Salir
        case 7:
            print(Fore.GREEN + "Gracias por utilizar el Sistema de Gestión de Productos. ¡Hasta luego!")
            break
        case _:
            print(Fore.RED + "Opción no válida. Por favor, elige una opción numérica del menú para continuar." + Style.RESET_ALL)
            continue