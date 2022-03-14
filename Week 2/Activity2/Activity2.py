
def printListOfDict(input, keys, template):

    print(template.format(*keys))
    for item in input:
        print(template.format(*list(item.get(key) for key in keys)))

def writeListOfDictsToFile(input, keys, template, filename, type, header = True):

    file = open(filename, type)
    if header:
        file.write(template.format(*keys))
    for item in input:
        file.write(template.format(*list(item.get(key) for key in keys)))



def exercise1(debug = True):

    input = open("PeopleTrainngDate.csv")
    keys = input.readline().rstrip("\n").split(",")
    data = []
    for line in input:
        rawSplit = line.rstrip("\n").split(",")
        fixedSplit = [rawSplit[0]]
        fixedSplit.append(rawSplit[1].strip("\"") + "," + rawSplit[2].strip("\""))
        fixedSplit.extend(rawSplit[3:-1])
        fixedSplit.append(Date(rawSplit[-1]))
        data.append(dict(zip(keys,fixedSplit)))
    input.close()
    if debug:
        printListOfDict(data,keys,"{:<10}{:<22} {:<20}{:<45} {:<45}{:<25}")
    return data, keys




class Date(object):


    def __init__(self, dateString):

        self.day = int(dateString.split(("/"))[0])
        self.month = int(dateString.split(("/"))[1])
        self.year = int(dateString.split(("/"))[2])

    def __str__(self):

        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def __format__(self, format_spec):

        return f"{self.day:02d}/{self.month:02d}/{self.year}" + " "*int((int(format_spec[1:])/2)-2)

    def __lt__(self, other):

        if self.year <= other.year:
            if self.month <= other.month:
                if self.day < other.day:
                    return True
            if self.month < other.month:
                return True
        if self.year < other.year:
            return True
        return False



def exercise2():

    data, keys = exercise1(debug = False)
    data.sort(key=lambda x: x.get('Updated'))
    keys.insert(0, keys.pop())
    writeListOfDictsToFile(data,keys,"{:<15} {:<10} {:<22} {:<20} {:<45}{:<45}\n", "exercise2Output.txt", 'w')

def exercise3():
    input = open("PeopleTrainingDateUpdate.csv")
    keys = ["Updated","Email","ID","Title","Name","Company",]
    data = []
    for line in input:
        rawSplit = line.rstrip("\n").split(",")
        fixedSplit = [Date(rawSplit[0])]
        fixedSplit.extend(rawSplit[1:4])
        fixedSplit.append(rawSplit[4].strip("\"") + "," + rawSplit[5].strip("\""))
        fixedSplit.extend(rawSplit[6:])
        data.append(dict(zip(keys,fixedSplit)))
    input.close()
    data.sort(key=lambda x: x.get('Updated'))
    dontNeed, origKeys = exercise1(debug = False)
    origKeys.insert(0, origKeys.pop())
    writeListOfDictsToFile(data,origKeys,"{:<15} {:<10} {:<22} {:<20} {:<45}{:<45}\n", "exercise2Output.txt", 'a', header = False)

exercise1()
exercise2()
exercise3()
