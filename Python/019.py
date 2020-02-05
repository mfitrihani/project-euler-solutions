import datetime

if __name__ == '__main__':
    year = 1901
    month = 1
    sundays = 0
    while year <= 2000:
        if datetime.date(year, month, 1).weekday() == 6:
            sundays += 1
        month += 1
        if month > 12:
            year += 1
            month = 1
    print(sundays)
