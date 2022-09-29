vowel= ["a", "e", "i", "o", "u"]
word= input("Input: ")
for char in word.lower():
    if not char in vowel:
        print (char , end="")