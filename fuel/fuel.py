try:
    Fraction = input("Fraction=")
    x , y = Fraction.split("/")
    if x.isnumeric() and y.isnumeric and y > "0" and x<=y:
        x=int(x)
        y=int(y)
        if (x/y)*100 >= int("99"):
           print ("F")
        elif (x/y)*100 <= int("1"):
           print ("E")
        else:
            print(str(round(x / y * 100))+"%")


except :
    print("")