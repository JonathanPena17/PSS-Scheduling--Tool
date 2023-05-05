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

        #filemenu creation
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


#create time picker
hour_string=StringVar()
min_string=StringVar()
last_value_sec = ""
last_value = ""        
f = ('Times', 20)

def display_msg():
    #date = cal.get_date()
    m = min_sb.get()
    h = sec_hour.get()
    s = sec.get()
    #t = f"Your appointment is booked for {date} at {m}:{h}:{s}."
    msg_display.config(text=t)


if last_value == "59" and min_string.get() == "0":
    hour_string.set(int(hour_string.get())+1 if hour_string.get() !="23" else 0)   
    last_value = min_string.get()

if last_value_sec == "59" and sec_hour.get() == "0":
    min_string.set(int(min_string.get())+1 if min_string.get() !="59" else 0)
if last_value == "59":
    hour_string.set(int(hour_string.get())+1 if hour_string.get() !="23" else 0)            
    last_value_sec = sec_hour.get()

fone = Frame(root)
ftwo = Frame(root)

fone.pack(pady=10)
ftwo.pack(pady=10)

min_sb = Spinbox(
    ftwo,
    from_=0,
    to=23,
    wrap=True,
    textvariable=hour_string,
    width=2,
    state="readonly",
    font=f,
    justify=CENTER
    )
sec_hour = Spinbox(
    ftwo,
    from_=0,
    to=59,
    wrap=True,
    textvariable=min_string,
    font=f,
    width=2,
    justify=CENTER
    )


sec = Spinbox(
    ftwo,
    from_=0,
    to=59,
    wrap=True,
    textvariable=sec_hour,
    width=2,
    font=f,
    justify=CENTER
    )

min_sb.pack(side=LEFT, fill=X, expand=True)
sec_hour.pack(side=LEFT, fill=X, expand=True)
sec.pack(side=LEFT, fill=X, expand=True)

msg = Label(
    root, 
    text="Hour  Minute  Seconds",
    font=("Helvetica", 12),
    bg="#F79AC0"
    )
msg.pack(side=TOP)

actionBtn =Button(
    root,
    text="Create Event",
    padx=10,
    pady=10,
    command=display_msg
)
actionBtn.pack(pady=10)

msg_display = Label(
    root,
    text="Birthday party",
    bg="#F79AC0"
)
msg_display.pack(pady=10)



turn_on = Button(root, text="select time")
turn_on.pack()
        

app = Window(root)
root.geometry("300x300")
root.wm_title("Personal Schedule")
root.mainloop()


