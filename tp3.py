def ejercicio1():
    # Entrada
    a = int(input("Ingrese el primer número a comparar: "))
    b = int(input("Ingrese el segundo número a comparar: "))

    # Proceso
    son_iguales = 'son iguales' if (a == b) else 'no son iguales'

    # Salida
    print(f"Los números introducidos {son_iguales}")
    return


def ejercicio2():
    # Entrada
    a = int(input("Ingrese el número a verificar si es par o no: "))

    # Proceso
    es_par = 'es par' if (a % 2 == 0) else 'es impar'

    # Salida
    print(f"El número introducido {es_par}")
    return


def ejercicio3():
    # Entrada
    a = int(input("Ingrese el número del mes cuyo nombre quisiera saber: "))

    # Proceso
    match a:
        case 1:
            mes = 'enero'
        case 2:
            mes = 'febrero'
        case 3:
            mes = 'marzo'
        case 4:
            mes = 'abril'
        case 5:
            mes = 'mayo'
        case 6:
            mes = 'junio'
        case 7:
            mes = 'julio'
        case 8:
            mes = 'agosto'
        case 9:
            mes = 'septiembre'
        case 10:
            mes = 'octubre'
        case 11:
            mes = 'noviembre'
        case 12:
            mes = 'diciembre'
        case _:
            mes = 'inválido. Inserte un número del 1 al 12.'

    # Salida
    print(f"El nombre del mes introducido es {mes}")
    return


def ejercicio4():
    # Entrada
    a = int(input("Ingrese el número de votos a favor: "))
    b = int(input("Ingrese el número de votos en contra: "))

    # Proceso
    votos_total = a + b
    votos_favor = (a / votos_total) * 100
    votos_contra = (b / votos_total) * 100
    es_aprobada = 'aprobada' if votos_favor > votos_contra else 'rechazada'

    # Salida
    print(f"Con {round(votos_favor, 2)}% votos a favor y {round(votos_contra, 2)}% votos en contra "
          f"sobre un total de {votos_total} votos, "
          f"la ley es {es_aprobada}")
    return


def ejercicio5():
    # Entrada
    a = int(input("Ingrese la nota del primer parcial: "))
    b = int(input("Ingrese la nota del segundo parcial: "))

    # Proceso
    promedio = (a + b) / 2
    if (a > 10 or a < 0) or (b > 10 or b < 0):
        resultado = 'ha ingresado valores de las notas incorrectos. Intente de nuevo'
    elif promedio >= 7:
        resultado = 'ha promocionado :)'
    elif promedio >= 4:
        resultado = 'ha aprobado :|'
    else:
        resultado = 'debe recuperar :('

    # Salida
    print(f"El alumno {resultado}")
    return


def ejercicio6():
    # Entrada
    a = int(input("Ingrese el número de páginas del libro: "))

    # Proceso
    if 300 <= a < 600:
        valor_base = 6200
    elif a > 600:
        valor_base = 9560
    else:
        valor_base = 5000

    costo_total = valor_base * (a * 32)

    # Salida
    print(f"El costo total del libro sería de {costo_total}")
    return


def ejercicio7():
    # Entrada
    a = int(input("Ingrese el número de kilómetros del viaje a recorrer: "))

    # Proceso
    if 0 <= a <= 10:
        valor_por_km = 200
    else:
        valor_por_km = 400

    costo_total = (valor_por_km * a) if a > 0 else 2700

    # Salida
    print(f"El costo total del viaje sería de {costo_total}")
    return


def ejercicio8():
    # Entrada
    a = int(input("Ingrese el número del año a verificar si es bisiesto: "))

    # Proceso
    if a % 4 == 0:
        if a % 100 != 0 or a % 400 == 0:
            es_bisiesto = 'es bisiesto'
        else:
            es_bisiesto = 'no es bisiesto'
    else:
        es_bisiesto = 'no es bisiesto'

    # Salida
    print(f"El año {es_bisiesto}")
    return


def ejercicio9():
    # Entrada
    a = int(input("Ingrese el número del día de la fecha: "))
    b = int(input("Ingrese el número del mes de la fecha: "))
    c = int(input("Ingrese el número del año de la fecha: "))

    # Proceso
    if (1 <= a <= 31) and (1 <= b <= 12) and c > 0:
        es_valida = 'es válida'
    else:
        es_valida = 'no es válida'

    # Salida
    print(f"La fecha ingresada {es_valida}")
    return


if __name__ == '__main__':
    ejercicio8()
