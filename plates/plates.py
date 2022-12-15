sym=[ ". ",", ", ";",":" ]
plate= input("Input: ")
if len(plate)<=6 and len(plate)>=2 \
            and plate[0].isalpha() \
            and plate[1].isalpha() \
            and plate[-4::-1].isalpha() \
            and plate[0] !="0"  :
    print("Valid")
else:
    print("Invalid")