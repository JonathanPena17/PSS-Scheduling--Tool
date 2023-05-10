import tkinter as tk
from tkinter import ttk




# menu window for creating a new appointment


#picker data for time
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

        # Create the spinbox for hour
        self.hour_label = tk.Label(self, text='Hour:')
        self.hour_label.grid(row=3, column=0)
        self.hour_var = tk.StringVar(self)
        self.hour_var.set(self.hours[0])
        self.hour_spinbox = tk.Spinbox(self, from_=1, to=12, textvariable=self.hour_var)
        self.hour_spinbox.grid(row=3, column=1)

        # Create the spinbox for minutes
        self.minute_label = tk.Label(self, text='Minute:')
        self.minute_label.grid(row=4, column=0)
        self.minute_var = tk.StringVar(self)
        self.minute_var.set(self.minutes[0])
        self.minute_spinbox = tk.Spinbox(self, from_=0, to=55, increment=5, textvariable=self.minute_var)
        self.minute_spinbox.grid(row=4, column=1)

        # Create the checkbox for AM
        self.am_pm_var = tk.StringVar(self)
        self.am_pm_var.set(self.am_pm[0])
        self.am_pm_checkbox = ttk.Checkbutton(self, text='AM', variable=self.am_pm_var, onvalue='AM', offvalue='')
        self.am_pm_checkbox.grid(row=5, column=1)

        # Create the checkbox for PM
        self.am_pm_var2 = tk.StringVar(self)
        self.am_pm_var2.set(self.am_pm2[0])
        self.am_pm_checkbox2 = ttk.Checkbutton(self, text='PM', variable=self.am_pm_var2, onvalue='PM', offvalue='')
        self.am_pm_checkbox2.grid(row=6, column=1)

        #Create the reoccurring button
        self.reoccurring_var = tk.StringVar(self)
        self.reoccurring_var.set(self.reoccurring_button[0])
        self.reoccurring_button = ttk.Button(self, text='Reoccurring', command=self.clickreoccurring_button)
        self.reoccurring_button.grid(row=6,column=3)
        #Create the single button
        self.single_var = tk.StringVar(self)
        self.single_var.set(self.single_button[0])
        self.single_button = ttk.Button(self, text='Single', command=self.clicksingle_button)
        self.single_button.grid(row=5,column=3)

        self.pack()






 # need submit button


# might need to update logic to restrict time selection
'''logic to restrict time selection
        if self.last_value == "59" and self.min_string.get() == "0":
            self.hour_string.set(int(self.hour_string.get())+1 if self.hour_string.get() !="23" else 0)   
            self.last_value = self.min_string.get()

        if self.last_value_sec == "59" and self.sec_hour.get() == "0":
            self.min_string.set(int(self.min_string.get())+1 if self.min_string.get() !="59" else 0)
        if self.last_value == "59":
            self.hour_string.set(int(self.hour_string.get())+1 if self.hour_string.get() !="23" else 0)            
            self.last_value_sec = self.sec_hour.get()
'''
