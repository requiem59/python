#   Ejercicio 7
#   Para este ejercicio el usuario introducirá un número y luego se 
#   mostrará en pantalla un triángulo con una altura del número introducido.

n = int(input("Intriduce un número: "))

def triangulo(num):
    if n > 0:
        for i in range(n):
            p = "*" + str(i*"*")
            print(p)
    else:
        print("Debe ser un entero positivo.")

triangulo(n)