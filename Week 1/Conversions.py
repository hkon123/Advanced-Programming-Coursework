
def feetToMeters(input):

    return input*0.3048

def inchesToMeters(input):

    return input*0.0254

def feetAndInchesToMEters(feet, inches):

    return feetToMeters(feet) + inchesToMeters(inches)

def poundsToKg(input):

    return input*0.45359

def kelvinToCelsius(input):

    return input+272.15

def minutesToSeconds(input):

    return input*60

def hoursToSeconds(input):

    return minutesToSeconds(input*60)

def hoursAndMinutesToSeconds(hours, minutes):

    return hoursToSeconds(hours) + minutesToSeconds(minutes)
