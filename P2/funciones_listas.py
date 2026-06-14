"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""


#Funciones más comunes en las listas
paises = ["Mexico","Canada", "EUA", "Mexico","Mexico", "Brasil"]

numeros =[23,45,8,24,100,100,23]
varios =[33,3.1416, True]
vacio = []
#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacio)
#Recorrer la lista 
#1er forma 
for i in paises:
    print(i)
    
# #2do forma 
for i in range(0,len(paises)):
    print(paises[i])

#ordenar elementos de una lista
print(paises)
paises.sort()
print(paises)
#dar la vuelta a una lista
paises.reverse()
print(paises)



#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises.append("Alemania")

#2da forma
paises.insert(1, "Hola")
print(paises)

#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises.pop(2)
print(paises)


#2da forma 
paises.remove("EUA")
print(paises)

#Buscar un elemento dentro de la lista
encontro = "EUA" in paises
print(encontro)
#Contar el numeros de veces que aparece un elemento dentro de una lista
num_veces= numeros.count(23)
print(num_veces)
num_paises = paises.count("Mexico")
print(num_paises)
#Conocer la posicion o indice en el que se encuentra un elemento de la lista
posicion = paises.index("Mexico")
print(posicion)
encontrados = []
for i in range(0, len(paises)):
    if(paises[i]=="Mexico"):
        encontrados.append(i)
    
print(encontrados)    
#Unir el contenido de una lista dentro de otra lista
numeros1 = [231,123,34,123,312,124,123]
numeros2 = [145,345]
print(numeros2)
numeros1.extend(numeros2)
print(numeros1)
#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente
numeros1.sort()
numeros1.reverse()
print(numeros1)


