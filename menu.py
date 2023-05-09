import calendar
import tkinter as tk
from tkinter import *



# menu window for creating a new appointment


#picker data for time
class TimePicker(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.oneDay_string = StringVar()
        self.twoDay_string = StringVar()
        self.hour_string = StringVar()
        self.min_string = StringVar()
        self.last_value_sec = ""
        self.last_value = ""
        self.f = ('Helvetica', 20)

        self.create_widgets()

    def create_widgets(self):
        fone = Frame(self)
        ftwo = Frame(self)
        fthree = Frame(self)
        fone.pack(pady=10)
        ftwo.pack(pady=10)
        fthree.pack(pady=20)

        self.min_sb = Spinbox(
            ftwo,
            from_=0,
            to=23,
            wrap=True,
            textvariable=self.hour_string,
            width=2,
            state="readonly",
            font=self.f,
            justify=CENTER
        )
        self.sec_hour = Spinbox(
            ftwo,
            from_=0,
            to=59,
            wrap=True,
            textvariable=self.min_string,
            font=self.f,
            width=2,
            justify=CENTER
        )

        self.sec = Spinbox(
            ftwo,
            from_=0,
            to=59,
            wrap=True,
            textvariable=self.sec_hour,
            width=2,
            font=self.f,
            justify=CENTER
        )

        self.sec_day = Spinbox(
            ftwo,
            from_=0,
            to=3,
            wrap=True,
            textvariable=self.twoDay_string,
            font=self.f,
            width=2,
            justify=CENTER
        )

        self.day = Spinbox(
            ftwo,
            from_=0,
            to=9,
            wrap=True,
            textvariable=self.oneDay_string,
            width=2,
            font=self.f,
            justify=CENTER
        )

        self.sec_day.pack(side=LEFT, fill=X, expand=True)
        self.day.pack(side=LEFT, fill=X, expand=True)
        self.min_sb.pack(side=LEFT, fill=X, expand=True)
        self.sec_hour.pack(side=LEFT, fill=X, expand=True)
        self.sec.pack(side=LEFT, fill=X, expand=True)

        self.msg = Label(
            self,
            text="Hour  Minute  Seconds",
            font=("Helvetica", 12),
            bg="#F79AC0"
        )
        self.msg.pack(side=TOP)

        self.actionBtn = Button(
            self,
            text="Create Event",
            padx=10,
            pady=10,
            command=self.display_msg
        )
        self.actionBtn.pack(pady=10)

        self.msg_display = Label(
            self,
            text="",
            bg="#F79AC0"
        )
        self.msg_display.pack(pady=10)

    def display_msg(self):
        dayone = self.day.get()
        daytwo = self.sec_day.get()
        m = self.min_sb.get()
        h = self.sec_hour.get()
        s = self.sec.get()
        t = f"Your appointment is booked for the {daytwo}{dayone}   {m}:{h}:{s}."
        self.msg_display.config(text=t)


#logic to restrict time selection
        if self.last_value == "59" and self.min_string.get() == "0":
            self.hour_string.set(int(self.hour_string.get())+1 if self.hour_string.get() !="23" else 0)   
            self.last_value = self.min_string.get()

        if self.last_value_sec == "59" and self.sec_hour.get() == "0":
            self.min_string.set(int(self.min_string.get())+1 if self.min_string.get() !="59" else 0)
        if self.last_value == "59":
            self.hour_string.set(int(self.hour_string.get())+1 if self.hour_string.get() !="23" else 0)            
            self.last_value_sec = self.sec_hour.get()

