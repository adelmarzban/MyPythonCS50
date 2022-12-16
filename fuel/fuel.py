while True:
    Fraction = input ("Fraction=")
    try:
        x0, y0 = Fraction.split ("/")
        x1 = int (x0)
        y1 = int (y0)
        fuel = x1/y1
        #print (x1, y1)
        #print (type (x1))
        #print (type (x1))
        if fuel > 1:
            break
        if (fuel) * 100 == int ("99") or (fuel) * 100 == int ("100"):
            print ("F")
        elif (fuel) * 100 <= int ("1"):
            print ("E")
        else:
            print (str (round (fuel * 100)) + "%")
    except (ValueError, ZeroDivisionError):
        print("ValueError", "ZeroDivisionError")
        break
    break