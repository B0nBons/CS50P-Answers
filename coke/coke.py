price = 50
tot_paid = 0

while price > 0:
    print("Amount Due: "+ str(price))
    pay = int(input("Insert Coin: "))

    if pay == 5 or pay == 10 or pay ==25:
        price = price - pay
        tot_paid += pay

    if price == 0:
        break

if tot_paid >= price:
    fin = tot_paid - 50
    print("Change Owed: " + str(fin))
