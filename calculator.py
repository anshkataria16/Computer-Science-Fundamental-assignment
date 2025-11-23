print("1. Addition\n2.Subtraction\n3. mulitiplication\n4.Divide\n5.Exit")
opt=int(input("enter your option"))
if opt==5:
    exit()
elif opt==1:
    a=int(input("enter first number"))
    b=int(input("enter the second number"))
    print("the addition of the number is",a+b)
elif opt==2:
    a=int(input("enter first number"))
    b=int(input("enter the second number"))
    print("the subtraction of the number is",a-b)
elif opt==3:
    a=int(input("enter first number"))
    b=int(input("enter the second number"))
    print("the multiplication of the number is",a*b)
elif opt==1:
    a=int(input("enter first number"))
    b=int(input("enter the second number"))
    print("the division of the number is",a/b)
else:
    print("please enter the valid option")
