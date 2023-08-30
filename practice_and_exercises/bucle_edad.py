# Ejercicio 5!!!
#   Para éste programa el usuario solo dará su edad y luego se mostrarán 
#   en pantalla todos los años cumplidos hasta el momento.

edad = input("\n¿Cuál es tu edad? -> ")

def añosCumplidos(años):
    for i in range(1, int(edad) + 1):
        print(i)

añosCumplidos(edad)