try:
    Fraction = input("Fraction=")
    x , y = Fraction.split("/")

    if (int(Fraction2[0])/int(Fraction2[1]))*100 >= int("99"):
        print ("F")
    elif (int(Fraction2[0])/int(Fraction2[1]))*100 <= int("1"):
        print ("E")
    else: print(round((int(Fraction2[0]) / int(Fraction2[1])) * 100 ),"%")


except :
    print("")