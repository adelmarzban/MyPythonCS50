try:
    Fraction = input("Fraction=")
    x , y = Fraction.split("/")
    x=int(x)
    y=int(y)
#    print(type(x))
 #   print(type(y))
  #  print((x))
   # print((y))
    if  x <= y  and y>0:
        x=int(x)
        y=int(y)
        if (x/y)*100 == int("99") or (x/y)*100 == int("100"):
           print ("F")
        elif (x/y)*100 <= int("1"):
           print ("E")
        else:
            print(str(round(x / y * 100))+"%")


except :
    print("")