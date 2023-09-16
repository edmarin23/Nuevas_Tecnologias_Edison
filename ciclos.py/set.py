# Los conjuntos son inmutables 
# Son desordenados ya quiere decir que cuando se llama, no se tiene certeza de el orden en que se mostrara
# Nos son indexados 
# No permite duplicados

vocales = {"a","e","i","o","u"}

print(len(vocales))

print(type(vocales))

#Para recorrer los conjuntos se usa in 

for i in vocales:
    print(vocales)
print("------------------")   
    
for i in vocales:
    print(vocales)
print("------------------")
    
    
for i in vocales:
    print(vocales)

print("------------------")

# Los diccionarios tienen el metodo add y remove, lo que quiere decir que no son 100% inmutables

vocales.add("@")
for i in vocales:
    print(vocales)

print (vocales)

# Podemos remover

vocales.remove("@")
for i in vocales:
    print(vocales)
    
# con pop se eliminar cualquier elemento al asar    
    vocales.pop()
