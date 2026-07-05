import sqlite3
from colorama import init, Fore, Back, Style

conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()


def solicitar_datos_producto():
    """Solicita y valida los datos de un producto antes de insertarlo o modificarlo."""
    nombre = str(input(Fore.YELLOW + "Ingrese el nombre del producto: ")).capitalize()
    descripcion = str(input(Fore.GREEN + "Ingrese la descripción del producto: ")).capitalize()
    categoria = str(input(Fore.MAGENTA + "Ingrese la categoría del producto: ")).capitalize()
    precio = float(input(Fore.RED + "Ingrese el precio del producto: "))
    cantidad = int(input(Fore.BLUE + "Ingrese la cantidad del producto: "))
    if nombre == "" or precio == "" or precio < 0 or cantidad == "" or cantidad < 0:
        print(Fore.RED + "Se ha ingresado uno o más datos inválidos. Por favor, asegúrate de completar los campos correctamente." + Style.RESET_ALL)
        return
    return nombre, descripcion, categoria, precio, cantidad

def agregar_producto():
    """Registra un nuevo producto en la BD."""
    try:
        nombre, descripcion, categoria, precio, cantidad = solicitar_datos_producto()
        cursor.execute('''
        INSERT INTO productos (nombre, descripcion, categoria, precio, cantidad)
        VALUES
            (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, categoria, precio, cantidad))
        conexion.commit()
        print(Fore.GREEN + f"Producto {nombre} con categoría {categoria}, cantidad {cantidad} y precio ${precio} agregado al sistema." + Style.RESET_ALL)
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al agregar producto: {e}" + Style.RESET_ALL)
        return

def consultar_productos():
    """Visualiza la lista completa de productos."""
    try:
        cursor.execute('SELECT * FROM productos')
        productos_db = cursor.fetchall()
        if len(productos_db) == 0:
            print("Actualmente no hay productos cargados en el sistema.")
            return
        else:
            print("A continuación se muestra la lista completa de productos cargados:")
            colors = [Fore.YELLOW, Fore.GREEN, Fore.MAGENTA, Fore.RED, Fore.BLUE, Fore.CYAN]
            for i, producto in enumerate(productos_db):
                color = colors[i % len(colors)]
                print(color + f"Producto N°: {producto[0]} | Nombre: {producto[1]} - Descripción: {producto[2]} - Categoría: {producto[3]} - Cantidad: {producto[4]} - Precio: ${producto[5]}" + Style.RESET_ALL)
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al consultar productos: {e}" + Style.RESET_ALL)
        return

def buscar_producto():
    """Busca un producto específico por su ID."""
    try:
        producto_buscado = int(input("Ingrese el ID del producto a buscar: "))
        cursor.execute('SELECT * FROM productos WHERE id = ?', (producto_buscado,))
        productos_db = cursor.fetchone()
        if productos_db is None:
            print("Actualmente no hay productos cargados en el sistema con el ID especificado.")
            return
        if producto_buscado == "" or producto_buscado < 0:
            print("El ID del producto no puede estar vacío. Por favor, ingresa un ID válido.")
            return
        else:
            print("A continuación se muestran las coincidencias encontradas para el producto buscado:")
            if producto_buscado == productos_db[0]:
                print(Fore.GREEN + f"Producto N° {productos_db[0]}: Nombre: {productos_db[1]} - Descripción: {productos_db[2]} - Categoría: {productos_db[3]} - Cantidad: {productos_db[4]} - Precio: ${productos_db[5]}" + Style.RESET_ALL)
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al buscar producto: {e}" + Style.RESET_ALL)
        return
    except ValueError:
        print(Fore.RED + "Por favor, ingresa un valor numérico válido para el ID del producto." + Style.RESET_ALL)
        return


def modificar_producto():
    try:
        """Actualiza los datos de un producto existente mediante su ID."""
        consultar_productos()
        producto_buscado = int(input("Ingrese el ID del producto a modificar: "))
        cursor.execute('SELECT * FROM productos WHERE id = ?', (producto_buscado,))
        productos_db = cursor.fetchone()
        if productos_db is None:
            print(Fore.YELLOW + "Actualmente no hay productos cargados en el sistema con el ID especificado." + Style.RESET_ALL)
        else:
            if producto_buscado == "" or producto_buscado < 0:
                print(Fore.RED + "Por favor, ingresa un ID válido." + Style.RESET_ALL)
                return
            else:
                nombre, descripcion, categoria, precio, cantidad = solicitar_datos_producto()
                cursor.execute('''
                UPDATE productos
                SET nombre = ?, descripcion = ?, categoria = ?, precio = ?, cantidad = ?
                WHERE id = ?
                ''', (nombre, descripcion, categoria, precio, cantidad, producto_buscado))
                conexion.commit()
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al intentar modificar el producto: {e}" + Style.RESET_ALL)
        return
    except ValueError:
        print(Fore.RED + "Por favor, ingresa un valor numérico válido para el ID del producto." + Style.RESET_ALL)
        return

def eliminar_producto():
    try:
        """Elimina un producto por su ID."""
        consultar_productos()
        producto_a_eliminar = input("Ingrese el ID del producto a eliminar: ")
        if producto_a_eliminar.isdigit():
            cursor.execute('DELETE FROM productos WHERE id = ?', (int(producto_a_eliminar),))
            conexion.commit()
            print(Fore.GREEN + f"Producto eliminado del sistema.")
        else:
            print(Fore.RED + "Por favor, ingresa un valor numérico válido." + Style.RESET_ALL)
            return
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al eliminar producto: {e}" + Style.RESET_ALL)
        return
    
def reporte_bajo_stock():
    """Muestra productos con stock igual o inferior al límite ingresado."""
    try:
        ingreso_usuario_stock = input("Ingrese la cantidad mínima de stock para consultar productos por igual o debajo de ese número: ")
        if not ingreso_usuario_stock.isdigit() or int(ingreso_usuario_stock) < 0:
            print(Fore.RED + "Por favor, ingresa un valor numérico válido para la cantidad mínima de stock." + Style.RESET_ALL)
            return
        cursor.execute('SELECT * FROM productos WHERE cantidad <= ?', (int(ingreso_usuario_stock),))
        productos_db = cursor.fetchall()
        if len(productos_db) == 0:
            print(Fore.YELLOW + "Actualmente no hay productos cargados en el sistema con stock igual o menor a la cantidad ingresada." + Style.RESET_ALL)
        else:
            print("A continuación se muestran los productos con stock igual o menor a la cantidad ingresada:")
            for producto in productos_db:
                print(Fore.LIGHTBLUE_EX + f"Producto N°: {producto[0]} | Nombre: {producto[1]} - Descripción: {producto[2]} - Categoría: {producto[3]} - Cantidad: {producto[4]} - Precio: ${producto[5]}" + Style.RESET_ALL)
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al generar el reporte: {e}" + Style.RESET_ALL)
        return
