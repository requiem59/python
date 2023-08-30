
alpha_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Ingresa '1' para encriptar o '2' para desencriptar.")
opt = int(input("> "))
clave = input("Numero de clave> ")

def encriptar(frase):
    mc = ""
    for letra in frase.upper():
        if letra in alpha_may:
            indice = alpha_may.find(letra)
            indice += int(clave)
            if indice >= 26:
                indice -= 26
            mc += alpha_may[indice]
        else:
            mc += letra
    return mc

def desencriptar(frase):
    mc = ""
    for letra in frase.upper():
        if letra in alpha_may:
            indice = alpha_may.find(letra)
            indice -= int(clave)
            if indice >= 26:
                indice -= 26
            mc += alpha_may[indice]
        else:
            mc += letra
    return mc

if opt == 1:
    print(encriptar(input("Ingresa una frase:\n>")))

if opt == 2:
    print(desencriptar(input("Ingresa una frase:\n>")))
