class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        valid_hours = 0 <= hours <= Time.max_hours
        valid_minutes = 0 <= minutes <= Time.max_minutes
        valid_seconds = 0 <= seconds <= Time.max_seconds
        if valid_hours and valid_minutes and valid_seconds:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

    def add_trailing_zero(x: int):
        return x if x > 9 else f'0{x}'

    def get_time(self):
        return f'{Time.add_trailing_zero(self.hours)}:' \
               f'{Time.add_trailing_zero(self.minutes)}:' \
               f'{Time.add_trailing_zero(self.seconds)}'

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1

        if self.minutes > Time.max_minutes:
            self.minutes = 0
            self.hours += 1

        if self.hours > Time.max_hours:
            self.hours = 0
        return self.get_time()

time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())