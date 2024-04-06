def ejercicio1():
    ctdad_mayores_18 = 0
    ctdad_menores_18 = 0
    suma_mayores_18 = 0
    suma_menores_18 = 0

    # Entrada
    a = int(input(f"Ingrese la edad de la persona a incluir. Solo se aceptan numeros positivos: "))

    # Proceso
    while a != -1:
        if a > 100 or a < 0:
            print("Ingrese un numero positivo entre 0 y 100")
        elif a >= 18:
            ctdad_mayores_18 += 1
            suma_mayores_18 += a
        else:
            ctdad_menores_18 += 1
            suma_menores_18 += a
        a = int(input(f"Ingrese la edad de la próxima persona a incluir, o -1 para terminar el cálculo: "))

    print(f"De las personas incluidas, "
          f"hay {ctdad_mayores_18} mayores de edad, con un promedio de {suma_mayores_18 / ctdad_menores_18} años, "
          f"y {ctdad_menores_18} menores de edad, con un promedio de {suma_menores_18 / ctdad_menores_18} años.")
    return


def ejercicio2():
    ctdad_aprobados = 0
    ctdad_reprobados = 0
    ctdad_aplazados = 0

    # Entrada
    a = int(input(f"Ingrese la nota del estudiante: "))

    # Proceso
    while a != -1:
        if a > 10 or a < 0:
            print("Ingrese un numero positivo entre 0 y 100")
        elif 4 < a <= 10:
            ctdad_aprobados += 1
        elif 2 < a <= 4:
            ctdad_aplazados += 1
        else:
            ctdad_reprobados += 1
        a = int(input(f"Ingrese la nota del próximo estudiante, o -1 para terminar el cálculo: "))
    total_estudiantes = ctdad_aprobados + ctdad_reprobados + ctdad_aplazados

    print(f"De las personas incluidas, "
          f"hay {ctdad_aprobados} aprobados, "
          f"{ctdad_reprobados} reprobados, y {round(((ctdad_aplazados * 100) / total_estudiantes), 2)}% de "
          f"estudiantes aplazados.")
    return


def ejercicio3():
    return


if __name__ == '__main__':
    ejercicio2()
