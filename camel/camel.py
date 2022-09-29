camelcase = input("camelCase:")
for char in camelcase:
    if char.isupper()==True:
        char=("_"+char.lower())
    else:
        char=char
    print(char, end="")