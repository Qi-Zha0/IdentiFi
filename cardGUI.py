from tkinter import *
import tkFileDialog
import tkMessageBox
from pprint import pprint
import json
welcomeMsg = "Welcome to IdentiFi!"
tags = ["", "", "", "", "", "", "", "", "", "", ""]
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)

def file_save():
	f = tkFileDialog.asksaveasfile(mode='w+', defaultextension=".txt")
	if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
		return
	filetosave = ""
	for tag in tags:
		filetosave = tag + " \n" + filetosave
	f.write(filetosave)
	#f.write(bkupFile)
	f.close()

def guiDisplay(dictInfo):
	#window setup
	window = Tk()
	window.geometry('800x400')
	window.title("User Profile")

	currow = 0
	for i in dictInfo:
		tags[currow] = i + " " + dictInfo[i]
		#info[currow] = dictInfo[i]
		lblA = Label(window, text=i, font=("Arial Bold", 20))
		lblB = Label(window, text=dictInfo[i], font=("Arial Bold", 20))
		lblA.grid(row=currow, column=0)
		lblB.grid(row=currow, column=1)
		currow = currow + 1
	
	menu = Menu(window)
	new_item = Menu(menu, tearoff=0)
	new_item.add_command(label='Close', command=window.destroy)
	new_item.add_command(label='Save as..', command=file_save)
	menu.add_cascade(label='File', menu=new_item)
	window.config(menu=menu)

	window.mainloop()
	#txt = Entry(window,width=10)
	#txt.grid(column=0, row=1)
	#txt.focus()

	#buttons
	#btn = Button(window, text="Click Me", bg="lightblue", fg='white', command=clicked)
	#btn.grid(column=1, row=0)
	#window.mainloop()


