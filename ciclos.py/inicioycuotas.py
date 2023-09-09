# Generar un programa que permita hacer el registro e iniciar sesion dentro de while, debe imprimir el menu usando la implementacion de if, elif , else (Selector multiple). Cuando inicie sesion que implemente la solucion del calculo de cuotas creada en el reto anterio.   


def registro():
    print("Formulario de registro")
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    return usuario, contraseña
def login(datos_registro):
    print("Formulario de login")
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    if usuario == datos_registro[0] and contraseña == datos_registro[1]:
        return True
    else:
        return False
def compras():
    valor_compra = float(input("Valor de la compra: "))
    num_cuotas = int(input("Número de cuotas a pagar: "))
    valor_cuota = valor_compra / num_cuotas
    print(f"El valor de cada cuota es: {valor_cuota}")
    while valor_compra > 0:
        pago = float(input("Ingrese el pago: "))
        if pago == valor_cuota:
            valor_compra -= pago
            num_cuotas -= 1
            print(f"Quedan {num_cuotas} cuotas por pagar")
        else:
            print("El pago no es igual al valor de la cuota")
