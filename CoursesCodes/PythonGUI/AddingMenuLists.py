from tkinter import *

myGui = Tk()


def hello():
	b = a.get()
	myLabel2 = Label ( text = b , fg = 'red', bg = 'yellow', font = 10).pack()

def dele():
	myLabel3 = Label ( text = 'delete' , fg = 'red', bg = 'yellow', font = 10).pack()



a = StringVar()

myGui.title("Hello")

myGui.geometry("500x500+500+100")

myLabel = Label( text ='one', fg = 'red', bg = 'yellow', font = 10).pack()

myButton = Button( text = 'enter', fg = 'blue', bg = 'green', command = hello,font = 10 ).pack() 

myButton = Button( text = 'delete', fg = 'blue', bg = 'red', command = dele,font = 10 ).pack() 


text = Entry( textvariable = a ).pack()

myMenu = Menu()

listOne = Menu()
listOne.add_command ( label = 'New File')
listOne.add_command ( label = 'OpenFile')
listOne.add_command ( label = 'Save File')

listTwo = Menu()
listTwo.add_command( label = 'Unod' )
listTwo.add_command( label = 'Redo')



#myMenu = Menu().add_cascade(label = "File") won't work
myMenu.add_cascade( label = "File", menu = listOne)
myMenu.add_cascade( label = "Edit", menu = listTwo)
myMenu.add_cascade( label = "Format")
myMenu.add_cascade( label = "Run")
myGui.config ( menu = myMenu )





myGui.mainloop()

