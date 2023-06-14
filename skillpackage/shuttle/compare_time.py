class Time():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    def __init__(self, day, hour, minute):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.day_index = Time.days.index(self.day)
        if self.minute >= 60:
            self.hour += 1
            self.minute %= 60
        if self.hour >= 24:
            if self.day_index + 1 == len(Time.days):
                self.day = 'Monday'
            else:
            	self.day = Time.days[self.day_index+1]
            self.hour %= 24
        
    def greater_than(self, time2):
        day_index = Time.days.index(self.day)
        if self.day_index > time2.day_index:
            return True
        elif self.day_index == time2.day_index:
            if self.hour > time2.hour:
                return True
            elif self.hour == time2.hour:
                if self.minute > time2. minute:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

        
if __name__ == '__main__':
    a = Time('Tuesday', 12, 4)
    b = Time('Saturday', 12, 4)

    print(b.greater_than(a))