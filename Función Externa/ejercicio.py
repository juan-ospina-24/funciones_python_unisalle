from funciones import agregar_producto
from funciones import buscar_producto
from funciones import eliminar_producto
from funciones import mostrar_producto

producto = {}

while True:
    print("1. Agregar Producto")
    print("2. Buscar Producto")
    print("3. Eliminar Producto")
    print("4. Mostrar Producto")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_producto(producto)
    elif opcion == "2":
        buscar_producto(producto)
    elif opcion == "3":
        eliminar_producto(producto)
    elif opcion == "4":
        mostrar_producto(producto)
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.\n")