import Tarea1PartePractica
import random
import string

# Codigos de retorno esperados
# Caso de éxito => 0

# Errores esperados metodo operation_selector
# Error en caso de que los parámetros num1 y num2 no sean enteros => -50
# Error en caso de que el parámetro op no ea string => -60
# Error en caso de que el parámetro op sea string pero distinto
# de +, -, *, & => -70

# Errores esparados metodo de calculo_promedio
# Error en caso de que la lista posea un elemento no número => -80
# Error en caso de que la lista posea más de 10 elementos => -90


# Prueba 1
# Verifica todos los casos de error de la solución
def test_casos_error_operation_selector():
    # Error por operando num1 y num2 erróneos
    estado, res1 = Tarea1PartePractica.operation_selector(7, 7.1, "+")
    assert estado == 1
    assert res1 is None
    estado, res1 = Tarea1PartePractica.operation_selector(12, "s", "*")
    assert estado == 1
    assert res1 is None
    estado, res1 = Tarea1PartePractica.operation_selector(True, 7, "-")
    assert estado == 1
    assert res1 is None
    estado, res1 = Tarea1PartePractica.operation_selector(None, 77, "&")
    assert estado == 1
    assert res1 is None

    # Error por operando op no string
    estado, res1 = Tarea1PartePractica.operation_selector(
        10, 10, 3)
    assert estado == 2
    assert res1 is None
    estado, res1 = Tarea1PartePractica.operation_selector(
        10, 10, 3.7)
    assert estado == 2
    assert res1 is None
    estado, res1 = Tarea1PartePractica.operation_selector(
        10, 10, True)
    assert estado == 2
    assert res1 is None

    # Error por operando op distinto a +, -, *, &
    random_letter = random.choice(string.ascii_letters)
    estado, res1 = Tarea1PartePractica.operation_selector(
        10, 10, random_letter)
    assert estado == 3
    assert res1 is None


# Prueba 2
# Verifica casos de exito de la funcion
def test_casos_exito_operation_selector():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    res_esperado = num1+num2
    estado, res1 = Tarea1PartePractica.operation_selector(num1, num2, "+")
    assert estado == 0
    assert res1 == res_esperado

    res_esperado = num1-num2
    estado, res1 = Tarea1PartePractica.operation_selector(num1, num2, "-")
    assert estado == 0
    assert res1 == res_esperado

    res_esperado = num1*num2
    estado, res1 = Tarea1PartePractica.operation_selector(num1, num2, "*")
    assert estado == 0
    assert res1 == res_esperado

    res_esperado = num1 & num2
    estado, res1 = Tarea1PartePractica.operation_selector(num1, num2, "&")
    assert estado == 0
    assert res1 == res_esperado


# Prueba 3
# Verifica los casos de error de la funcion de numeros primos
def test_casos_error_calculo_promedio():
    # Error por elemento no número
    estado, result = Tarea1PartePractica.calculo_promedio([1, 2, 3, "4"])
    assert estado == 13
    assert result is None

    estado, result = Tarea1PartePractica.calculo_promedio([1, True, 3, 4])
    assert estado == 13
    assert result is None

    # Error por tamaño de lista
    estado, result = Tarea1PartePractica.calculo_promedio(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    assert estado == 24
    assert result is None


# Prueba 4
# Verifica los casos de exito de la funcion de números primos
def test_casos_calculo_promedio():
    lista_valores = []
    for i in range(10):
        lista_valores.append(random.randint(-100, 100))

    promedio = sum(lista_valores)/len(lista_valores)

    estado, result = Tarea1PartePractica.calculo_promedio(lista_valores)
    assert estado == 0
    assert result == promedio
