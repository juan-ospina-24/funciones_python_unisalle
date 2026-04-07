def agregar_producto(producto):
    nombre = input("Nombre: ")
    valor = input("Valor: ")
    producto[nombre] = valor
    print("Producto agregado.\n")

def buscar_producto(producto):
    nombre = input("Nombre a buscar: ")
    if nombre in producto:
        print("Valor:", producto[nombre], "\n")
    else:
        print("Producto no encontrado.\n")

def eliminar_producto(producto):
    nombre = input("Nombre a eliminar: ")
    if nombre in producto:
        del producto[nombre]
        print("Producto eliminado.\n")
    else:
        print("Producto no existe.\n")

def mostrar_producto(producto):
    if producto:
        print("Agenda:")
        for nombre, valor in producto.items():
            print(nombre, ":", valor)
        print()
    else:
        print("La agenda está vacía.\n")

producto = {}
