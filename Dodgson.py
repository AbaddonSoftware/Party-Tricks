from dateutil.parser import parse
class Dodgson:
    """An implementation of the Charles Dodgson aka Lewis Caroll Day from Date Trick"""

    @staticmethod
    def get_year_value(year):
        year = year % 100
        return (year // 12) + (year % 12) + ((year % 12) // 4)

    @staticmethod
    def get_century_value(year):
        year = year // 100
        year_values = {19: 0, 20: 6, 21: 4}
        return year_values[year]

    @staticmethod
    def is_leap_year(year):
        return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

    @staticmethod
    def get_month_value(month):
        month_values = {
            1: 0,
            2: 3,
            3: 3,
            4: 6,
            5: 1,
            6: 4,
            7: 6,
            8: 2,
            9: 5,
            10: 0,
            11: 3,
            12: 5,
        }
        return month_values[month]

    @staticmethod
    def get_daydate_value(self, daydate, year):
        return daydate if self.is_leap_year(year) else (daydate - 1)

    def get_weekday_value(self, datetime):
        year, month, day = (
            datetime.year,
            datetime.month,
            datetime.day,
        )
        daydate = self.get_daydate_value(day, year)
        century_value = self.get_century_value(year)
        year_value = self.get_year_value(year)
        month_value = self.get_month_value(month)
        weekday_value = (
            daydate + century_value + year_value + month_value
        ) % 7
        return weekday_value
