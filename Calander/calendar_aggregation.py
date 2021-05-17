class LeapChecker:
    def __init__(self):
        pass

    def check(self, year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

class Calendar:
    def __init__(self, leap_checker):
        self._year = 0
        self._month = 0
        self._day = 0
        self._leap_checker = leap_checker

    def set_date(self, year, month, day):
        self._year =year
        self._month = month
        self._day = day

    def get_day_of_week(self):
        total_days = 0
        day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day_of_week = ["일", "월", "화", "수", "목", "금", "토"]

        for year in range(1, self._year):
            if self._leap_checker.check(year):  #윤년일 경우
                total_days += 366
            else:
                total_days += 365
        for month in range(1, self._month):
            total_days += day_of_month[month]

        if self._month >= 3 and self._leap_checker.check(self._year):
            total_days += 1

        total_days += self._day

        return day_of_week[total_days % 7] #해당 요일 return

    def get_year(self):
        return self._year

    def get_month(self):
        return self._month

    def get_day(self):
        return self._day

if __name__ == "__main__":
    leap_checker = LeapChecker()
    my_Calendar = Calendar(leap_checker)
    year = int(input("input a Year:"))
    month = int(input("input a Month:"))
    day = int(input("input a Day:"))
    my_Calendar.set_date(year, month, day)
    print("요일:" + my_Calendar.get_day_of_week())
    print("Year:", my_Calendar.get_year())
    print("Month:", my_Calendar.get_month())
    print("Day:", my_Calendar.get_day())


