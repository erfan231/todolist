from tkinter import *


window = Tk() #create the window
menu = Menu(window) # making a menu
window.config(menu = menu) #creates a Master menu for the window

filemenu = Menu(menu)# creating a sub menu
menu.add_cascade(label = "File", menu = filemenu) #adding the filemenu inside the menu*(master)
filemenu.add_command(label = "ok") #creating a menu inside "filemenu"
window.title("ToDoList") #screens title
content = Listbox(window, font = "Ariel 12 bold") #the space where the todo gets added to
task = StringVar() #type of data
entry = Entry(window, textvariable = task, font = "Arial 24") #making an box to take inputs
#adding buttons and the commands
addbtn = Button(window, text = "Add", font = "Ariel 18",
                command = lambda content= content, task = task : content.insert(END,task.get()))

deletebtn = Button(window, text = "Delete" , font = "Ariel 14",
                   command = lambda content = content: content.delete(ANCHOR))
text = Label(window, text = "Enter", font = "Ariel 14", bd = 2)
text.grid(row = 1, column = 0)

content.grid(row = 0 , column = 1, columnspan = 2) #placing the todo placeholder on the screen
entry.grid(row= 1 , column = 1, columnspan = 2) #placing the input box
addbtn.grid(row = 2, column = 0) #placing the button
deletebtn.grid(row= 2, column = 1)


window.mainloop()
