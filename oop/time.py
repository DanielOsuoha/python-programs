class Time:
    def __init__(self, time) -> None:
        self.time = time
    
    def convert_to_minutes(self):
        m  = self.time//60
        s = self.time % 60
        print(str(m) + ':' + str(s))

    def convert_to_hours(self):
        h = self.time//3600
        m  = (self.time % 3600)//60
        s = (self.time % 3600) % 60
        print(str(h) + ':' + str(m) + ':' + str(s))

time = Time(60080)
time.convert_to_minutes()
time.convert_to_hours()