import tkinter

ventana = tkinter.Tk()
ventana.geometry("370x200")
ventana.config(bg = "#EE124E")

titulo = tkinter.Label(ventana, text = "Calculador de semanas.", font = "calibri 11", bg = "#EE124E")
titulo.grid(row = 0, column = 1)

lab1 = tkinter.Label(ventana, text = "     Años: ", font = "calibri 11", bg = "#EE124E")
lab1.grid(row = 2, column = 0)

ansIn = tkinter.Entry(ventana, font = "calibri 11", text = "Volumen")
ansIn.grid(padx = 2, row = 2, column = 2)

lab2 = tkinter.Label(ventana, text = "     Meses: ", font = "calibri 11", bg = "#EE124E")
lab2.grid(row = 3, column = 0)

mesIn = tkinter.Entry(ventana, font = "calibri 11")
mesIn.grid(padx = 2, row = 3, column = 2)

lab3 = tkinter.Label(ventana, text = "     Dias: ", font = "calibri 11", bg = "#EE124E")
lab3.grid(row = 4, column = 0)

diasIn = tkinter.Entry(ventana, font = "calibri 11")
diasIn.grid(padx = 2, row = 4, column = 2)

resultado = tkinter.Label(ventana, bg = "#EE124E", font = "calibri 12")
resultado.grid(row = 7, column = 1)

def calcular():
    a = int(ansIn.get())
    m = int(mesIn.get())
    d = int(diasIn.get())
    
    semA = a * 52
    semM = m * 4
    semD = int(d / 7)
    
    semT = semA + semM + semD
    
    resultado["text"] = "{0} semanas.".format(semT)

boton = tkinter.Button(ventana, text = "Calcular", font = "calibri 11", command = calcular)
boton.grid(row = 6, column = 1)

ventana.mainloop()