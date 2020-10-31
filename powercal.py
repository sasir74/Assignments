#calculator for poer consumption

units = float(input("Please enter Number of Units you Consumed : "))

#USER CONSOLE

if units < 50:
    amount = units * 3

elif units <= 100 and units>=51:
    amount = 150 + ((units - 50) * 6)

elif units <= 200 and units>=101:
    amount = 150 + 300 + ((units - 100) * 9)

else:
    amount = 150 + 300 + 900 + ((units - 200) * 8.45)

print("\nElectricity Bill =  $",amount)
