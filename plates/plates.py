plate= input("Input: ")
valid = False
if len(plate)<=6 and len(plate)>=2 \
            and plate[0].isalpha() \
            and plate[1].isalpha():
    letter_finished = False
    valid = True
    for c in plate:
        if not c.isalpha() and not c.isdigit():
            valid = False
        if not letter_finished:
            if c.isdigit():
                letter_finished = True
                if c == '0':
                    valid = False
        elif c.isalpha():
            valid = False

if valid:
    print("Valid")
else:
    print("Invalid")