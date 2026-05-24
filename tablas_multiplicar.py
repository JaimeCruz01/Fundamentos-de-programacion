'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''
num = int(input("Ingresa un numero: "))

print(f"1 * {num} = {num*1}")
print(f"2 * {num} = {num*2}")
print(f"3 * {num} = {num*3}")
print(f"4 * {num} = {num*4}")
print(f"5 * {num} = {num*5}")
print(f"6 * {num} = {num*6}")
print(f"7 * {num} = {num*7}")
print(f"8 * {num} = {num*8}")
print(f"9 * {num} = {num*9}")
print(f"10 * {num} = {num*10}")

for i in range(0,10):
    print(f"{i+1} * {num} = {(i+1)*num}")

i = 0
while i < 10: 
    i += 1
    print(f"{i} * {num} = {(i)*num}")
    
def tabla(numero):
    num = numero
    tabla = f"""1 * {num} = {num*1}
2 * {num} = {num*2}
3 * {num} = {num*3}
4 * {num} = {num*4}
5 * {num} = {num*5}
6 * {num} = {num*6}
7 * {num} = {num*7}
8 * {num} = {num*8}
9 * {num} = {num*9}
10 * {num} = {num*10}"""
    return tabla

mensaje = tabla(num)
print(mensaje)

def tabla(num_tab,n):
    mul=num_tab*n
    print(f"{num_tab} x {n}  = {mul} ")
    n+=1
    return n
  
num_tabla=int(input("Dame un numero para obtener la tabla de multiplicar:  "))

for num in range(1,11):
  num=tabla(num_tabla,num)