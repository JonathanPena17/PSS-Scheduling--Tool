import tkinter as tk
from tkinter import ttk
import datetime
import calendar
from dateutil.relativedelta import relativedelta

class TimePicker(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.clicksingle_button = None
        self.clickreoccurring_button = None
        self.reoccurring_button = None
        self.single_button = None
        self.antiTasks_button = None
        self.master = master
        self.months = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']
        self.days = list(range(1, 32))
        self.years = list(range(2023, 2101))
        self.hours = list(range(1, 13))
        self.minutes = list(range(0, 60, 5))
        self.am_pm = ['AM']
        self.am_pm2 = ['PM']
        self.task_name = tk.StringVar()
        self.event_type_var = tk.StringVar(self)
        self.reoccurring_freq_var = tk.StringVar(self, value='')
        self.event_type_var.set('Single')
        self.event_types = ['Single', 'Reoccurring', 'Anti-Task']
        self.reoccurring_options = ['Daily', 'Weekly','BiWeekly', 'Monthly', 'Yearly']
        self.init_ui()

    def init_ui(self):

        # Create the dropdown menu for month
        self.month_label = tk.Label(self, text='Month:')
        self.month_label.grid(row=0, column=0)
        self.month_var = tk.StringVar(self)
        self.reoccurring_freq_var = tk.StringVar(self)
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

        # Create the task name input
        self.task_name_label = tk.Label(self, text='Task:')
        self.task_name_label.grid(row=3, column=0)
        self.task_name_entry = tk.Entry(self, textvariable=self.task_name)
        self.task_name_entry.grid(row=3, column=1)

        # Create the spinbox for start time
        self.start_label = tk.Label(self, text='Start Time:')
        self.start_label.grid(row=4, column=0)
        self.start_hour_var = tk.StringVar(self)
        self.start_hour_var.set(self.hours[0])
        self.start_hour_spinbox = tk.Spinbox(self, from_=1, to=12, textvariable=self.start_hour_var)
        self.start_hour_spinbox.grid(row=4, column=1)
        self.start_minute_var = tk.StringVar(self)
        self.start_minute_var.set(self.minutes[0])
        self.start_minute_spinbox = tk.Spinbox(self, from_=0, to=55, increment=5, textvariable=self.start_minute_var)
        self.start_minute_spinbox.grid(row=4, column=2)
        self.start_am_pm_var = tk.StringVar(self)
        self.start_am_pm_var.set(self.am_pm[0])
        self.start_am_pm_checkbox_am = tk.Checkbutton(self, text='AM', variable=self.start_am_pm_var, onvalue='AM', offvalue='')
        self.start_am_pm_checkbox_am.grid(row=4, column=3)
        self.start_am_pm_checkbox_pm = tk.Checkbutton(self, text='PM', variable=self.start_am_pm_var, onvalue='PM', offvalue='')
        self.start_am_pm_checkbox_pm.grid(row=4, column=4)


        # Create the spinbox for end time
        self.end_label = tk.Label(self, text='End Time:')
        self.end_label.grid(row=5, column=0)
        self.end_hour_var = tk.StringVar(self)
        self.end_hour_var.set(self.hours[0])
        self.end_hour_spinbox = tk.Spinbox(self, from_=1, to=12, textvariable=self.end_hour_var)
        self.end_hour_spinbox.grid(row=5, column=1)
        self.end_minute_var = tk.StringVar(self)
        self.end_minute_var.set(self.minutes[0])
        self.end_minute_spinbox = tk.Spinbox(self, from_=0, to=55, increment=5, textvariable=self.end_minute_var)
        self.end_minute_spinbox.grid(row=5, column=2)
        self.end_am_pm_var = tk.StringVar(self)
        self.end_am_pm_var.set(self.am_pm[0])
        self.end_am_pm_checkbox = tk.Checkbutton(self, text='AM', variable=self.end_am_pm_var, onvalue='AM', offvalue='')
        self.end_am_pm_checkbox.grid(row=5, column=3)
        self.end_am_pm_checkbox_pm = tk.Checkbutton(self, text='PM', variable=self.end_am_pm_var, onvalue='PM', offvalue='')
        self.end_am_pm_checkbox_pm.grid(row=5, column=4)

############################################I think the bug is around here #############################################
        # Create the dropdown menu for event type
        self.event_type_label = tk.Label(self, text='Event Type:')
        self.event_type_label.grid(row=7, column=0)
        self.event_type_dropdown = ttk.OptionMenu(self, self.event_type_var, self.event_types[0], *self.event_types, command=self.show_options)
        self.event_type_dropdown.grid(row=7, column=1)
        
        self.show_options()

        # Create the submit button
        self.submit_button = tk.Button(self, text='Submit', command=self.submit)
        self.submit_button.grid(row=9, column=2)

        self.msg_display = tk.Label(self, text='')
        self.msg_display.grid(row=10, columnspan=5)

    def show_options(self, *args):
        event_type = self.event_type_var.get()
        if event_type == 'Single':
            # Hide the reoccurring options
            self.hide_reoccurring_options()
        elif event_type == 'Reoccurring':
            # Show the reoccurring options
            self.show_reoccurring_options()
            self.reoccurring_freq_var = tk.StringVar(self)

    def hide_reoccurring_options(self):
        # Remove the reoccurring option dropdown if it exists
        if hasattr(self, 'reoccurring_option_dropdown'):
                    self.reoccurring_option_dropdown.destroy()

    def show_reoccurring_options(self):
        # Create the dropdown menu for reoccurring options
        self.hide_reoccurring_options()
        self.reoccurring_option_var = tk.StringVar(self)
        self.reoccurring_option_var.set(self.reoccurring_options[0])
        self.reoccurring_option_dropdown = ttk.OptionMenu(self, self.reoccurring_option_var, self.reoccurring_options[0], *self.reoccurring_options)
        self.reoccurring_option_dropdown.grid(row=7, column=2)

################################################^^^^^^^#############################################
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
        task_name = self.task_name_entry.get()
        self.task_name = task_name
        ###########Not sure if this goes here############
        freq = self.reoccurring_freq_var.get()


        # Format time string
        start_minute = f"{int(start_minute):02d}"
        start_am_pm = self.start_am_pm_var.get()
        end_minute = f"{int(end_minute):02d}"
        end_am_pm = self.end_am_pm_var.get()
        
        time_str = f'{month} {day}, {year} - {start_hour}:{start_minute}{start_am_pm} to {end_hour}:{end_minute}{end_am_pm} ({event_type}:{task_name})'

         # Validate input
        try:
                # Convert start and end times to 24-hour format for comparison
                if start_am_pm == 'PM' and int(start_hour) != 12:
                    start_hour = str(int(start_hour) + 12)
                elif start_am_pm == 'AM' and int(start_hour) == 12:
                    start_hour = '0'
                if end_am_pm == 'PM' and int(end_hour) != 12:
                    end_hour = str(int(end_hour) + 12)
                elif end_am_pm == 'AM' and int(end_hour) == 12:
                    end_hour = '0'

                start_time = int(start_hour) * 100 + int(start_minute)
                end_time = int(end_hour) * 100 + int(end_minute)
                if start_time >= end_time:
                    raise ValueError("Start time must be before end time")

        except ValueError as e:
                self.msg_display.config(text=str(e))
                return

        if event_type == 'Single':

            # Check if the latest input matches with any previous input
            with open('user_input.txt', 'r') as f:
                contents = f.readlines()
            if time_str+'\n' in contents:
                    self.msg_display.config(text="Error: This appointment time has already been booked.")
            else:
                # Write the latest input to the file
                with open('user_input.txt', 'a') as f:
                    f.write(f"{time_str}\n")
                    self.msg_display.config(text=f"Your appointment is booked for {time_str}.")
        
        elif event_type == 'Reoccurring':
            ##############This part is not working###############
            print("Reoccurring")
            print(freq)
            print("its not working")

            if freq == 'Daily':
                print("Reoccurring Daily")
                ########This does not print so it must mean that "freq is not being called"
                # Get the user's selected start date
                start_date = datetime.date(year, month, day)

                # Iterate through the rest of the year, incrementing the date by one day
                current_date = start_date
                while current_date.year == year:
                    # Format the current date as a string for display
                    current_date_str = current_date.strftime('%B %d, %Y')
                    
                    # Create a task for the current date
                    time_str = f'{current_date_str} - {start_hour}:{start_minute}{start_am_pm} to {end_hour}:{end_minute}{end_am_pm} ({event_type}:{task_name})'
                    
                    # Write the task to the file
                    with open('user_input.txt', 'a') as f:
                        f.write(f"{time_str}\n")
                    
                    # Increment the date by one day
                    current_date += datetime.timedelta(days=1)
                
                self.msg_display.config(text=f"Your appointment is booked for {time_str}:{freq}")

            elif freq == 'Weekly':
                # Get the user's selected start date
                start_date = datetime.date(year, month, day)

                # Iterate through the rest of the year, incrementing the date by one day
                current_date = start_date
                while current_date.year == year:
                    # Format the current date as a string for display
                    current_date_str = current_date.strftime('%B %d, %Y')
                    
                    # Create a task for the current date
                    time_str = f'{current_date_str} - {start_hour}:{start_minute}{start_am_pm} to {end_hour}:{end_minute}{end_am_pm} ({event_type}:{task_name})'
                    
                    # Write the task to the file
                    with open('user_input.txt', 'a') as f:
                        f.write(f"{time_str}\n")
                    
                    # Increment the date by one day
                    current_date += datetime.timedelta(days=7)
                
                self.msg_display.config(text=f"Your appointment is booked for {time_str}:{freq}")

            elif freq == 'BiWeekly':
                # Get the user's selected start date
                start_date = datetime.date(year, month, day)

                # Iterate through the rest of the year, incrementing the date by one day
                current_date = start_date
                while current_date.year == year:
                    # Format the current date as a string for display
                    current_date_str = current_date.strftime('%B %d, %Y')
                    
                    # Create a task for the current date
                    time_str = f'{current_date_str} - {start_hour}:{start_minute}{start_am_pm} to {end_hour}:{end_minute}{end_am_pm} ({event_type}:{task_name})'
                    
                    # Write the task to the file
                    with open('user_input.txt', 'a') as f:
                        f.write(f"{time_str}\n")
                    
                    # Increment the date by one day
                    current_date += datetime.timedelta(days=14)
                
                self.msg_display.config(text=f"Your appointment is booked for {time_str}:{freq}")
            
            elif freq == 'Monthly':
                # Get the user's selected start date
                start_date = datetime.date(year, month, day)

                # Iterate through the rest of the year, incrementing the date by one month
                current_date = start_date
                while current_date.year == year:
                    # Format the current date as a string for display
                    current_date_str = current_date.strftime('%B %d, %Y')

                    # Create a task for the current date
                    time_str = f'{current_date_str} - {start_hour}:{start_minute}{start_am_pm} to {end_hour}:{end_minute}{end_am_pm} ({event_type}:{task_name})'

                    # Write the task to the file
                    with open('user_input.txt', 'a') as f:
                        f.write(f"{time_str}\n")

                    # Increment the date by one month
                    current_date += relativedelta(months=1)
                
                self.msg_display.config(text=f"Your appointment is booked for {time_str}:{freq}")
            
            elif freq == 'Yearly':
                # Get the user's selected start date
                start_date = datetime.date(year, month, day)

                # Set a maximum number of years to schedule the task
                max_years = 5

                # Iterate through the years, incrementing the year by one
                current_year = start_date.year
                while current_year - start_date.year < max_years:
                    # Format the current date as a string for display
                    current_date_str = start_date.replace(year=current_year).strftime('%B %d, %Y')
                    
                    # Create a task for the current date
                    time_str = f'{current_date_str} - {start_hour}:{start_minute}{start_am_pm} to {end_hour}:{end_minute}{end_am_pm} ({event_type}:{task_name})'
                    
                    # Write the task to the file
                    with open('user_input.txt', 'a') as f:
                        f.write(f"{time_str}\n")
                    
                    # Increment the year by one
                    current_year += 1
                
                self.msg_display.config(text=f"Your appointment is booked for {time_str}:{freq}")
            

            





