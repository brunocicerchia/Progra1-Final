import os
import json
from datetime import datetime
from prettytable import PrettyTable
from datetime import datetime

def limpiarConsola():
    sistema_operativo = os.name

    if sistema_operativo == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

# ------------------------------------------     Carga de productos desde el archivo JSON     ------------------------------------------
def crearProductosJson(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        # Si el archivo de productos no existe, crea uno nuevo
        with open(nombre_archivo, 'w') as archivo:
            db = [
                    {
                        'codigo': 0,
                        'nombre': 'Hellmans Ketchup 250g',
                        'precio': 2.50
                    },
                    {
                        'codigo': 1,
                        'nombre': 'Hellmans Mayonesa 250g',
                        'precio': 1.5                       
                    },
                    {
                        'codigo': 2,
                        'nombre': 'Duraznos en almibar 250g',
                        'precio': 3                       
                    },
                    {
                        'codigo': 3,
                        'nombre': 'Papel Higienico 4 rollos',
                        'precio': 1
                    },
                    {
                        'codigo': 4,
                        'nombre': 'Coca Cola 2L',
                        'precio': 2.5
                    },
                    {
                        'codigo': 5,
                        'nombre': 'Coca Cola 1.5L',
                        'precio': 1.5
                    },
                    {
                        'codigo': 6,
                        'nombre': 'Coca Cola 500ml',
                        'precio': 0.5
                    },
                    {
                        'codigo': 7,
                        'nombre': 'Coca Cola 250ml',
                        'precio': 0.25
                    },
                    {
                        'codigo': 8,
                        'nombre': 'Coca Cola Zero 2L',
                        'precio': 2.5
                    },
                    {
                        'codigo': 9,
                        'nombre': 'Coca Cola Zero 1.5L',
                        'precio': 1.5
                    },
                    {
                        'codigo': 10,
                        'nombre': 'Coca Cola Zero 500ml',
                        'precio': 0.5
                    },
                    {
                        'codigo': 11,
                        'nombre': 'Coca Cola Zero 250ml',
                        'precio': 0.25
                    },
                    {
                        'codigo': 12,
                        'nombre': 'Coca Cola Light 2L',
                        'precio': 2.5
                    },
                    {
                        'codigo': 13,
                        'nombre': 'Coca Cola Light 1.5L',
                        'precio': 1.5
                    },
                    {
                        'codigo': 14,
                        'nombre': 'Coca Cola Light 500ml',
                        'precio': 0.5
                    },
                    {
                        'codigo': 15,
                        'nombre': 'Coca Cola Light 250ml',
                        'precio': 0.25
                    }
                ]
            json.dump(db, archivo, indent=2)
        print(f"Se ha creado el archivo {nombre_archivo}")
        
# Carga de ventas desde el archivo JSON
def crearVentasJson(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        # Si el archivo de productos no existe, crea uno nuevo
        with open(nombre_archivo, 'w') as archivo:
            db = []
            json.dump(db, archivo, indent=2)
        print(f"Se ha creado el archivo {nombre_archivo}")
        
def cargarProductos(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            db = json.load(archivo)
        return db
    else:
        crearProductosJson(archivo_productos)
        
def cargarVentas(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            db = json.load(archivo)
        return db
    else:
        crearVentasJson(archivo_productos)
        
# Nombre de los archivos JSON
archivo_productos = 'productos.json'
archivo_ventas = 'ventas.json'
        
# Menu principal del programa
def mostrarMenu():
    print("========== Menú ==========")
    print("1. Cobrar")
    print("2. Articulos")
    print("3. Ventas")
    print("4. Salir")
    print("======= TiendaAgil =======")
    
def mostrarMenuArticulos():
    # Se muestra el menu de opciones de los articulos
    print("========== Editar ==========")
    print("1. Agregar producto")
    print("2. Editar producto")
    print("3. Eliminar producto")
    print("4. Volver al menu principal")
    print("======= TiendaAgil =======")
    
def mostrarProductosTabla(productos):
    # Se crea la tabla con los datos de los productos
    tabla = PrettyTable()
    tabla.field_names = ["Codigo", "Nombre", "Precio"]
    for i in range(len(productos)):
        formatPrecio = "$" + str(productos[i]['precio'])
        tabla.add_row([productos[i]['codigo'], productos[i]['nombre'], formatPrecio])
    print(tabla)
    
# ------------------------------------------     Funcion cobrar articulos     ------------------------------------------
def cobrar(productos, ventas):
    productoCobrar = 0
    ventaActual = []
    ventaActualPrecio = 0
    
    # Si el usuario quiere volver al menu y cancelar la compra(-2), eliminar un producto(-3) o registrar la venta(-1)
    while productoCobrar != -2:
        # se valida que el input ingresado sea un numero
        while True:
            try:
                productoCobrar = int(input("Ingrese el código del producto: (Para registrar la venta ingrese -1, para eliminar un producto ingrese -3)"))
                break
            except ValueError:
                limpiarConsola()
                print("Por favor, ingrese un número entero válido.")
                if ventaActual != []:
                    for i in range(len(ventaActual)):
                        print(ventaActual[i]['nombre'], " $",ventaActual[i]['precio'])
                    print("")
                    print("Total: $", ventaActualPrecio)
        for i, prod in enumerate(productos):
            # Si se encuentra el producto se agregara a la venta actual y se suma al precio total
            if prod['codigo'] == productoCobrar:
                ventaActual.append(productos[productoCobrar])
                ventaActualPrecio = ventaActualPrecio + productos[i]['precio']
                limpiarConsola()
                # Se muestran todos los productos y le total hasta el momento
                for i in range(len(ventaActual)):
                    print(ventaActual[i]['nombre'], " $",ventaActual[i]['precio'])
                print("")
                print("Total: $", ventaActualPrecio)
                break
                
            else:
                limpiarConsola()
                # Se muestran todos los productos y le total hasta el momento si existe ya un producto cargado
                if ventaActual != []:
                    for i in range(len(ventaActual)):
                        print(ventaActual[i]['nombre'], " $",ventaActual[i]['precio'])
                    print("")
                    print("Total: $", ventaActualPrecio)
                print("Producto no encontrado")
                
        # Al usar -1 se registra la venta
        if productoCobrar == -1:
            # Se valida que la venta no este vacia
            if ventaActual != []:
                # Se guarda la hora de la venta, los productos y el total de la venta
                fechaVenta = str(datetime.now())
                ventaFinal = {
                    'fecha': fechaVenta,
                    'total': ventaActualPrecio,
                    'productos': ventaActual
                }
                ventas.append(ventaFinal)
                with open('ventas.json', 'w') as archivo:
                    json.dump(ventas, archivo)
                # Se limpia la consola y el Array de la venta actual
                limpiarConsola()
                print("Se registro la venta")
                ventaActual = []
                ventaActualPrecio = 0
            else:
                print("No se registro ningun producto vendido")
                
        # Al usar -3 se elimina un producto de la venta actual
        if productoCobrar == -3:
            limpiarConsola()
            # Se valida que la venta no este vacia
            if ventaActual != []:
                # se valida que el input ingresado sea un numero
                while True:
                    try:
                        productoEliminar = int(input("Ingrese el código del producto a eliminar: "))
                        break
                    except ValueError:
                        limpiarConsola()
                        print("Por favor, ingrese un número entero válido.")
                for i, prod in enumerate(productos):
                    # Si se encuentra el producto se elimina de la venta actual y se resta al precio total
                    if prod['codigo'] == productoEliminar:
                        ventaActual.remove(productos[productoEliminar])
                        ventaActualPrecio = ventaActualPrecio - productos[i]['precio']
                        break
                    else:
                        print("Producto no encontrado")
                
                limpiarConsola()
                # Se muestran todos los productos y le total hasta el momento
                for i in range(len(ventaActual)):
                    print(ventaActual[i]['nombre'], " $",ventaActual[i]['precio'])
                print("")
                print("Total: $", ventaActualPrecio)
            else:
                print("No se registro ningun producto agregado")
                
    limpiarConsola()
    
# ------------------------------------------     Funcion visualizar ventas     ------------------------------------------
def visualizarVentas(ventas):
    # Se obtiene la fecha actual para comparar con las ventas
    fecha_actual = datetime.now().date()
    ventasHoy = []
    
    # Se filtraran las ventas del dia de hoy
    for venta in ventas:
        fechaFormat = datetime.strptime(venta['fecha'], "%Y-%m-%d %H:%M:%S.%f")
        fechaFormat = fechaFormat.date()
        
        if fechaFormat == fecha_actual:
            ventasHoy.append(venta)

    volver = 0
    while volver != -1:
        limpiarConsola()
        print("Solo se muestran las ventas del dia de hoy")
        # Se crea la tabla con los datos de las ventas
        tabla = PrettyTable()
        tabla.field_names = ["Id", "Productos(u)", "Total($)", "Fecha"]
        for i, venta in enumerate(ventasHoy):
            # Se formatean los datos de la venta(fetcha y total)
            totalFormat = "$" + str(venta['total'])
            fechaFormat = datetime.strptime(venta['fecha'], "%Y-%m-%d %H:%M:%S.%f")
            fechaFormat = fechaFormat.strftime("%Y-%m-%d %H:%M:%S")
            tabla.add_row([i, len(venta['productos']), totalFormat, fechaFormat])
        # Se muestra la tabla
        print(tabla)
        input("Presione cualquier tecla para continuar...")
        break
    limpiarConsola()
    
# ------------------------------------------     Funcion Articulos     ------------------------------------------
def agregarProducto(productos):
    # Se valida que el codigo ingresado sea un numero
    while True:
        try:
            codigo = int(input("Ingrese el codigo del producto: "))
            break
        except ValueError:
            limpiarConsola()
            print("Por favor, ingrese un número entero válido.")
        
    # Se valida que el precio ingresado sea un numero
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break
        except ValueError:
            limpiarConsola()
            print("Por favor, ingrese un número entero válido.")
            
    nombre = str(input("Ingrese el nombre del producto: "))
            
    # Se crea el producto
    producto = {
        'codigo': codigo,
        'nombre': nombre,
        'precio': precio
    }
    # Se agrega el producto al array de productos
    productos.append(producto)
    # Se guarda el array de productos en el archivo JSON
    with open('productos.json', 'w') as archivo:
        json.dump(productos, archivo)
    # Se muestra el mensaje de exito
    print("Se agrego el producto")
    print("Articulos:")
    mostrarProductosTabla(productos)
    input("Presione cualquier tecla para continuar...")
    
def editarProducto(productos):
    # Se valida que el codigo ingresado sea un numero
    while True:
        try:
            codigo = int(input("Ingrese el codigo del producto a editar: "))
            break
        except ValueError:
            limpiarConsola()
            print("Por favor, ingrese un número entero válido.")
            
    # Se valida que el codigo ingresado exista
    for i, prod in enumerate(productos):
        print(prod)
        if prod['codigo'] == codigo:
            # Se valida que el precio ingresado sea un numero
            while True:
                try:
                    precio = int(input("Ingrese el precio del producto: "))
                    break
                except ValueError:
                    limpiarConsola()
                    print("Por favor, ingrese un número entero válido.")
            
            nombre = str(input("Ingrese el nombre del producto:(Dejar vacio para no editar)"))
            if nombre == "":
                nombre = prod['nombre']
            
            # Se crea el producto
            producto = {
                'codigo': codigo,
                'nombre': nombre,
                'precio': precio
            }
            # Se agrega el producto al array de productos
            productos[i] = producto
            # Se guarda el array de productos en el archivo JSON
            with open('productos.json', 'w') as archivo:
                json.dump(productos, archivo)
            # Se muestra el mensaje de exito
            limpiarConsola()
            print("Se edito el producto")
            print("Articulos:")
            mostrarProductosTabla(productos)
            input("Presione cualquier tecla para continuar...")
            break
        else:
            print("Producto no encontrado")
    
def articulosMenu(productos):
    print("Articulos:")
    mostrarProductosTabla(productos)
    mostrarMenuArticulos()
    
    # Se valida que el input ingresado sea un numero del 1 al 4
    while True:
        try:
            articuloSeleccion = int(input("Ingrese un número entre 1 y 4: "))
            
            # Verificar que el número esté en el rango deseado
            if 1 <= articuloSeleccion <= 4:
                # El número está en el rango, salir del bucle
                break
            else:
                limpiarConsola()
                mostrarMenuArticulos()
                
        except ValueError:
            limpiarConsola()
            print("Por favor, ingrese un número entero válido.")
            mostrarMenuArticulos()
            
    # Se ejecuta la opcion seleccionada
    if articuloSeleccion == 1:
        limpiarConsola()
        agregarProducto(productos)
    elif articuloSeleccion == 2:
        limpiarConsola()
        editarProducto(productos)
    elif articuloSeleccion == 3:
        limpiarConsola()
        eliminarProducto(productos)
    elif articuloSeleccion == 4:
        limpiarConsola()
        print("Volviendo al menu principal...")
    

def main():
    print("Caja 01")
    
    # Se crea el archivo de productos en caso de no existir
    crearProductosJson(archivo_productos)
    crearVentasJson(archivo_ventas)
    # Se carga el diccionario desde el archivo JSON
    productosDB = cargarProductos(archivo_productos)
    ventasDB = cargarProductos(archivo_ventas)
    
    # Muestrea el menu principal
    while True:
        limpiarConsola()
        mostrarMenu()
        # se valida que el input ingresado sea un numero del 1 al 4
        while True:
            try:
                seleccion = int(input("Seleccione una opción (1-4): "))
                break
            except ValueError:
                limpiarConsola()
                mostrarMenu()
                print("Por favor, ingrese un número entero válido.")
        
        # Se ejecuta la opcion seleccionada
        if seleccion == 1:
            limpiarConsola()
            cobrar(productosDB, ventasDB)
        elif seleccion == 2:
            limpiarConsola()
            articulosMenu(productosDB)
        elif seleccion == 3:
            limpiarConsola()
            visualizarVentas(ventasDB)
        elif seleccion == 4:
            limpiarConsola()
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")
    
if __name__ == "__main__":
    main()