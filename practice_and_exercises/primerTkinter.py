import tkinter

ventana = tkinter.Tk() #Se crea la ventana.
ventana.geometry("400x500") #Se define el tamaño de la ventana.

texto = tkinter.Label(ventana, text = "Gastritis", bg = "red") #En esta función debe especificar donde irá la etiqueta y lo que va                                                                 a decir

texto.pack(fill = tkinter.X) #Es necesario para que se muestre el texto, por defecto lo acomoda centrado en la parte superior.

def tanganana():
    print("Tangananica!!!")

def tangananica():
    print("Tanganana!!!")
    
def leerText():
    lt = textIn.get()
    print(lt)

boton1 = tkinter.Button(ventana, text = "Tangananica", padx = 50, pady = 30, command = tangananica)
boton2 = tkinter.Button(ventana, text = "Tanganana", padx = 50, pady = 30, command = tanganana)
boton3 = tkinter.Button(ventana, text = "Leer", command = leerText)
boton1.pack(side = tkinter.RIGHT)
boton2.pack(side = tkinter.LEFT)
boton3.pack()

textIn = tkinter.Entry(ventana, width=8, show = "*") #width es para el numero de caracteres admitidos, no para el tamaño
textIn.pack()

textIn2 = tkinter.Entry(ventana, width=4, font = "Calibri 14")
textIn2.pack()

ventana.mainloop() #Esta función se encarga de registrar todos los eventos de la ventana.
