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
            mylist=mylist

        break
sorted_mylist = {k: mylist[k] for k in sorted(mylist)}

print(sorted_mylist)

for i in sorted_mylist:
    print(sorted_mylist[i], i.upper())
