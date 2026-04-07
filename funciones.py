# Punto 1: promedio y nota mayor y minima
def promedio(notas):
    return sum(notas) / len(notas)

def nota_mas_alta(notas):
    return max(notas)

def nota_mas_baja(notas):
    return min(notas)

notas = [3.7, 4.2, 3.0, 5.0, 3.9]

print("Promedio:", promedio(notas))
print("Nota más alta:", nota_mas_alta(notas))
print("Nota más baja:", nota_mas_baja(notas))
# Punto 2: Usa una lista de tuplas (nombre, nota) y una función que devuelva solo los estudiantes aprobados (nota ≥ 3.0).
def aprobados(estudiantes):
    resultado = []
    for nombre, nota in estudiantes:
        if nota >= 3.0:
            resultado.append((nombre, nota))#resultado.append es para agregar datos
    return resultado
estudiantes = [
    ("stephanie", 3.5),
    ("Luisa", 2.8),
    ("Carlitos", 4.0),
    ("valentina", 2.9),
    ("laura", 3.0)
]
print(aprobados(estudiantes))
# Punto 3: Implementa una agenda simple con funciones para agregar, buscar y eliminar contactos usando un diccionario.
def agregar_contacto(agenda):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono
    print("Contacto agregado.\n")

def buscar_contacto(agenda):
    nombre = input("Nombre a buscar: ")
    if nombre in agenda:
        print("Teléfono:", agenda[nombre], "\n")
    else:
        print("Contacto no encontrado.\n")

def eliminar_contacto(agenda):
    nombre = input("Nombre a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado.\n")
    else:
        print("Contacto no existe.\n")

def mostrar_contactos(agenda):
    if agenda:
        print("Agenda:")
        for nombre, telefono in agenda.items():
            print(nombre, ":", telefono)
        print()
    else:
        print("La agenda está vacía.\n")

agenda = {}

while True:
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar contactos")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_contacto(agenda)
    elif opcion == "2":
        buscar_contacto(agenda)
    elif opcion == "3":
        eliminar_contacto(agenda)
    elif opcion == "4":
        mostrar_contactos(agenda)
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.\n")
        
# Punto 3.2: Agenda mas  simple
def agregar_contacto(agendu):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    agendu[nombre] = telefono
    print("Contacto agregado.\n")

def buscar_contacto(agendu):
    nombre = input("Nombre a buscar: ")
    if nombre in agendu:
        print("Teléfono:", agendu[nombre], "\n")
    else:
        print("Contacto no encontrado.\n")

def eliminar_contacto(agendu):
    nombre = input("Nombre a eliminar: ")
    if nombre in agendu:
        del agendu[nombre]
        print("Contacto eliminado.\n")
    else:
        print("Contacto no existe.\n")

agendu = {}

while True:
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_contacto(agenda)
    elif opcion == "2":
        buscar_contacto(agenda)
    elif opcion == "3":
        eliminar_contacto(agenda)
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.\n")

# Punto 4: Gestiona un inventario donde cada producto tiene nombre, precio y cantidad. Calcula el valor total del inventario.
def agregar_producto(inventario):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    
    inventario[nombre] = {"precio": precio, "cantidad": cantidad}
    print("Producto agregado.\n")

def calcular_valor_total(inventario):
    total = 0
    for producto in inventario.values():
        total += producto["precio"] * producto["cantidad"]
    return total

inventario = {}

while True:
    print("1. Agregar producto")
    print("2. Calcular valor total")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        agregar_producto(inventario)
    elif opcion == "2":
        print("Valor total del inventario:", calcular_valor_total(inventario), "\n")
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.\n")

# 5. Dada una lista de palabras, construye un diccionario con la frecuencia de aparición de cada una.
from collections import Counter
lista_palabras = ["manzana", "rey", "peon", "rey", "caja", "reina", "rey", "queso", "peon"]
aparicion = Counter(lista_palabras)
print(aparicion)

# Punto 6
print("Mete las temperaturas de cada dia de la semmana: ")
numeros = []
for i in range(7):
    temperaturas = float(input("Ingresa la temperatura: "))
    numeros.append(temperaturas)

print("La mayor temperatura es: ", max(numeros))
print("La menor temperatura es: ", min(numeros))

