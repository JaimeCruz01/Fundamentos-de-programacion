print("\033c")
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros = [23,33,45,8,24,0,100]
print(numeros)
lista2 = "["
lista3 = "["
cont = 0
for i in range(0, len(numeros)):
    if(cont+1 == len(numeros)):
        lista2 += (f" {numeros[i]}]")
    elif cont != 0:
        lista2 += (f" {numeros[i]},")
    else:
        lista2 += (f"{numeros[i]},")
    cont+=1
print(lista2)

cont2=0
lista3 = "["
while cont2 != len(numeros):
    if(cont2+1 == len(numeros)):
        lista3 += (f" {numeros[cont2]}]")
    elif cont2 != 0:
        lista3 += (f" {numeros[cont2]},")
    else:
        lista3 += (f"{numeros[cont2]},")
    cont2+=1
print(lista3)

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
#1er forma
palabras = ["UTD","Tercer","Cuatrimestre","TI"]
palabra = input("Dame la palabra a buscar: ").strip()

if palabra in palabras:
    print(f"Encontre la palabra {palabra}")
else:
    print(f"No se encontro {palabra}")

#2DA FORMA
buscado = True
for i in range(0,len(palabras)):
    if palabra == palabras[i]:
        print(f"Encontre la palabra {palabra}")
        buscado = False
if buscado:
    print(f"No se encontro {palabra}")

mensaje = (f"No se encontro {palabra}")
for i in range(0,len(palabras)):
    if palabra == palabras[i]:
        mensaje = (f"Encontre la palabra {palabra}")
print(mensaje)

cont = 0
mensaje2 = (f"No se encontro {palabra}")
while cont != len(palabras):
    if palabra == palabras[i]:
        mensaje2 = (f"Encontre la palabra {palabra}")
    cont += 1
print(mensaje2)
#3er FORMA

#Ejemplo 3 Añadir elementos a la lista

#opcion 1
lista = []
true = True
while true:
    valor = input("Dame un valor: ").strip()
    lista.append(valor)
    true = input("¿Quieres ingresar otro valor? (true/false) ").strip() == "True"

# opcion 2
lista = []
opc = "si"
while opc == "si":
    valor = input("Dame un valor: ").strip()
    lista.append(valor)
    opc = input("¿Quieres ingresar otro valor? (si/no) ").strip() 
    
    
#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda


agenda= [
    ["6183670857","Jaime"],
    ["6181880185","Ana"],
    ["6182904476","Omar"]
]

for i in agenda:
    print(i)

mensaje = ""
for i in range(0,len(agenda)):
    mensaje += "["    
    for j in range(0,len(agenda[i])):
        mensaje += (f"{" " if j != 0 else ""}'{agenda[i][j]}'{"]" if j == (len(agenda[i])-1) else ","}")
    mensaje += "\n"

print(mensaje)
