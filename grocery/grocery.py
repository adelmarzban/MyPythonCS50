mylist = {}

while True:
    try:
        fruit = input()
        fruit = fruit.title()
        if fruit in mylist:
            mylist[fruit.title()] += 1
        else:
            mylist[fruit.title()] = 1
    except EOFError:
        for i in mylist:
            mylist=(sorted(mylist))
            print(mylist[i], i.upper())
        break