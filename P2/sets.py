"""
Sets.-
    Es un tipo de datos para tener una colección de valores pero no tiene ni índice ni orden

    Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""

print("\033c")

coleccion_datos = {"hola", "123", 123, "mexico", "Holanda"}

coleccion_datos.add("ganador")
print(coleccion_datos)

coleccion_datos.pop()
print(coleccion_datos)

# Ejemplo:
# Crear un programa que solicite los email de los alumnos de la UTD,
# almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados.

# Solución 1

lista_correos = []

total_correos = int(input("¿Cuántos correos desea ingresar?: "))

for indice in range(total_correos):
    correo_usuario = input(f"Ingrese el correo {indice+1}: ")
    lista_correos.append(correo_usuario)

print("\nLista original:")
print(lista_correos)

correos_unicos = list(set(lista_correos))

print("\nLista sin duplicados:")
print(correos_unicos)

# Solución 2

registro_correos = []

cantidad_registros = int(input("\n¿Cuántos correos desea ingresar?: "))

for posicion in range(cantidad_registros):
    email = input(f"Ingrese el correo {posicion+1}: ")
    registro_correos.append(email)

lista_unica = []

for email in registro_correos:
    if email not in lista_unica:
        lista_unica.append(email)

print("\nLista original:")
print(registro_correos)

print("\nLista sin duplicados:")
print(lista_unica)





