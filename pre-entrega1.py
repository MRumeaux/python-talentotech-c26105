productos = []
print("Bienvenido al Sistema de Gestión de Productos.")


while True:
    opcion = int(input("Por favor, elige una opción numérica del menú para continuar:\n1. Agregar producto\n2. Mostrar productos\n3. Buscar producto\n4. Eliminar producto\n5. Salir\nIngresa el número de la opción que deseas ejecutar: "))
    match opcion:
        # Agregar producto
        case 1:
            nombre = str(input("Ingrese el nombre del producto: ")).capitalize()
            categoria = str(input("Ingrese la categoría del producto: ")).capitalize()
            precio = int(input("Ingrese el precio del producto (sin centavos): "))
            if nombre == "" or categoria == "" or precio == "" or precio < 0:
                print("Se ha ingresado uno o más datos inválidos. Por favor, asegúrate de completar los campos correctamente.")
                continue
            producto = [
                nombre,
                categoria,
                precio
            ]
            productos.append(producto)
            print(f"Producto {nombre} con categoría {categoria} y precio ${precio} agregado al sistema.")
        # Mostrar productos    
        case 2:
            if len(productos) == 0:
                print("Actualmente no hay productos cargados en el sistema.")
            else:
                print("A continuación se muestra la lista completa de productos cargados:")
                for producto in productos:
                    print(f"Producto N°: {productos.index(producto) + 1} | Nombre: {producto[0]} - Categoría: {producto[1]} - Precio: ${producto[2]}")
        # Buscar producto
        case 3:
            if len(productos) == 0:
                print("Actualmente no hay productos cargados en el sistema.")
            else:
                producto_buscado = str(input("Ingrese el nombre del producto a buscar: ")).capitalize()
                if producto_buscado == "":
                    print("El nombre del producto no puede estar vacío. Por favor, ingresa un nombre válido.")
                    continue
                else:
                    print("A continuación se muestran las coincidencias encontradas para el producto buscado:")
                    for producto in productos:
                        if producto_buscado == producto[0]:
                            print(f"Producto encontrado en posición N° {productos.index(producto) + 1}: Nombre: {producto[0]} - Categoría: {producto[1]} - Precio: ${producto[2]}")
        # Eliminar producto
        case 4:
            if len(productos) == 0:
                print("Actualmente no hay productos cargados en el sistema.")
            else:
                print("A continuación se muestra la lista completa de productos cargados:")
                for producto in productos:
                    print(f"Producto N°: {productos.index(producto) + 1} | Nombre: {producto[0]} - Categoría: {producto[1]} - Precio: ${producto[2]}")
                producto_a_eliminar = input("Ingrese el número de posición del producto a eliminar: ")
                if producto_a_eliminar.isdigit():
                    producto_eliminado = productos.pop(int(producto_a_eliminar) - 1)
                    print(f"Producto '{producto_eliminado[0]}' eliminado del sistema.")
                else:
                    print("Por favor, ingresa un valor numérico válido.")
                    continue
        # Salir
        case 5:
            print("Gracias por utilizar el Sistema de Gestión de Productos. ¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Por favor, elige una opción numérica del menú para continuar.")
            continue