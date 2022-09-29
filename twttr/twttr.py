vowel= ["a", "A", "E", "e", "I", "i", "O", "o", "U" ,"u"]
word= input("Input: ")
for char in word:
    if not char in vowel:
        print (char , end="")