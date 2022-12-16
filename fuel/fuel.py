while True:
    Fraction = input ("Fraction=")
    try:
        x0, y0 = Fraction.split ("/")
        x1 = int (x0)
        y1 = int (y0)
        print (x1, y1)
        print (type (x1))
        print (type (x1))
        if (x1 / y1) * 100 == int ("99") or (x1 / y1) * 100 == int ("100"):
            print ("F")
        elif (x1 / y1) * 100 <= int ("1"):
            print ("E")
        else:
            print (str (round (x1 / y1 * 100)) + "%")
    except (ValueError, ZeroDivisionError):
        break
    break