from tkinter import *  

from time import strftime


root = Tk()

root.title('Clock')



def clock():
    time = strftime('%H:%M:%S %p')
    lable.config(text=time)
    lable.after(100, clock)

lable = Label(root, font=('Courier', 80), background='black', foreground='cyan')

lable.pack(anchor='center')


clock()

mainloop()

