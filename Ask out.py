import tkinter
from tkinter import filedialog, Text
import os
import random

# main window
root = tkinter.Tk()
root.geometry('450x450')
root.title(" ")

# initial "no" coordinates
xval = 296
yval = 330

# if they said yes
def yesyesyes():
    # red canvas
    canvas2 = tkinter.Canvas(root, height=446, width=446, bg='red')
    canvas2.place(x=0, y=0)
    
    label_widget = tkinter.Label(root, text="ASJDJSJFJJDJJFSDD\nHELL YEAH", fg="Pink", width=28, height=14, bg="Black", bd='10', font=("Arial", 20))
    label_widget.place(x=-1, y=-1)

# update randomised "no" coordinates with list
def randomando():
    randlst = [random.randint(212, 360)]
    randlst.append(random.randint(246, 394))
    button_widget2.place(x=randlst[0], y=randlst[1])

# initial white canvas
canvas = tkinter.Canvas(root, height=300, width=300)
canvas.place(x=0, y=0)

# asketh
label_widget = tkinter.Label(root, text="\nWill you go out with me", fg='black', width=26, height=7, font=("Arial", 20))
label_widget.place(x=5, y=5)

# yes button
button_widget1 = tkinter.Button(root, text="YES", width=6, height=1, bd='1', font=("Arial", 12), command=yesyesyes)
button_widget1.place(x=80, y=330)

# no button
button_widget2 = tkinter.Button(root, text="NO", width=6, height=1, bd='1', font=("Arial", 12), command=randomando)
button_widget2.place(x=xval, y=yval)

# Start the GUI loop
root.mainloop()
