amount_due=50
while(amount_due>0):
    print("Amount due:", amount_due)
    coin=int(input("Insert coin: "))
    if coin in [25, 10, 5]:
        amount_due-=coin

change=abs(amount_due)
print("Change Owed:", change)