try:
    Fraction = input("Fraction=")
    x , y = Fraction.split("/")
    if x.isnumeric() and y.isnumeric:
        x=int(x)
        y=int(y)
        if (x/y)*100 >= int("99"):
           print ("F")
        elif (x/y)*100 <= int("1"):
           print ("E")
        else:
            print(f"{int(x / y * 100)}%")


except :
    print("")