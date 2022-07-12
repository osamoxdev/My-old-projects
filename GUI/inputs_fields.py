from tkinter import * 

root = Tk()

enter = Entry(root, width=25, fg="green", bg="black")

enter.pack()
enter.insert(0, 'your plan here')

def click():

  lable = Label(root, text='-'+enter.get())
  lable.pack()
  


butten = Button(root,text='Enter your plan', command=click, 
fg="red", bg="black")
#fg for text bg for the backround of button

butten.pack()


root.geometry("600x400")
root.mainloop()

