

# Las listas son estructuras de datos lineales
# se crean usando bracket. ejemplo: my list= []
# Las listan son ordenadas (Orden de insercion), esto quiere decir que el ultimo dato ingresado ocupara la ultima posicion.
# Emplease metodos para manipular items de la misma.
# Como los array la primer posicion inicia en 0
# Permite items duplicados
# Las listas son mutables, es decir que podemos agregar, actualizar o remover items
# Puede contener distintos tipos de datos

nombres= ["Juan", "Pepito","Maria","Lisa"]

# el Metodo len() valida el tamaño de la lista
print(len(nombres))
print(type(nombres))

listaDatos= ["Pepito","Perez",1000100100, 1.80, True]

print (f" EL mumero de doc es: {listaDatos[2]}")

# Slicing de datos 
print (listaDatos[0:2])
# Para imprimir los elementos entre el apellido y altura
print (listaDatos[1:4])
# Para que imprima todo menos true
print (listaDatos[:4])
# Para que imprima del dos hasta el ultimo
print (listaDatos[2:])

# Para que imprima de adelante hacia atrs
print (listaDatos[:-1])
print (listaDatos[:-2])
print (listaDatos[:-3])

print (listaDatos[-4:-1])
print (listaDatos[1:4])

