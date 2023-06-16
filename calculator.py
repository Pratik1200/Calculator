n1=1 
while n1 == 1:
    print ("Welcome to Calculator")
    print ("Select any one from the following")
    print ("1-Addition \n2-Subtraction \n3-Multiplication \n4-Division")
    value=int(input("Enter your choice"))
    if value == 1:
        a=float(input("Enter first silly;)"))
        b=float(input("Now enter second number;)"))
        print("result is :", a+b)
    elif value == 2:
        a=float(input("Enter first Number ;)"))
        b=float(input("Now enter second number ;)"))
        print("result is :", a-b)
    elif value == 3:
        a=float(input("Enter first Number;)"))
        b=float(input("Now enter second number;)"))
        print("result is :", a*b)
    elif value == 4:
        a=float(input("Enter first Number;)"))
        b=float(input("Now enter second number;)"))
        print("result is :", a/b)
    else:
        print("select from 1-4")
    n=input("Press 1 if you want to go again;(:)")
    if n!="1":
        exit()
    n1=int(n)