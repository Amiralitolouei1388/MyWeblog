from tkinter import *
from time import *


root = Tk()
root.title("Digital Clock")
root.config(bg='black')
root.resizable(False,False)

def MyTime():
	times = strftime("%I:%M:%S  %p")
	lab.config(text = times)
	lab.after(1000, MyTime)

lab = Label(root, font=('Arial',50), bg='black', fg='aqua')
lab.pack()

MyTime()

root.mainloop()