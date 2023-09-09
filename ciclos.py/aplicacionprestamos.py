bicicletas_disponibles = [f"mountain bike {i+1}" for i in range(5)]
usuarios = []

def mostrar_bicicletas_disponibles():
    print("Bicicletas disponibles:")
    for i, bicicleta in enumerate(bicicletas_disponibles):
        if bicicleta:
            print(f"{i+1}. {bicicleta}")

def registrar_usuario():
    num_tarjeta = input("Ingrese el número de tarjeta: ")
    if not num_tarjeta:
        print("No es posible asignar una bicicleta sin número de tarjeta.")
        return
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo electrónico: ")
    usuario = {
        "num_tarjeta": num_tarjeta,
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "bicicleta_prestada": None,
        "origen": None,
        "destino": None
    }
    usuarios.append(usuario)
    print("Usuario registrado con éxito.")
    
    opcion = input("¿Desea prestar una bicicleta? (Sí/No): ").lower()
    if opcion == "si":
        prestar_bicicleta(usuario)

def prestar_bicicleta(usuario):
    mostrar_bicicletas_disponibles()
    if not usuario:
        print("Usuario no válido.")
        return
    if usuario["bicicleta_prestada"]:
        print("Este usuario ya tiene una bicicleta prestada.")
        return
    bicicleta_idx = int(input("Seleccione una bicicleta (ingrese el número): ")) - 1
    if bicicleta_idx < 0 or bicicleta_idx >= len(bicicletas_disponibles):
        print("Bicicleta no válida.")
        return
    if not bicicletas_disponibles[bicicleta_idx]:
        print("La bicicleta seleccionada no está disponible.")
        return
    bicicleta = bicicletas_disponibles[bicicleta_idx]
    usuario["bicicleta_prestada"] = bicicleta
    bicicletas_disponibles[bicicleta_idx] = None
    
    origen = input("Ingrese el origen: ")
    destino = input("Ingrese el destino: ")
    usuario["origen"] = origen
    usuario["destino"] = destino
    print(f"{usuario['nombre']} ha prestado {bicicleta} desde {origen} hasta {destino}.")

def listar_usuarios():
    print("Listado de usuarios:")
    for i, usuario in enumerate(usuarios):
        print(f"{i+1}. {usuario['nombre']} {usuario['apellido']} ({usuario['correo']})")

def listar_prestamos():
    print("Listado de préstamos:")
    for usuario in usuarios:
        if usuario["bicicleta_prestada"]:
            print(f"{usuario['nombre']} {usuario['apellido']} ha prestado {usuario['bicicleta_prestada']} desde {usuario['origen']} hasta {usuario['destino']}.")

while True:
    print("\nMenú:")
    print("1. Registrar usuario")
    print("2. Prestar bicicleta")
    print("3. Listar usuarios")
    print("4. Listar préstamos")
    print("5. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        prestar_bicicleta(None)  # None para usar la función dentro de registrar_usuario
    elif opcion == "3":
        listar_usuarios()
    elif opcion == "4":
        listar_prestamos()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
#Primer momento