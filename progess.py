#Student Progress Report App

rollno = int(input("Enter Your RollNo : "))
name = input("Enter Your Name :")
sub1 = int(input("Enter Subject 1 Marks : "))
sub2 = int(input("Enter Subject 2 Marks : "))
sub3 = int(input("Enter Subject 3 Marks : "))
sub4 = int(input("Enter Subject 4 Marks : "))
sub5 = int(input("Enter Subject 5 Marks : "))
sub6 = int(input("Enter Subject 6 Marks : "))
total = sub1+sub2+sub3+sub4+sub5+sub6
average = total/6

#User Console
print("Roll Number : ",rollno)
print("Student Name : ",name)
print("Total Marks : ",total)
print("Percentage : ",average)
if average>=80 and  average<=100 :
    print("Grade is   A")
elif average>=60 and average<=79 :
    print("Grade is   B")
elif average>=50 and average<=59 :
    print("Grade is   C")
elif average>=40 and average<=49 :
    print("Grade is   D")
elif average<40 :
    print("You are Promoted")
else:
    print("Enter valid Marks to get grade.")
