amount_due = 50

while amount_due > 0:
    print("Amount Due: ",amount_due)
    coin = int(input("Insert Coin: "))
    amount_due = amount_due - coin
    if amount_due == 0:
        print("Change Owed:  0")
    elif amount_due < 0:
        print("Change Owed:", (amount_due * -1))
