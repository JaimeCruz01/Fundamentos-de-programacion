# 1er utilizar los modulos 
import modulos
modulos.borrarpantalla()
nom, ape = modulos.funcion4("Jaime", "Cruz")
print(f"Hola, yo soy {nom} {ape}")

#2da formar de utilizar modulos
from modulos import funcion1, funcion2, funcion3, funcion4, borrarpantalla
modulos.borrarpantalla()
nom, ape = modulos.funcion4("Jaime", "Cruz")
print(f"Hola, yo soy {nom} {ape}")
