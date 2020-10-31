#calculator for discounts

bill = float(input("Enter bill amount :"))
total1 =(bill*0.25)
total2 =(bill*0.20)
total3 =(bill*0.10)

#User Console

if bill>=3001 :
    print("You got 25% Discount on your bill.")
    print("Now your Bill is ",bill-total1)
elif bill>=2001 and bill<=3000 :
    print("You got 20% Discount on your bill.")
    print("Now your Bill is ",bill-total2)
elif bill>=1001 and bill<=2000 :
    print("You got 10% Discount on your bill.")
    print("Now your Bill is ",bill-total3)
else:
    print("To avail discount, please buy above 1001$ . Thank You.")
