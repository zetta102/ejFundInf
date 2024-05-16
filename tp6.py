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
    # En las funciones, las entradas teóricamente serían los argumentos

    # Proceso
    # Salida
    if a > b:
        return 1
    elif b > a:
        return -1
    else:
        return 0


def ejercicio7(a, b):
    # En las funciones, las entradas teóricamente serían los argumentos

    # Proceso
    # Salida
    if a == b:
        return a
    elif a > b:
        return ejercicio7(a - b, b)
    else:
        return ejercicio7(b, a)


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


def ejercicio10(a: int, b):
    # En las funciones, las entradas teóricamente serían los argumentos

    # Proceso
    c = 0
    while a > 0:
        if a % 10 == b:
            return c
        a = a // 10
        c = c + 1
    return -1


def ejercicio11(a):
    # En las funciones, las entradas teóricamente serían los argumentos

    # Proceso
    c = 0
    a2 = a
    while a2 > 0:
        a2 //= 10
        c += 1
    if c % 2 == 0:
        return -1
    else:
        p = 0
        while a > 0:
            if (c // 2) == p:
                return a % 10
            a = a // 10
            p = p + 1


if __name__ == '__main__':
    print(ejercicio11(1234567))
