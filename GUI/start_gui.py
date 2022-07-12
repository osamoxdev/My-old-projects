from tkinter import *
# import tkinter as tk

root = Tk()

myLabel = Label(root, text="Hellow World!").grid(row=0, column=0)
myLabel2 = Label(root, text="let's get start it ").grid(row=1, column=1)

# row عمود
# column صف
button1 = Button(root, text='start').grid(row=2, column=2)

button2 = Button(root, text='Don\'t start', state=DISABLED).grid(row=2 , column=0)

button3 = Button(root, text='square', padx=20, pady=20).grid(row=3, column=1)
# myLabel.grid(row=0, column=0)
# myLabel2.grid(row=0, column=1)

root.mainloop()
