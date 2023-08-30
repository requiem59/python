# Ejercicio 9!!!
#   En éste programa se mostrara todo lo que el usuario 
#   introduzca hasta que ingrese la palabra salir.

salir = "salir"

while True:
    texto = input("")
    print(texto)

    if texto == salir:
        print("¡Adios!")
        break