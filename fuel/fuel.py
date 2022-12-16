while True:
    fraction = input ("Fraction:")
    try:
        #print(len (fraction))
        x , y = fraction.split("/")
        f= (int(x)/int(y))
        #print(len(x)+1)
        fraction[len(x)] == "/" and x.isnumeric() and y.isnumeric()
        if f <=1:
            break
    except(ValueError,ZeroDivisionError):
        pass
if f*100 <= 1:
    print ("E")
if f*100 >= 99:
    print ("F")
else:
    print(str(round(f*100))+"%")