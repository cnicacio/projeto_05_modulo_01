class Time:
    def __init__(self):
        self.hours = 6
        self.minutes = 0
        self.days = 1
    
    def __str__(self): 
        return f"Dia {self.days}, {self.hours:02d}:{self.minutes:02d}"
    
    def forward(self, minutes):
        self.minutes += minutes
        while(self.minutes >= 60):
            self.minutes -= 60
            self.hours += 1
        while(self.hours >= 24):
            self.hours -= 24
            self.days += 1
    
    def late(self):
        if self.hours >= 8 and self.minutes > 0 or self.hours > 8:
            return True
    
    def define(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        return f"Dia {self.days}, {self.hours:02d}:{self.minutes:02d}"