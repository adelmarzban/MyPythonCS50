i=0
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
while True:
    try:
        order = input("order? ")
        if order.title() in menu:
            i=i+menu[order.title()]
            #print(i)
            #print ("$%.2f" % (i))
            print ("Total:" ,"$%.2f" % (i))
    except(EOFError):
        #i = i + menu[order]
        print ("Total:" ,"$%.2f" % (i))
        break