import calendar
import tkinter as tk
from menu import *


class CalendarUI(tk.Frame):
    def __init__(self, master=None, year=None, month=None):
        super().__init__(master)
        self.master = master
        self.year = year if year else calendar.datetime.date.today().year
        self.month = month if month else calendar.datetime.date.today().month
        self.current_date = calendar.datetime.date.today()
        self.create_widgets()

    def create_widgets(self):
        self.current_month_label = tk.Label(self, text=calendar.month_name[self.month] + " " + str(self.year))
        self.current_month_label.grid(row=0, column=0, columnspan=7)

        self.weekday_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, weekday in enumerate(self.weekday_labels):
            label = tk.Label(self, text=weekday)
            label.grid(row=1, column=i)

        self.days_buttons = []
        self.update_days_buttons()

        prev_button = tk.Button(self, text="<", command=self.go_to_previous_month)
        prev_button.grid(row=0, column=1, sticky="w")

        next_button = tk.Button(self, text=">", command=self.go_to_next_month)
        next_button.grid(row=0, column=5, sticky="e")


    def update_days_buttons(self):
        for button in self.days_buttons:
            button.grid_forget()
        self.days_buttons.clear()

        month_calendar = calendar.monthcalendar(self.year, self.month)

        for row, week in enumerate(month_calendar):
            for col, day in enumerate(week):
                if day == 0:
                    continue
                button = tk.Button(self, text=str(day), command = self.create)
                button.grid(row=row+2, column=col)
                self.days_buttons.append(button)
                if button == self.current_date:
                    button.configure(bg="yellow") # highlight the current day
        

        create_task = tk.Button(self, text="Create", command = self.create)
        create_task.grid(row = 11 , column=1)

        select_task = tk.Button(self, text="Select", command = self.create)
        select_task.grid(row = 11 , column = 3)
                
        

    def go_to_previous_month(self):
        if self.month == 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1
        self.current_month_label.config(text=calendar.month_name[self.month] + " " + str(self.year))
        self.update_days_buttons()

    def go_to_next_month(self):
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1
        self.current_month_label.config(text=calendar.month_name[self.month] + " " + str(self.year))
        self.update_days_buttons()

    def create(self):
        root = tk.Tk()
        root.geometry('300x200')
        root.resizable(False, False)
        root.title('Events')



#place menu window into calendar time select window

    def createTimePicker(self):
        root = Tk()
        tp = TimePicker(root)
        tp.pack()
        root.geometry("300x300")
        root.wm_title("Personal Schedule")
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    app = CalendarUI(master=root)
    app.pack(fill="both", expand=True)
    root.mainloop()
