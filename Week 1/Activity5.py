
def extractMarkers(source, markers):

    result = dict.fromkeys(markers,0)
    for marker in markers:
        while marker in source:
            result[marker] +=1
            source = source.replace(marker,"",1)
    return result, source

def removeSpaces(source):

    return source.replace(" ","")


def exercise1():

    vowels = ("A", "E", "I", "O", "U")
    userInput = input("Input a sentence to analyse:\n")
    result, extractedInput = extractMarkers(userInput.upper(), vowels)
    for marker in vowels:
        print("{}: {}".format(marker, "*"*result[marker]))
    cleanInput = removeSpaces(extractedInput)
    print("Other (non-space) Characters: {}".format(len(cleanInput)))

def isAnagram(source, comparison):

    for letter in source:
        if letter in comparison:
            source = source.replace(letter, "", 1)
            comparison = comparison.replace(letter, "", 1)
        else:
            return False
    return True

def exercise2():

    word1 = input("input the first word: ")
    word2 = input("input the second word: ")
    if isAnagram(word1,word2):
        print("These are anagrams")
    else:
        print("These are not anagrams")




exercise1()
exercise2()
