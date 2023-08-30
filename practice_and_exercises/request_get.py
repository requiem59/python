import requests
import argparse

parser = argparse.ArgumentParser(description = "Detector de comandos")  #Aqui se crea el detector de comandos
parser.add_argument('-t', '--target', help = "Valor")                   #Aqui le damos los argumentos
parser = parser.parse_args()

if parser.target:
    try:
        url = requests.get(url = parser.target)         #Aqui toma la url dada en el parser
        heads = dict(url.headers)                  # Con esta función se obtienen las cabeceras de la url 
        for i in heads:                            # y se mandan a un diccionario
            print(i + " : " + heads[i])
    except:
        print("Error de conexión.")
else:
    print("No hay argumento.")
    
#Ahora otro ejemplo de get: En este caso se obtendrá un archivo por medio de la url del mismo.
    
r = requests.get('https://imagenes.20minutos.es/files/og_thumbnail/uploads/imagenes/2019/01/19/866781.jpg') #Primero se obtiene el archivo

with open('perrito.jpg', 'wb') as df       #Luego se crea el archivo perrit.png y se le manda el contenido del get
    df.write(r.content)