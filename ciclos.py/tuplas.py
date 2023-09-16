
#dias_semana= ("lunes", "martes", "miercoles","jueves", "viernes", "sabado","domingo")
  
#print (type(dias_semana))

#Son inmutables
# para cambiar se debe hacer un casteo 
# Contienen distintos tipos de datos
# Si se require añadir algo en una tupla, se debe convertir primero en una lista
# Se puede acceder la tupla indicando el indice de la misma, el cual comienza desde 0 
# Si se desea recorrer la tupla, se usa el ciclo for 
# Podemos hacer joins entre tupla
# Para conocer el tamaño usamos la funcion len
# Las tuplas permiten duplicados

# print (dir(dias_semana))

dias_semana= ("lunes", "martes", "miercoles","jueves", "viernes", "sabado","domingo")

# Funcion len
  
print (len(dias_semana))

print(dias_semana[0])
print(dias_semana[1])
print(dias_semana[2])
print(dias_semana[3])
print(dias_semana[4])
print(dias_semana[5])
print(dias_semana[6])

# A las tuplas podemos hacer slicing indicando el rango que queremos imprimir

print(dias_semana[:6])
print(dias_semana[0:])
print(dias_semana[-1:])
print(dias_semana[:-1])
print(dias_semana[2:5])

#Par recorrer la tupla usmor for para iterrar por los indices

for i in range (len(dias_semana)):
    print (dias_semana[i])


# Para cambiar algun valor de la tupla o añadir, debemos primero convertira a una list: 

dias_semana_lista = list(dias_semana)
print (type(dias_semana_lista))

dias_semana_lista.append("festivo") # Para agregar se usa append

print(dias_semana_lista[:8])

dias_semana_lista.pop()  # Para eliminar la ultima posicion

dias_semana= tuple(dias_semana_lista) # Para convertir nuevamente a tupla

print(type(dias_semana))
