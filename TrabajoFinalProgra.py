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
    print("4. Exportar")
    print("5. Salir")
    print("======= TiendaAgil =======")
    
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
                productoCobrar = int(input("Ingrese el código del producto: "))
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
        # se valida que el input ingresado sea un numero del 1 al 5
        while True:
            try:
                seleccion = int(input("Seleccione una opción (1-5): "))
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
            print("Articulos")
        elif seleccion == 3:
            limpiarConsola()
            visualizarVentas(ventasDB)
        elif seleccion == 4:
            print("Exportar")
        elif seleccion == 5:
            limpiarConsola()
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")
    
if __name__ == "__main__":
    main()