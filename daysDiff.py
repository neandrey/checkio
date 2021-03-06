import datetime, math

def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    f = datetime.date(*date1)
    print(f)
    s = datetime.date(*date2)
    print(s)
    #f - s == datetime.timedelta()
    print((s-f).days)


    return abs((s-f).days)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
