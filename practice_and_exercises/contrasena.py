#   Ejercicio 8!!!
#   Se almacenará una contraseña y lego se le preguntará al usuario por 
#   la contraseña hasta que la ingrese correctamente.

cont = "asereje"

def validacion(pswd):
    cont1 = input("Contraseña: ")
    while cont1 != cont:
        cont1 = input("Intenta de nuevo: ")
    if cont1 == cont:
        print("Bienvenido!!!\n")

validacion(cont)