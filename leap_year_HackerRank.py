def is_leap(year):
    leap = False
    if ( year % 4 == 0 and year % 100 != 0):
        leap = True
    elif (year % 100 == 0 and year % 400 == 0):
        leap = True
    # else:
    #     print("{0} is not a leap year".format(year))
    return leap
    

year = int(input("Enter num : "))
print(is_leap(year))