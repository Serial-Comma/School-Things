def leapyear(year):
    leap = False
    if (year % 400 == 0) and (year % 100 == 0):
        leap = True
        return leap
    elif (year % 4 ==0) and (year % 100 != 0):
        leap = True
        return leap
    else:
        leap = False
        return leap

months = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']

x = input("Input the month and year in the form MM/YYYY ")

x = x.split('/')

month = int(x[0])
year = int(x[1])
    
leap = leapyear(year)
if leap == False:
    print("{} is not a leap year".format(year))
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print("{} has 31 days".format(months[month-1]))
    elif month == 2:
        print("{} has 28 days".format(months[month-1]))
    else:
        print("{} has 30 days".format(months[month-1]))
    
else:
    print("{} is a leap year".format(year))
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print("{} has 31 days".format(months[month-1]))
    elif month == 2:
        print("{} has 29 days".format(months[month-1]))
    else:
        print("{} has 30 days".format(months[month-1]))


