

def exercise1():

    multiplier = 2
    while True:
        try:
            userInput = int(input("Enter number to show times table of: "))
            break;
        except:
            print("Please use an integer value")
    print(f"The even timetable for {userInput} is:")
    while multiplier <= 20:
        print("{:>9} times {} is {}".format(multiplier, userInput, userInput*multiplier))
        multiplier+=2

def exercise2():

    symbol = "*"
    triangleOrientations = ["<", ">", "^"]
    while True:
        try:
            triangleOrientation = triangleOrientations[int(input("Do you want a left sided triangle(0), a right sided triange(1) or a diamond(2): "))]
            triangleSize = int(input("What size do you want the pattern to be: "))
            if triangleOrientation == "^" and triangleSize%2 == 0:
                print("\n\nUse odd sizes for the pattern when choosing diamond\n\n")
                continue
            break
        except:
            print("\n\nUse integers as input, and only specified integers for the type selection\n\n")
    for i in range(triangleSize):
        print("{:{orientation}{size}}".format(symbol, size = triangleSize, orientation = triangleOrientation))
        if triangleOrientation != "^":
            symbol = symbol + "*"
        elif i < triangleSize//2:
            symbol = symbol + "**"
        else:
            symbol = symbol[:-2]

def exercise3():

    template = "{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}"
    weekdays = template.format("M", "T", "W", "Th", "F", "S", "Su")
    filler = ""
    while True:
        try:
            daysInMonth = int(input("How many days in the month(28-31): "))
            startDay = int(input("What day is the first on the month(1-7): ")) - 1
            if daysInMonth < 28 or daysInMonth > 31 or startDay < 0 or startDay > 6:
                print("\n\nAssign values within the specified ranges\n\n")
                continue
            break
        except:
            print("\n\nUse integers to define values\n\n")
    print(weekdays)
    days = [*range(1,daysInMonth+1)]
    firstWeekDays = days[0:7-startDay]
    week1Tuple = tuple(filler for i in range(startDay))
    tempWeekList = list(week1Tuple)
    tempWeekList.extend(firstWeekDays)
    week1Tuple = tuple(tempWeekList)
    print(template.format(*week1Tuple))
    startDay = 7-startDay
    for i in range(5):
        try:
            print(template.format(*tuple(days[startDay:startDay+7])))
            startDay+=7
        except:
            lastWeekDays = days[startDay:daysInMonth]
            lastWeekTuple = tuple(filler for i in range(7-len(lastWeekDays)))
            tempWeekList = list(lastWeekTuple)
            lastWeekDays.extend(tempWeekList)
            lastWeekTuple = tuple(lastWeekDays)
            print(template.format(*lastWeekTuple))
            break


exercise1()
exercise2()
exercise3()
