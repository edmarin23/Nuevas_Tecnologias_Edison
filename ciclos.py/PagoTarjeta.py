valorcompra = float(input("Ingrese el valor de compra: "))
numcuotas = int(input("Ingrese numero de cuotas: "))

valorcuota = valorcompra / numcuotas

cuota_actual = 1
saldo_restante = valorcompra

while cuota_actual <= numcuotas:
    if cuota_actual == 1:
        saldo_restante -= valorcuota  # Descuento del valor completo en la primera cuota
    else:
        saldo_restante -= valorcuota  # Descuento solo el valor de la cuota en cuotas posteriores
    
    print(f"Cuota {cuota_actual}: Valor de cuota = {valorcuota:.2f} | Saldo restante = {saldo_restante:.2f}")
    
    cuota_actual += 1

