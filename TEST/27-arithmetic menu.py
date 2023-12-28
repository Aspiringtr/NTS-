a=int(input("1.ADDITITON OPERATION\n2.SUBSTRACTION OPERATION\n3.MULTIPICATION OPERATION\n4.DIVISION OPERATION\nEnter your choice(1|2|3|4):"))
if a==1:
    b=int(input("Enter number 1:"))
    c=int(input("Enter number 2:"))
    print("the addition of 1 and 2 is:",b+c)
elif a==2:
    b=int(input("Enter number 1:"))
    c=int(input("Enter number 2:"))
    print("the subtraction of 1 and 2 is:",b-c)
elif a==3:
    b=int(input("Enter number 1:"))
    c=int(input("Enter number 2:"))
    print("the multiplication of 1 and 2 is:",b*c)
elif a==4:
    b=int(input("Enter number 1:"))
    c=int(input("Enter number 2:"))
    print("the division of 1 and 2 is:",b/c)
else:
    print("invalid choice")