# 7. Convierte notas numéricas a letras (A, B, C, D, F) usando tuplas como rangos y devuelve un reporte por estudiante.
# Puntaje de 0-100, osea cada letra abarca 20 puntos F: 0-19, D: 20-39, C: 40-59, B: 60-79, A: 80-100.
tuplaA = (80, 100)
tuplaB = (60, 79)
tuplaC = (40, 59)
tuplaD = (20, 39)
tuplaF = (0, 19)

nota_estudiante = float(input("Ingresa tu nota: "))
if tuplaA[0] <= nota_estudiante <= tuplaA[1]:
  print("Tienes un A")
elif tuplaB[0] <= nota_estudiante <= tuplaB[1]:
  print("Tienes un B")
elif tuplaC[0] <= nota_estudiante <= tuplaC[1]:
  print("Tienes un C")
elif tuplaD[0] <= nota_estudiante <= tuplaD[1]:
  print("Tienes un D")
elif tuplaF[0] <= nota_estudiante <= tuplaF[1]:
  print("Tienes un F")

# 8. Simula un carrito de compras con funciones para agregar productos, aplicar descuentos y generar el total a pagar.
productos = {
    "Xbox Series S": 1500000,
    "Xbox Series X" : 2500000,
    "PlayStation 5 Pro": 3000000,
    "PlayStation 5 Slim Digital": 2100000,
    "Nintendo Switch": 1600000,
    "Nintendo Switch 2": 2900000,
}
carrito = []
total = 0

cantidad = int(input("¿Cuántos objetos deseas comprar? "))

for i in range(cantidad):
    nombre_prod = input(f"Producto {i+1} - Escribe el nombre exacto: ")

    if nombre_prod in productos:
        precio = productos[nombre_prod]
        carrito.append(nombre_prod)
        total += precio  # Sumamos al total
        print(" {nombre_prod} agregado.")
    else:
        print("Ese producto no existe en la tienda.")

# Descuento si gasta mas de 5 millones
if total > 5000000:
    descuento = total * 0.10
    total -= descuento
    print("¡Descuento aplicado del 10%!: -${descuento}")

print("Tu carrito final es: {carrito}")
print("Total a pagar: {total}")

# 9. Dado un listado de tuplas (producto, categoría), agrupa los productos por categoría usando un diccionario de listas.
productos_categoria= [
    ("Celular", "Tecnología"), ("Televisor", "Tecnología"), 
    ("Computador", "Tecnología"), ("Audifonos", "Tecnología"),
    ("Meson", "Hogar"), ("Mesa", "Hogar"), 
    ("Escoba", "Hogar"), ("Cama", "Hogar"),
    ("Cuchillos", "Cocina"), ("Microondas", "Cocina"), 
    ("Nevera", "Cocina"), ("Estufa", "Cocina")
]

diccionario_agrupado = {}

for producto, categoria in productos_categoria:
    if categoria not in diccionario_agrupado:
        diccionario_agrupado[categoria] = []
    
    diccionario_agrupado[categoria].append(producto)

print("--- Diccionario Agrupado ---")
for cat, prods in diccionario_agrupado.items():
    print(f"{cat}: {prods}")
    
# Punto 10. Registra votos de una lista de candidatos, detecta votos inválidos y determina el ganador con su porcentaje.
def registrar_votos(candidatos):
    votos = {candidato: 0 for candidato in candidatos}
    invalidos = 0
    
    cantidad = int(input("¿Cuántos votos se registrarán?: "))
    
    for i in range(cantidad):
        voto = input(f"Voto #{i+1}: ")
        
        if voto in candidatos:
            votos[voto] += 1
        else:
            invalidos += 1
    
    return votos, invalidos

def calcular_ganador(votos):
    total_validos = sum(votos.values())
    
    if total_validos == 0:
        return None, 0
    
    ganador = max(votos, key=votos.get)
    porcentaje = (votos[ganador] / total_validos) * 100
    
    return ganador, porcentaje

candidatos = ["Ana", "Luis", "Carlos"]

votos, invalidos = registrar_votos(candidatos)

print("\nResultados:")
for candidato, cantidad in votos.items():
    print(candidato, ":", cantidad)

print("Votos inválidos:", invalidos)

ganador, porcentaje = calcular_ganador(votos)

if ganador:
    print(f"Ganador: {ganador} con {porcentaje:.2f}% de los votos válidos")
else:
    print("No hubo votos válidos")