#Ejercicio 4...

#       El usuario introducirá su nombre completo y luego este se mostrará
#       todo en minúscula, todo en mayúscula y por último solo con las 
#       primeras letras en mayúscula.

import string as st

nombre = input("\nTu nombre, por favor: ")

def tripleNombre(nom):
    nom1 = nombre.upper()
    nom2 = nombre.lower()
    nom3 = nombre.title()
    print("\n" + nom1 + "\n" + nom2 + "\n" +nom3)

tripleNombre(nombre)
