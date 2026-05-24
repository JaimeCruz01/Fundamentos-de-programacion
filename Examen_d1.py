def venta():
    opc = "si"
    total = 0
    cont = 0
    while opc == "si":    
        cont += 1
        marca=input("Ingresa la marca del carro: ").lower()
        origen=input("Ingresa el origen del carro: ").lower()
        costo=(float)(input("Ingresa el costo del carro: "))
        impuesto=0
        if origen=="alemania":
            impuesto=0.3
        elif origen=="japon":
            impuesto=0.20
        elif origen=="italia":
            impuesto=0.15
        elif origen=="usa":
            impuesto=0.08

        impuesto_pesos=costo*impuesto
        pv=impuesto_pesos+costo

        print(f"El impuesto pagar es: $ {impuesto_pesos}")
        print(f"El precio de venta es: ${pv}")
        opc = ""
        total += pv
        while opc != "si" and opc != "no":
            opc = input("¿Quieres ingresar un nuevo valor? (si/no) " ).lower()
    return cont, total 
    
cont, total = venta()


print("Numero de veces que se realizo el proceso: ",cont)
print("Total de la suma de los resultados capturados: ",total)
