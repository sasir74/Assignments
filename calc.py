#calculator for basic

print(" MY CALCULATOR\n"
      " =============\n"
      "1. ADD\n"
      "2. SUBTRACT\n"
      "3. MULTIPLY\n"
      "4. DIVISON\n"
      "5. EXIT\n")
option = int(input("Please choose OPTION :"))

if option==1 :
    a = int(input("Enter value A : "))
    b = int(input("Enter value B : "))
    print(a+b)
elif option==2 :
    a = int(input("Enter value A : "))
    b = int(input("Enter value B : "))
    print(a-b)
elif option==3 :
    a = int(input("Enter value A : "))
    b = int(input("Enter value B : "))
    print(a*b)
elif option==4 :
    a = int(input("Enter value A : "))
    b = int(input("Enter value B : "))
    print(a/b)
elif option!=5:
    print("I don't understand your option... Please try again.")
else:
    print("Bye...")
