"""
Create a Time class and initialize it with hours and minutes.
1. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
2. Make a method displayTime which should print the time.
3. Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.
"""
class Time :
    def __init__(self,hours,minutes,Time1,Time2):
        self.hours = hours
        self.minutes = minutes
        self.Time1 = Time1
        self.Time2 = Time2
    
    def addTime(self):
        return (self.Time1) + (self.Time2)
    
    def displayTime(self):
        TotalMinutes = (self.hours)*60 + (self.minutes)
        return TotalMinutes

    
T = Time(5, 30,5.30,1.50)
print(f"Time1 and Time2  sum are : {T.addTime()}")
print(T.displayTime())