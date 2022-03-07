

class Stack:


    def __init__(self):
        self.container = []

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop(-1)

    def view(self):
        print(self.container)


class Queue:


    def __init__(self):
        self.container = []

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop(0)

    def view(self):
        print(self.container)

def exercise1():

    current = []
    while True:
        print("\n\n\n")
        opt = int(input("Create a stack(0), queue(1) or exit(2): "))
        print("\n\n\n")
        if opt == 0:
            stack = Stack()
            current.append(stack)
        elif opt == 1:
            queue = Queue()
            current.append(queue)
        else:
            break
        while True:
            print("\n\n\n")
            option = int(input( "1. Push\n"\
                                "2. Pop\n"\
                                "3. View\n"\
                                "4. Exit\n"
                                "ans: "))
            if option == 1:
                current[-1].push(input("Enter item: "))
            elif option == 2:
                print(current[-1].pop())
            elif option == 3:
                current[-1].view()
            else:
                break

def exercise2():
    template1 = "{:<10} {:>5}: ${:.2f} ${:<4}"
    template2 = "{:<15} : ${:.2f} ${:<4}"
    inputSales = [[390, 250, 460, 470], [345, 270, 480, 510], [379, 300, 450, 360]]
    locations = {"L3":"London", "P2":"Paris", "N6":"New York", "B8":"Beijing"}
    keys = ("L3", "P2", "N6", "B8")
    months = ("Apr18", "May18", "Jun18")
    for i in range(len(locations)):
        print(template1.format(locations.get(keys[i]),keys[i], sum(j[i]for j in inputSales)/len(inputSales), sum(j[i]for j in inputSales)))
    print()
    for i in range(len(months)):
        print(template2.format(months[i], sum(inputSales[i])/len(inputSales[i]), sum(inputSales[i])))
    print()
    print("Total: ${}".format(sum(sum(j) for j in inputSales)))

exercise2()
