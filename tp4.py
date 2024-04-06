import sys


def ejercicio1():
    # Entrada
    a = int(input("Ingrese el primer número de la lista de valores: "))
    b = 0
    v = 0

    # Proceso
    # Se asume que el valor -1 servirá solo para salir de la lectura y no como valor final,
    # ya que si así fuera, el último valor siempre sería 1
    while v != -1:
        v = int(input("Ingrese el último número de la lista de valores o -1 para salir: "))
        b = v if v != -1 else b

    # Salida
    print(f"El primer número introducido fue {a}, y el último fue {b}")
    return


def ejercicio2():
    # TODO: no se me ocurre todavía cómo plantearlo bajo las restricciones que impone el enunciado

    # Entrada

    # Proceso

    # Salida
    return


def ejercicio3():
    # Acá estoy usando la constante maxsize que la da Python y representa el valor máximo posible
    # que puede tener un número entero
    valor_min = sys.maxsize
    valor_max = -sys.maxsize

    # Entrada
    a = int(input("Ingrese el primer número de la lista de valores: "))

    # Proceso
    while a != -1:
        valor_max = a if a > valor_max else valor_max
        valor_min = a if a < valor_min else valor_min
        a = int(input("Ingrese el próximo número de la lista de valores o -1 para salir: "))

    # Salida
    print(f"De la lista de valores introducidos, el máximo es {valor_max}, y el mínimo es {valor_min}")
    return


def ejercicio4():
    suma_impares = 0

    # No hay entrada, pero lo mantenemos para ser ordenados

    # Proceso
    for i in range(42, 177):
        if i % 2 != 0:
            suma_impares += i

    # Salida
    print(f"La suma de números impares entre 42 y 177 es {suma_impares}")
    return


def ejercicio5():
    # Entrada
    a = int(input("Ingrese el número de números que desee ver: "))

    # Proceso
    for i in range(1, a + 1):
        # Salida
        print(f"{i}")
    return


def ejercicio6():
    # Entrada
    a = int(input("Ingrese el número cuya tabla de multiplicar desee ver: "))

    # Proceso
    for i in range(1, 13):
        # Salida
        print(f"{a} x {i} = {a * i}")
    return


def ejercicio7():
    # Acá estoy usando la constante maxsize que la da Python y representa el valor máximo posible
    # que puede tener un número entero
    valor_max = -sys.maxsize
    posicion_max = 0
    suma_valores = 0

    # Entrada
    # Proceso
    for i in range(1, 11):
        a = int(input(f"Ingrese el número en la posición {i}: "))
        suma_valores += a
        if a > valor_max:
            valor_max = a
            posicion_max = i

    # Salida
    print(f"De los números introducidos, el promedio es {suma_valores / 10}, "
          f"el máximo es {valor_max}, "
          f"y se encuentra en la posición {posicion_max}")
    return


def ejercicio8():
    suma_pares = 0
    contador = 0

    # Entrada
    # Proceso
    while suma_pares != 100:
        a = int(input(f"Ingrese el número a sumar. Solo los pares se tomarán en cuenta: "))
        contador += 1
        if a % 2 == 0:
            suma_pares += a

    print(f"Para llegar a la suma total de 100, se ingresaron {contador} números pares.")
    return


def ejercicio9():
    patentes_pares = 0
    patentes_impares = 0

    # Entrada
    a = int(input("Ingrese el último dígito de la patente: "))

    # Proceso
    while a != -1:
        patentes_pares = patentes_pares + 1 if a % 2 == 0 else patentes_pares
        patentes_impares = patentes_impares + 1 if a % 2 != 0 else patentes_impares
        a = int(input("Ingrese el próximo dígito de la lista de patentes o -1 para salir: "))

    # Salida
    print(f"Circularon {patentes_pares} patentes pares y {patentes_impares} patentes impares")
    return


def ejercicio10():
    # Entrada
    a = int(input("Ingrese el número cuyo factorial desee ver: "))
    factorial = 1

    # Proceso
    for i in range(2, a + 1):
        factorial *= i

    # Salida
    print(f"El factorial de {a} es {factorial}")
    return


def ejercicio11():
    # Entrada
    a = int(input("Ingrese el número para el que desea verificar si es primo: "))

    # Proceso
    if not a % 2 == 0 and not a % 3 == 0 and a % a == 0 and a % 1 == 0:
        es_primo = "es primo."
    else:
        es_primo = "no es primo."

    # Salida
    print(f"El número {a} {es_primo}")
    return


def ejercicio12():
    # Entrada
    a = int(input("Ingrese el el número de iteraciones de Fibonacci que desee ver: "))
    n_menos_dos = 0
    n_menos_uno = 1

    # Proceso
    for i in range(0, a + 1):
        placeholder = n_menos_dos + n_menos_uno
        n_menos_dos = n_menos_uno
        n_menos_uno = placeholder
        # Salida
        print(placeholder)
    return


if __name__ == '__main__':
    ejercicio12()
