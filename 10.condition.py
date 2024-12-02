is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("drink plenty of water")
elif is_cold:
    print("It's a cold day")  
    print("wear warm clothes") 
else:
    print("It's a lovely day")


#price of a house is 1M.if buyer has good credit ,they need to put down 10% otherwise 20%.print the down payment.

price = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}  ")      

