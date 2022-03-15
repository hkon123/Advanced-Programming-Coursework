import re

def exercise2():

    file = open("The_Raven.txt", encoding="utf8")
    input = ""
    for line in file:
        input += line

    result = re.findall("shrieked", input)
    if len(result)>0:
        print("shrieked is in the text")
    else:
        print("shrieked is noy in the text")

    result = re.findall("bleak", input)
    if len(result)>0:
        print("bleak is in the text")
    else:
        print("bleak is not in the text")

    result = re.findall("\w*pp\w+", input)
    print(f"pp is in {len(result)} words")

    newInput = input.replace("!","#")
    print(newInput)

    result = re.findall(r"\b[tT]\w*(?<!e)\b", input)
    template = "{}, " * len(result)
    print("These words start with t and do not end with e " + template.format(*result))




def main():
    exercise2()

if __name__ == "__main__":
    main()
