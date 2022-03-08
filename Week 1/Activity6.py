import Conversions as cv

def exercise1():

    while True:
        try:
            option = int(input( "\n\n\nConversions:\n"\
                                "1. Feet and inches to meters\n"\
                                "2. Pounds to kilograms\n"\
                                "3. Kelvin to Celsius\n"\
                                "4. Hours and minutes to seconds\n"\
                                "5. Quit\n"
                                "ans: "))
            if option == 1:
                feet = int(input("Feet: "))
                inches = int(input("Inches: "))
                if feet < 0 or inches < 0:
                    print("\n\n use valid input!\n\n")
                    continue
                print("Meters: {}".format(cv.feetAndInchesToMEters(feet, inches)))
            elif option == 2:
                pounds = int(input("Pounds: "))
                if pounds < 0:
                    print("\n\n use valid input!\n\n")
                    continue
                print("Kilograms: {}".format(cv.poundsToKg(pounds)))
            elif option == 3:
                kelvin = int(input("Kelvin: "))
                if kelvin < 0:
                    print("\n\n use valid input!\n\n")
                    continue
                print("Celsious: {}".format(cv.kelvinToCelsius(kelvin)))
            elif option == 4:
                hours = int(input("Hours: "))
                minutes = int(input("Minutes: "))
                if hours < 0 or minutes < 0 or minutes > 60:
                    print("\n\n use valid input!\n\n")
                    continue
                print("Seconds: {}".format(cv.hoursAndMinutesToSeconds(hours, minutes)))
            elif option == 5:
                break
        except:
            print("\n\n use valid input!\n\n")
            continue

def exercise2():
    Janet = DistanceStudent("Mr Janet Sanet Greenhold", "place", 21, 1, "Advanced Programming")
    Janet.printStatus()



class Person(object):


    def __init__(self, name, address, age):


        namelist = name.split()

        self.name = Name(namelist[1], namelist[-1], namelist[0], namelist[2:-1])
        self.address = address
        self.age = age

    def personalDetails(self):

        return self.name, self.address, self.age


class Student(Person):


    def __init__(self, name, address, age, id):

        super(Student, self).__init__(name, address, age)
        self.id = id

    def personalDetails(self):

        return super(Student, self).personalDetails(),self.id


class Name(object):


    def __init__(self, firstName, surname, title, *otherName):

        self.firstName = firstName
        self.surname = surname
        self.title = title
        self.otherName = list(otherName)

    def formalName(self):
        print("{} {}. ".format(self.title, self.firstName[0].upper()), end="")
        for name in self.otherName[0]:
            print("{}. ".format(name[0].upper()), end="")
        print(self.surname, end="")


class DistanceStudent(Student):


    def __init__(self, name, address, age, id, currentModule):

        super(DistanceStudent, self).__init__(name, address, age, id)
        self.currentModule = currentModule

    def printStatus(self):
        self.name.formalName()
        print(" is currently studying the {} module.".format(self.currentModule))

exercise1()
exercise2()
