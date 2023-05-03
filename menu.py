import calender
import tkinter as tk
from tkinter import *
from tktimepicker import AnalogPicker, AnalogThemes
from tkcalendar import *

root = Tk()

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

        

    def exitProgram(self):
        exit()


turn_on = Button(root, text="select time")
turn_on.pack()
        

app = Window(root)
root.geometry("300x300")
root.wm_title("Personal Schedule")
root.mainloop()


