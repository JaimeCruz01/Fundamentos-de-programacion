"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
print("\033c")

paises = ("Mexico","Canada","EUA")
varios = ("Hola",123,False,1.23)

print(paises)

for i in paises:
    print(i)

for i in range(0,len(paises)):
    print(paises[0])

cont = 0
while cont < len(paises):
    print(paises[cont])
    cont += 1


print(f"El pais inagural de la copa del mundo es: {paises[0]}")

edades=(23,23,24,19,18,17,18,19,18,19,18,19,19,19,22)
print(edades.count(18))

print(edades)
num = int(input("Ingresa un numero: "))
cont2 = 0
posiciones = []
for i in range(0,len(edades)):
  
    if(num == edades[i]):
        cont2 +=1
        posiciones.append(i)
        print(f"Posicion {cont2}: {i}")
if (cont2 == 0):
    print("No se encontro el numero")
posiciones_tuple = tuple(posiciones)
print(posiciones_tuple)