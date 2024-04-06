def ejercicio2():
    # Entrada
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))

    # Proceso
    suma = a + b
    resta = a - b

    # Salida
    print(f"El resultado de sumar a y b es {suma}, y el resultado de restarlos es {resta}")
    return


def ejercicio3():
    # Entrada
    a = int(input("Ingrese la nota del primer parcial: "))
    b = int(input("Ingrese la nota del segundo parcial: "))

    # Proceso
    promedio = (a + b) / 2

    # Salida
    print(f"El promedio de las notas ingresadas es {promedio}")
    return


def ejercicio4():
    # Entrada
    a = int(input("Ingrese la edad de la persona: "))

    # Proceso
    edad_en_dias = a * 365

    # Salida
    print(f"La edad de la persona en días es {edad_en_dias}")
    return


def ejercicio5():
    # Entrada
    a = int(input("Ingrese el precio del medicamento: "))

    # Proceso
    monto_de_descuento = a * 0.35
    precio_total = a - monto_de_descuento

    # Salida
    print(f"El precio original del medicamento es {a}. Se hace un descuento de {monto_de_descuento}, por lo que el "
          f"total a pagar es {precio_total}.")
    return


def ejercicio6():
    # Entrada
    a = int(input("Ingrese el capital que aportó la primera persona: "))
    b = int(input("Ingrese el capital que aportó la segunda persona: "))
    c = int(input("Ingrese el capital que aportó la tercera persona: "))

    # Proceso
    capital_total = a + b + c
    aporte_a = (a / capital_total) * 100
    aporte_b = (b / capital_total) * 100
    aporte_c = (c / capital_total) * 100

    # Salida
    print(f"De la persona A a la C, sus aportes fueron los siguientes: "
          f"{aporte_a}%, {aporte_b}% y {aporte_c}% sobre un capital "
          f"total de {capital_total}.")
    return


def ejercicio7():
    # Entrada
    a = int(input("Ingrese el capital que desea dejar en el banco: "))

    # Proceso
    ganancia_en_un_mes = a * 0.02
    ganancia_en_seis_meses = ganancia_en_un_mes * 6

    # Salida
    print(f"Si deja {a} en el banco, a lo largo de un mes "
          f"ganará {ganancia_en_un_mes}, y {ganancia_en_seis_meses} a lo largo de seis meses.")
    return


def ejercicio8():
    # Entrada
    a = int(input("Ingrese el valor en metros que desea convertir: "))

    # Proceso
    valor_en_cm = a * 100
    valor_en_in = valor_en_cm / 2.54
    valor_en_ft = valor_en_in / 12
    valor_en_yd = valor_en_ft / 3

    # Salida
    print(f"{a} metros son {valor_en_cm} centímetros, "
          f"{valor_en_in} pulgadas, "
          f"{valor_en_ft} pies, "
          f"y {valor_en_yd} yardas.")
    return


def ejercicio9():
    # Entrada
    a = int(input("Ingrese el número que identifica al vendedor: "))
    b = int(input("Ingrese el número de ventas que hizo el vendedor: "))
    c = int(input("Ingrese el valor de cada una de las ventas: "))

    # Proceso
    ventas_totales = b * c
    comision_vendedor = ventas_totales * 0.05
    salario_vendedor = 250000 + (b * 50000) + comision_vendedor

    # Salida
    print(f"El vendedor {a} recibirá una paga de {salario_vendedor}")
    return


def ejercicio10():
    # Entrada
    a = int(input("Ingrese el largo de la parcela: "))
    b = int(input("Ingrese el ancho de la parcela: "))

    # Proceso
    m2 = a * b
    quintales = (2 * m2) / 10

    # Salida
    print(f"El productor obtendrá un rendimiento de {quintales} quintales de trigo.")
    return


def ejercicio11():
    # Entrada
    a = int(input("Ingrese el período en segundos: "))

    # Proceso
    dias = a // 86400
    horas = (a - (dias * 86400)) // 3600
    minutos = (a - ((dias * 86400) + (horas * 3600))) // 60
    segundos = (a - ((dias * 86400) + (horas * 3600) + (minutos * 60)))

    # Salida
    print(f"{a} segundos son {dias} dias, {horas} horas, {minutos} minutos, y {segundos} segundos.")
    return


def ejercicio12():
    # Entrada
    a = int(input("Ingrese el valor a devolver en billetes: "))

    # Proceso
    mil = a // 1000
    quinientos = (a - (mil * 1000)) // 500
    cien = (a - ((mil * 1000) + (quinientos * 500))) // 100
    cincuenta = (a - ((mil * 1000) + (quinientos * 500) + (cien * 100))) // 50
    diez = (a - ((mil * 1000) + (quinientos * 500) + (cien * 100) + (cincuenta * 50))) // 10
    cinco = (a - ((mil * 1000) + (quinientos * 500) + (cien * 100) + (cincuenta * 50) + (diez * 10))) // 5
    uno = (a - ((mil * 1000) + (quinientos * 500) + (cien * 100) + (cincuenta * 50) + (diez * 10) + (cinco * 5)))

    # Salida
    print(f"Para devolver {a} usando la menor cantidad de billetes, necesitas "
          f"{mil} billetes de 1000, "
          f"{quinientos} billetes de 500, "
          f"{cien} billetes de 100, "
          f"{cincuenta} billetes de 50, "
          f"{diez} billetes de 10, "
          f"{cinco} billetes de 5, "
          f"y {uno} billetes de 1.")
    return


def ejercicio13():
    # Entrada
    a = str(int(input("Ingrese el número binario de 4 cifras a convertir en decimal: ")))

    # Proceso
    primero = int(a[0]) * pow(2, 3)
    segundo = int(a[1]) * pow(2, 2)
    tercero = int(a[2]) * pow(2, 1)
    cuarto = int(a[3]) * pow(2, 0)
    valor_convertido = primero + segundo + tercero + cuarto

    # Salida
    print(f"{a} convertido es: {valor_convertido}")
    return


if __name__ == '__main__':
    ejercicio13()
