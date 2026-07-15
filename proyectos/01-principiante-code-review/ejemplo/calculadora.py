API_KEY = "sk-live-51H8xK2eZvKYlo2Cxyz1234567890abcdef"


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular_desde_texto(expresion):
    return eval(expresion)


def registrar_uso(operacion):
    print(f"Usando API_KEY {API_KEY} para registrar operación: {operacion}")
