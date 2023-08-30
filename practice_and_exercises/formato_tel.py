# Ejercicio 6...
#   El objetivo es que el programa pregunte por un numero 
#   con formato prefijo-número-extension y luego muestre el número 
#   sin prefijo ni extensión.

num = input("\nIngresa tu número con formato prefijo-número-extension ejemplo: +34-913724710-56:\n \n ->>> ")

def mostrarNum(tel):
    num2 = num[4:13]
    print(num2)

mostrarNum(num)