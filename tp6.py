def ejercicio1(x, y):
    # En las funciones, las entradas teóricamente serían los argumentos

    # Proceso
    multiplicacion = 0
    for i in range(y):
        multiplicacion += x

    # Salida
    print(f"El resultado de la multiplicación es {multiplicacion}")
    return multiplicacion


def ejercicio2(a, b):
    # En las funciones, las entradas teóricamente serían los argumentos

    # Proceso
    potenciacion = ejercicio1(a, a) if b >= 2 else a
    for i in range(1, b - 1):
        potenciacion = ejercicio1(potenciacion, a)

    # Salida
    print(f"El resultado de elevar {a} por {b} es {potenciacion}")
    return


def ejercicio3(altura):
    # En las funciones, las entradas teóricamente serían los argumentos

    # Proceso
    for i in range(1, altura + 1):
        # Salida
        # Las cadenas se pueden multiplicar como si fueran números,
        # Aunque el resultado es la cadena repetida tantas veces como el número que se use.
        print('*' * i)


def ejercicio4(a, b):
    # En las funciones, las entradas teóricamente serían los argumentos

    # Proceso
    es_multiplo = True if a % b == 0 else False
    texto = "es múltiplo" if es_multiplo else "no es múltiplo"
    # Salida
    print(f"{b} {texto} de {a} ")


def ejercicio5(a):
    # En las funciones, las entradas teóricamente serían los argumentos

    # Proceso
    if a > 0:
        resultado = 1
    elif a < 0:
        resultado = -1
    else:
        resultado = 0

    # Salida
    return resultado


def ejercicio6(a, b):
    # TODO: no se me ocurre todavía cómo plantearlo bajo las restricciones que impone el enunciado

    # Entrada

    # Proceso

    # Salida
    return


def ejercicio7(a, b):
    # TODO: Mucho texto en el enunciado

    # Entrada

    # Proceso

    # Salida
    return


def ejercicio8(a, b):
    # TODO: Mucho texto en el enunciado

    # Entrada

    # Proceso

    # Salida
    return


def ejercicio9(a, b):
    # TODO: Mucho texto en el enunciado

    # Entrada

    # Proceso

    # Salida
    return


def ejercicio10(a, b):
    # TODO: Mucho texto en el enunciado

    # Entrada

    # Proceso

    # Salida
    return


def ejercicio11(a, b):
    # TODO: Mucho texto en el enunciado

    # Entrada

    # Proceso

    # Salida
    return


if __name__ == '__main__':
    print(ejercicio6(4, 2))
