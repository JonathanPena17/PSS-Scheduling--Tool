import tkinter as tk
from tkinter import ttk


class TimePicker(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.clicksingle_button = None
        self.clickreoccurring_button = None
        self.reoccurring_button = None
        self.single_button = None
        self.master = master
        self.months = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']
        self.days = list(range(1, 32))
        self.years = list(range(2023, 2101))
        self.hours = list(range(1, 13))
        self.minutes = list(range(0, 60, 5))
        self.am_pm = ['AM']
        self.am_pm2 = ['PM']
        self.reoccurring_button = ['Reoccurring']
        self.single_button = ['Single']
        self.init_ui()

    def init_ui(self):

        # Create the dropdown menu for month
        self.month_label = tk.Label(self, text='Month:')
        self.month_label.grid(row=0, column=0)
        self.month_var = tk.StringVar(self)
        self.month_var.set(self.months[0])
        self.month_dropdown = ttk.Combobox(self, textvariable=self.month_var, values=self.months)
        self.month_dropdown.grid(row=0, column=1)

        # Create the dropdown menu for day
        self.day_label = tk.Label(self, text='Day:')
        self.day_label.grid(row=1, column=0)
        self.day_var = tk.StringVar(self)
        self.day_var.set(self.days[0])
        self.day_dropdown = ttk.Combobox(self, textvariable=self.day_var, values=self.days)
        self.day_dropdown.grid(row=1, column=1)

        # Create the dropdown menu for year
        self.year_label = tk.Label(self, text='Year:')
        self.year_label.grid(row=2, column=0)
        self.year_var = tk.StringVar(self)
        self.year_var.set(self.years[0])
        self.year_dropdown = ttk.Combobox(self, textvariable=self.year_var, values=self.years)
        self.year_dropdown.grid(row=2, column=1)

        # Create the spinbox for start time
        self.start_label = tk.Label(self, text='Start Time:')
        self.start_label.grid(row=3, column=0)
        self.start_hour_var = tk.StringVar(self)
        self.start_hour_var.set(self.hours[0])
        self.start_hour_spinbox = tk.Spinbox(self, from_=1, to=12, textvariable=self.start_hour_var)
        self.start_hour_spinbox.grid(row=3, column=1)
        self.start_minute_var = tk.StringVar(self)
        self.start_minute_var.set(self.minutes[0])
        self.start_minute_spinbox = tk.Spinbox(self, from_=0, to=55, increment=5, textvariable=self.start_minute_var)
        self.start_minute_spinbox.grid(row=3, column=2)
        self.start_am_pm_var = tk.StringVar(self)
        self.start_am_pm_var.set(self.am_pm[0])
        self.start_am_pm_checkbox_am = tk.Checkbutton(self, text='AM', variable=self.start_am_pm_var, onvalue='AM', offvalue='')
        self.start_am_pm_checkbox_am.grid(row=3, column=3)
        self.start_am_pm_checkbox_pm = tk.Checkbutton(self, text='PM', variable=self.start_am_pm_var, onvalue='PM', offvalue='')
        self.start_am_pm_checkbox_pm.grid(row=3, column=4)


        # Create the spinbox for end time
        self.end_label = tk.Label(self, text='End Time:')
        self.end_label.grid(row=4, column=0)
        self.end_hour_var = tk.StringVar(self)
        self.end_hour_var.set(self.hours[0])
        self.end_hour_spinbox = tk.Spinbox(self, from_=1, to=12, textvariable=self.end_hour_var)
        self.end_hour_spinbox.grid(row=4, column=1)
        self.end_minute_var = tk.StringVar(self)
        self.end_minute_var.set(self.minutes[0])
        self.end_minute_spinbox = tk.Spinbox(self, from_=0, to=55, increment=5, textvariable=self.end_minute_var)
        self.end_minute_spinbox.grid(row=4, column=2)
        self.end_am_pm_var = tk.StringVar(self)
        self.end_am_pm_var.set(self.am_pm[0])
        self.end_am_pm_checkbox = tk.Checkbutton(self, text='AM', variable=self.end_am_pm_var, onvalue='AM', offvalue='')
        self.end_am_pm_checkbox.grid(row=4, column=3)
        self.end_am_pm_checkbox_pm = tk.Checkbutton(self, text='PM', variable=self.end_am_pm_var, onvalue='PM', offvalue='')
        self.end_am_pm_checkbox_pm.grid(row=4, column=4)


        # Create the radio buttons for single/reoccurring events
        self.event_type_label = tk.Label(self, text='Event Type:')
        self.event_type_label.grid(row=5, column=0)
        self.event_type_var = tk.StringVar(self)
        self.event_type_var.set('Single')
        self.single_button = tk.Radiobutton(self, text='Single', variable=self.event_type_var, value='Single')
        self.single_button.grid(row=5, column=1)
        self.reoccurring_button = tk.Radiobutton(self, text='Reoccurring', variable=self.event_type_var, value='Reoccurring')
        self.reoccurring_button.grid(row=5, column=2)

        # Create the submit button
        self.submit_button = tk.Button(self, text='Submit', command=self.submit)
        self.submit_button.grid(row=6, column=2)

        self.msg_display = tk.Label(self, text='')
        self.msg_display.grid(row=7, columnspan=5)


    def submit(self):
        month = self.month_var.get()
        day = self.day_var.get()
        year = self.year_var.get()
        start_hour = self.start_hour_var.get()
        start_minute = self.start_minute_var.get()
        start_am_pm = self.start_am_pm_var.get()
        end_hour = self.end_hour_var.get()
        end_minute = self.end_minute_var.get()
        end_am_pm = self.end_am_pm_var.get()
        event_type = self.event_type_var.get()

        start_minute = f"{int(self.start_minute_var.get()):02d}"
        start_am_pm = self.start_am_pm_var.get()
        end_minute = f"{int(self.end_minute_var.get()):02d}"
        end_am_pm = self.end_am_pm_var.get()

        time_str = f'{month} {day}, {year} - {start_hour}:{start_minute}{start_am_pm} to {end_hour}:{end_minute}{end_am_pm} ({event_type} event)'


        # Read the contents of the file
        with open('user_input.txt', 'r') as f:
            contents = f.readlines()

        # Check if the latest input matches with any previous input
        if time_str+'\n' in contents:
            print("Error: This appointment time has already been booked.")
            self.msg_display.config(text="Error: This appointment time has already been booked.")
        else:
            # Write the latest input to the file
            with open('user_input.txt', 'a') as f:
                f.write(f"{time_str}\n")
            print(f"Your appointment is booked for {time_str}.")
            self.msg_display.config(text=f"Your appointment is booked for {time_str}.")




   