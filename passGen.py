"""
    Password Generator with GUI using Tkinter library
    Created by requiem59 (Christian Alexis Mejia Mondragón)

"""

import random
import tkinter as tk
from tkinter.messagebox import showerror, showwarning

#Character groups
ab = "abcdefghijklmnopqrstuvwxyz"
AB = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!#$%&*+-.<=>?@_"

#Password generator function
def generator():
    #Clearing the password field
    password.delete(0,'end')
    
    included = ""
    passwd = ""
    #Receiving password length
    try:
        l = int(lIn.get())    
        #Warning message to avoid hinder the program
        if(l > 300):
            tk.messagebox.showwarning(title="Warning", message="Big values could overload the program.")
        #Validating the checkButtons values and adding the selected characters to the included string
        if(lower.get()):
            included += ab
        if(upper.get()):
            included += AB
        if(numb.get()):
            included += numbers
        if(symb.get()):
            included += symbols
        for i in range(l):
            passwd = passwd + random.choice(included)
        password.insert(0, passwd)
    #Throw an error mesagebox if the length value is not an integer or none checkButton is selected
    except:
        tk.messagebox.showerror(title="Error", message="Invalid length value or no boxes selected.")
    
#Creating main window
window = tk.Tk()
window.geometry("525x240")
window.title("Safe Password Generator")
window.config(bg = "#787484")

#Creating length input and label
lab1 = tk.Label(window, text="Password length", font="arial 11", bg="#787484")
lab1.grid(row = 0, column = 0, pady = 12, columnspan = 2)

lIn = tk.Entry(window, font="arial 11")
lIn.grid(row = 0, column = 2, columnspan = 2)

#Declaring checkButton variables as booleans
lower = tk.BooleanVar() 
upper = tk.BooleanVar() 
numb = tk.BooleanVar() 
symb = tk.BooleanVar() 

#Setting them to false as default
lower.set(False)
upper.set(False)
numb.set(False)
symb.set(False)

#Creating the checkButtons for indicate which characters will be included in the password
radMin = tk.Checkbutton(window, text="Lowercase", variable = lower, font="arial 11", bg="#787484")
radMin.grid(row = 1, column = 0, padx = 10, pady = 12)

radMay = tk.Checkbutton(window, text="Uppercase", variable = upper, font="arial 11", bg="#787484")
radMay.grid(row = 1, column = 1, padx = 20)

radNum = tk.Checkbutton(window, text="Numbers", variable = numb, font="arial 11", bg="#787484")
radNum.grid(row = 1, column = 2, padx = 20)

radSym = tk.Checkbutton(window, text="Symbols", variable = symb, font="arial 11", bg="#787484")
radSym.grid(row = 1, column = 3, padx = 20)

#A space for aesthetic purposes
space = tk.Label(window, bg = "#787484")
space.grid(row = 4, column = 0, columnspan=4)

#Button for calling the password generator function
genButton = tk.Button(window, text = "Generate", command = generator, font = "arial 11")
genButton.grid(row =2, column = 1, columnspan = 2, rowspan = 2, padx = 80)

#Creating label to display the password
password = tk.Entry(window, font = "arial 11", width = 45)
password.grid(row = 5, column = 0, columnspan = 4)

window.mainloop()
