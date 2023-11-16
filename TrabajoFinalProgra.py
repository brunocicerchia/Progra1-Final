import os
import random
import json
import time
import keyboard

# Carga de datos desde el archivo JSON
def crear_archivo_json(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        # Si el archivo no existe, crea uno nuevo
        with open(nombre_archivo, 'w') as archivo:
            db = [
                {'ventas': []},
                {'productos': [
                    {
                        'codigo': '123456789',
                        'nombre': 'Hellmans Ketchup 250g',
                        'precio': 2.50,
                        'stock': 10                        
                    },
                    {}
                    ]}
            ]
            json.dump(db, archivo, indent=2)
        print(f"Se ha creado el archivo {nombre_archivo}")
        
def cargarDiccionario(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            db = json.load(archivo)
        return db
    else:
        crear_archivo_json(archivo_db)
        
# Nombre del archivo JSON
archivo_db = 'db.json'
        
# Menu principal del programa
def mostrarMenu():
    print("========== Menú ==========")
    print("1. Cobrar")
    print("2. Articulos")
    print("3. Ventas")
    print("4. Exportar")
    print("5. Cerrar caja")
    print("6. Salir")
    print("==========================")
    
# Funcion cobrar articulos
def cobrar(productos):
    print("Venta 01")
    ventaActual = []
    
    while True:
        productoCobrar = str(input("Ingrese el código del producto: "))
        for i, prod in enumerate(productos):
            if prod["codigo"] == productoCobrar:
                print("Producto encontrado")
                print("Indice de producto: ", i)
                ventaActual.append(productoCobrar)
                break

def main():
    print("Caja 01")
    
    # Se crea el archivo en caso de no existir
    crear_archivo_json(archivo_db)
    # Se carga el diccionario desde el archivo JSON
    db = cargarDiccionario(archivo_db)
    ventas = db[0]['ventas']
    productos = db[1]['productos']
    print(productos)
    print(ventas)
    
    # Muestrea el menu de opciones
    while True:
        mostrarMenu()
        seleccion = input("Seleccione una opción (1-5): ")
        if seleccion == "1":
            print("Cobrar")
            cobrar(productos)
        elif seleccion == "2":
            print("Articulos")
        elif seleccion == "3":
            print("Ventas")
        elif seleccion == "4":
            print("Exportar")
        elif seleccion == "5":
            print("Cerrar caja")
        elif seleccion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")
    
if __name__ == "__main__":
    main()