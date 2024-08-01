def operation_selector(num1, num2, op):
    """
    Realiza una operación entre dos números enteros según el carácter op y
    realiza verificaciones.

    :param num1: Primer número (debe ser entero).
    :param num2: Segundo número (debe ser entero).
    :param op: Carácter que indica la operación a realizar ('+', '-', '*', '&')
    (debe ser una cadena).
    :return: Una tupla con un código de error/éxito y el resultado de la
    operación o None si hay error.
             Código de error: 0 para éxito, 1 para error de tipo de número, 2
             para error de tipo de operación.
    """
    # Verificación de tipo de números
    if not isinstance(num1, int) or not isinstance(num2, int):
        return 1, None  # Código de error 1: Tipo de número no válido

    # Verificación de tipo de operación
    if not isinstance(op, str):
        return 2, None  # Código de error 2: Tipo de operación no válido

    # Verificación de operación válida
    if op == '+':
        return 0, num1 + num2  # Código de éxito 0
    elif op == '-':
        return 0, num1 - num2  # Código de éxito 0
    elif op == '*':
        return 0, num1 * num2  # Código de éxito 0
    elif op == '&':
        if num1 in [0, 1] and num2 in [0, 1]:
            return 0, num1 & num2  # Código de éxito 0
        else:
            return 1, None  # Código de error 1: Los números deben ser 0 o 1
    else:
        return 3, None  # Código de error 2: Operación no válida


def calculo_promedio(lista_valores):
    """
    Calcula el promedio de una lista digitada por el usuario.
    La lista debe contener 10 o menos valores.
    La lista solo puede contener números.

    :param lista_valores: Lista digitada por el usuario.
    :param error: Estado actual del programa el cual contempla éxito o un
    determinado error.
    :param i: Contador para movilizarse en la lista.
    :param verificador: Valor booleano para determinar si el elemento de la
    lista es un número.
    """

    # Definición de párametros base
    lista = eval(lista_valores)
    error = 0  # "éxito"
    i = 0

    # Verificación de números en lista
    while i < len(lista):
        verificador = isinstance(lista[i], (int, float))
        if not verificador == 1:
            error = 13  # "Error 13: ERROR_INVALID_DATA"
            prom = "None"
            break
        i += 1

    # Operación de promediado
    if verificador is True:
        prom = sum(lista) / len(lista)

    # Verificación de cantidad de elementos en lista
    if len(lista) > 10:
        error = 24  # "Error 24: ERROR_BAD_LENGTH"
        prom = "None"

    # Resultados
    return error, prom
