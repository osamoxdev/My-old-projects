from tkinter import *

root = Tk()

root.title("calculator")

inputs = Entry(root, width=35, borderwidth=5)

inputs.grid(row=0,column=0,columnspan=3, padx=10, pady=10)
# columnspan 3 ,to make the column fits the 3 buttons
def Buttons(number):

    revars = inputs.get()
    inputs.delete(0, END)
    inputs.insert(0, str(revars) + str(number))

def Clear():

    inputs.delete(0, END)

def add():

    firstNumber= inputs.get()

 
    global num1 # to use this varibal on anothor def
    global math
    math = 'add'
    num1 = int(firstNumber)
    inputs.delete(0, END)#delete numberr when you click

def Equal() :

    secondNumber = inputs.get()
    inputs.delete(0, END)
    if math == 'add' :

        inputs.insert(0, num1 + int(secondNumber))

    elif math == 'sub' :

        inputs.insert(0, num1 - int(secondNumber))

    elif math == 'mult' :

        inputs.insert(0, num1 * int(secondNumber))

    elif math == 'divi' :

        inputs.insert(0, float(num1) / float(secondNumber))




def subtract():

    firstNumber= inputs.get()
    global num1
    num1 = int(firstNumber)
    global math
    math = 'sub'
    inputs.delete(0, END)

def multiply():

    firstNumber= inputs.get()

    global num1
    num1 = int(firstNumber)
    global math
    math = 'mult'
    inputs.delete(0, END)

def divide():

    firstNumber= inputs.get()

    global num1
    num1 = int(firstNumber)
    global math
    math = 'divi'
    inputs.delete(0, END)


button1 = Button(root, text= "1", padx= 45, pady=20,command=lambda: Buttons(1))
button2 = Button(root, text= "2", padx= 45, pady=20,command=lambda: Buttons(2))
button3 = Button(root, text= "3", padx= 45, pady=20,command=lambda: Buttons(3))

button4 = Button(root, text= "4", padx= 45, pady=20,command=lambda: Buttons(4))
button5 = Button(root, text= "5", padx= 45, pady=20,command=lambda: Buttons(5))
button6 = Button(root, text= "6", padx= 45, pady=20,command=lambda: Buttons(6))

button7 = Button(root, text= "7", padx= 45, pady=20,command=lambda: Buttons(7))
button8 = Button(root, text= "8", padx= 45, pady=20,command=lambda: Buttons(8))
button9 = Button(root, text= "9", padx= 45, pady=20,command=lambda: Buttons(9))

button0 = Button(root, text= "0", padx= 45, pady=20,command=lambda: Buttons(0))
buttonClear = Button(root, text = "Clear", bg="yellow", fg="black",
padx= 90, pady= 20 , command=Clear)

button_plus = Button(root, text= '+', padx= 43, pady=20,command=add)
button_sub = Button(root, text= '_', padx= 45, pady=20,command=subtract)
button_mult = Button(root, text= 'X', padx= 45, pady=20,command=multiply)
button_divy = Button(root, text= '÷', padx= 45, pady=20,command=divide)
button_equal = Button(root, text= '=',bg="green",fg=
"white", padx= 100, pady=20,command=Equal)


button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button0.grid(row=4, column=0)
buttonClear.grid(row=4, column= 1, columnspan=2)

button_plus.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_mult.grid(row=6, column=1)
button_divy.grid(row=6, column=2)

root.mainloop()