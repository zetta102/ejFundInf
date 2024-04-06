def ejercicio1(a, b):
    lista = []

    # Entrada
    v = int(input(f"Ingrese número a agregar a la lista. Debe estar entre {a} y {b}: "))

    # Proceso
    while v != -1:
        if a < v <= b:
            lista.append(v)
        else:
            print(f"El número ingreasdo no está entre {a} y {b}")
        v = int(input("Ingrese el próximo dígito a agregar en la lista o -1 para salir: "))
    return lista


def ejercicio2(a, b):
    suma = 0

    # Entrada
    lista = ejercicio1(a, b)

    # Proceso
    for i in lista:
        suma += i

    # Salida
    return suma


def ejercicio3(a, b):
    suma = 0

    # Entrada
    lista = ejercicio1(a, b)

    # Proceso
    for i in lista:
        suma += i

    # Salida
    return suma
