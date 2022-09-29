payment = 0
amountDue = 50
changeOwed= 0
coke = 50
while amountDue > 0:
    print("Amount Due: ", amountDue)
    coin = int(input("what is your coin?"))
    payment=payment+coin
    if coin == 25 or coin == 10 or coin == 5:
        amountDue = amountDue - coin
    else:
        print(amountDue)
print("Change owed: ", abs(coke-payment))