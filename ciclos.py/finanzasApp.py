# La aplicacion de permitir registrar ingresos y contal el saldo de estos, si el egreso es mayo de que el saldo, no debe permitir el retiro y mostrara un mensaje de saldo insuficiente.
# La aplicacion llevara registro de los movimientos indicando el numero de ingresos y egresos. 

saldo=0
acumIngreso = 0
acumuEgreso = 0

isOn= int(input("Ingrese 1 para inicializar el servicio: "))

while isOn !=0:

    opc= int(input("1. Ingreso:\n 2. Egreso\n 3- Salir"))

    if opc==1:
        ingreso= int(input("Registre el ingreso"))

        saldo= saldo+ingreso

        print(f"Su Saldo es {saldo}")
      #forma 2 de concatenar  print("Saldo es: " + saldo)
      #forma 3 de concatenarprint("saldo es:", saldo)
        acumIngreso +=1
        print(acumIngreso)
    
    elif opc==2:
        egreso= int(input("Registre el monto a retirar:"))   

        saldo= saldo-egreso

        if saldo <0:
            print("Saldo insuficiente") 
            saldo= saldo+egreso
            print(saldo)
            

        else:
            print(f"Su saldo es: $ {saldo}")
            acumuEgreso +=1
            print(acumuEgreso)   

    elif opc==3:
        print ("salir")  
        isOn=0
    else:
        print("Ingrese una opcion valida")    


        





