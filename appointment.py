import calendar
import schedule

class appointment:

   def __init__(self, date, time, participants,location,startDate,endTime, howOften):
        calendar.date=date
        calendar.time=time
        self.participants=participants
        self.location=location
        schedule.howOften=howOften
        #not sure how to  get new dates for easy making of start and end times, they wont be needed for every appointment
        calendar.startDate=startDate
        calendar.endTime=endTime


    


