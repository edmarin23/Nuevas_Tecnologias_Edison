
# Los diccionarios permiten tener clave: valor
# Son cambiables, no permiten duplicados 
# Desde python 3.7 son ordenados, anterior a esto era desordenado
# Permiten agregar y remover items 
# Son iterables 
# poseen distintos metodos para manipular el dato 
# admiten distintos tipos de datos
usuario= {"nombre":"pepito","apellido": "perez", "edad": 25}

print(usuario)

# Imprime las claves
print(usuario.keys())

# Imprime los valores
print(usuario.values())

# Para conocer el tamño del diccionario, usamos el metodo len()
print(len(usuario))
print(type(usuario))

# Cuando queremos buscar in item especifico podemos usar get()

print(usuario.get("nombre"))

print(usuario["edad"])

# Podemos agregar nuevos items
usuario["correo"]= "pepit@mail.com"

print(usuario.keys())
print(usuario.get("correo"))

# Podemos actualizar un valor

usuario.update({"correo":"pperez@mail.com"})

print(usuario.get("correo"))

# Para quitar
"""
usuario.pop("nombre")
print(usuario.keys())
usuario.popitem()
del usuario ["edad"]
print(usuario.keys())"""


# Para recorrer el diccionario, podemos elegir entre recorrer las claves, recorrer los valores o recorres ambos

#ambos 

for x,y in usuario.items():
    print(x,y)
    
# Recorrer claves

for x in usuario.keys():
    print(x)
    
#Recorrer valores
    
    for y in usuario.values():
        print(y)
        
# Poemos tener un diccionario de diccionarios

usuarios = {"usuario1":{"nombre":"juan", "edad": 12}, "usuario2":{"nombre":"Maria","Edad":15,}, "usuario3":{"nombre": "Julia", "edad":18}}

estudiante1 = {"nota1": 4.5, "nota2":4.3}
estudiante2 = {"nota1": 4.4, "nota2":4.3}
estudiante3 = {"nota1": 4.5, "nota2":4.1}

estudiantes = {
    "estudiante1": estudiante1,
    "estudiante2": estudiante2,
    "estudiante3": estudiante3,
    
}
print(estudiantes["estudiante2"]["nota2"])

