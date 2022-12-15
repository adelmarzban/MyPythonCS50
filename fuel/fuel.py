try:
    Fraction = input("Fraction=")
    Fraction2 = Fraction.split("/")

    if (int(Fraction2[0])/int(Fraction2[1]))*100 == int("100"):
        print ("F")
    elif (int(Fraction2[0])/int(Fraction2[1]))*100 == int("0"):
        print ("E")
    else: print((int(Fraction2[0]) / int(Fraction2[1])) * 100 )


except :
    print("")