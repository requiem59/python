import tkinter

ventana = tkinter.Tk()
ventana.geometry("360x300")
ventana.config(bg = "#967BFA")
ventana.title("Calculadora de dosis")

titulo = tkinter.Label(ventana, text = "Convertidor de dosis dada en mg a ml.", font = "verdana 10", bg = "#967BFA")
titulo.grid(row = 0, column = 0, pady=8, columnspan=3)

lab1 = tkinter.Label(ventana, text = "  Volumen en ml: ", font = "verdana 10", bg = "#967BFA")
lab1.grid(row = 2, column = 0, sticky=tkinter.W)

volIn = tkinter.Entry(ventana)
volIn.grid(row = 2, column = 2, pady=5) 

lab2 = tkinter.Label(ventana, text = "  Dosis en mg: ", font = "verdana 10", bg = "#967BFA")
lab2.grid(row = 3, column = 0, sticky=tkinter.W)

dosIn = tkinter.Entry(ventana)
dosIn.grid(row = 3, column = 2, pady=5)

lab3 = tkinter.Label(ventana, text = "  Presentación en mg: ", font = "verdana 10", bg = "#967BFA")
lab3.grid(row = 4, column = 0)

presIn = tkinter.Entry(ventana)
presIn.grid(row = 4, column = 2, pady=5)

resultado = tkinter.Label(ventana, bg = "#967BFA", font = "verdana 10")
resultado.grid(row = 8, column = 0, columnspan=3)

espacio = tkinter.Label(ventana, bg = "#967BFA")
espacio.grid(row = 5, column = 0, columnspan=3)

espacio = tkinter.Label(ventana, bg = "#967BFA")
espacio.grid(row = 7, column = 0, columnspan=3)

def calcular():
    va = volIn.get()
    da = dosIn.get()
    pa = presIn.get()
    
    if va=="" or da=="" or pa =="":
        resultado["text"] = "No deje casillas vacias, tampoco ingrese letras."
    else:
        v = float(va)
        d = float(da)
        p = float(pa)

        dosMg = v * d / p
        dosMg = round(dosMg, 3)

        resultado["text"] = "La dosis a administrar es: {0} ml.".format(dosMg)

boton = tkinter.Button(ventana, text = "Calcular", font = "verdana 10", command = calcular)
boton.grid(row = 6, column = 1)

ventana.mainloop()