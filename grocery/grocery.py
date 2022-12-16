list = {}

while True:
    try:
        fruit = input()
        fruit = fruit.title()
        if fruit in list:
            list[fruit.title()] += 1
        else:
            list[fruit.title()] = 1
    except (EOFError):
        for i in list:
            print(list[i], i.upper())
        break
