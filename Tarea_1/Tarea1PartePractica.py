import time
seguir = True


def operation_selector(num1, num2, op):
    """
    Realiza una operación entre dos números enteros según el carácter op y realiza verificaciones.

    :param num1: Primer número (debe ser entero).
    :param num2: Segundo número (debe ser entero).
    :param op: Carácter que indica la operación a realizar ('+', '-', '*', '&') (debe ser una cadena).
    :return: Una tupla con un código de error/éxito y el resultado de la operación o None si hay error.
             Código de error: 0 para éxito, 1 para error de tipo de número, 2 para error de tipo de operación.
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
            return 1, None  # Código de error 1: Los números deben ser 0 o 1 para AND lógico
    else:
        return 2, None  # Código de error 2: Operación no válida

def calculo_promedio(lista_valores):
    """
    Calcula el promedio de una lista digitada por el usuario.
    La lista debe contener 10 o menos valores.
    La lista solo puede contener números.

    :param lista_valores: Lista digitada por el usuario.
    :param error: Estado actual del programa el cual contempla éxito o un determinado error.
    :param i: Contador para movilizarse en la lista.
    :param verificador: Valor booleano para determinar si el elemento de la lista es un número.
    """

    #Definición de párametros base
    lista= eval(lista_valores)
    error= "éxito"
    i= 0

    #Verificación de números en lista
    while i < len(lista):
        verificador= isinstance(lista[i], (int, float))
        if verificador == False:
            error= "Error 13: ERROR_INVALID_DATA"
            prom= "None"
            break
        i+= 1

    #Operación de promediado 
    if verificador == True:
        prom= sum(lista)/len(lista)

    #Verificación de cantidad de elementos en lista
    if len(lista) > 10:
        error= "Error 24: ERROR_BAD_LENGTH"
        prom= "None"

    #Resultados
    print("Proceso: ", error)
    print("Resultado: ", prom)

def main():
    try:
        num1 = int(input("Ingresa el primer número entero: "))
        num2 = int(input("Ingresa el segundo número entero: "))
    except ValueError:
        print("Error: Los valores ingresados deben ser números enteros.")
        return

    op = input("Ingresa la operación deseada (+, -, *, &): ").strip()

    codigo_error, resultado = operation_selector(num1, num2, op)  # Se llama a la funcion la cual retorna una tupla

    if codigo_error == 0:
        print(f"El resultado de {num1} {op} {num2} es {resultado}.")
    elif codigo_error == 1:
        print("Error: Los números deben ser enteros y, en el caso de AND lógico, deben ser 0 o 1.")
    elif codigo_error == 2:
        print("Error: Operación no válida o tipo de operación no válida.")

    time.sleep(1)
    input("\n\nPresiona Enter para continuar...")
    print("\n" * 100)  # Limpia la pantalla
    while seguir:  # Parte del codigo que genera una continuidad en el uso del programa: seguir o salir del programa
        sesigue = input("Desea agragar otra operación: Sí(1)   No(0)\nDigite la opción: ")
        if sesigue == "1":
            print("\n" * 100)
            main()
        elif sesigue == "0":
            exit()

if __name__ == "__main__":
    print("\n" * 100)
    main()
