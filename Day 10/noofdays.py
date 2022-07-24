#check if its leap year or not
def leapyear(year):
    """Check if its leap year or not and returns true or false """
    if(year%4==0):
        if(year%100==0 and year%400!=0):
            return False
        else:
            return True
    else:
       return False

def days_in_month(month,year):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if month==2:
        if leapyear(year):
            return 29
        else:
            return 28
    else:
        return month_days[month-1]


year=int(input('Enter the year'))
month=int(input(("Enter a month:")))
print(days_in_month(month, year))
