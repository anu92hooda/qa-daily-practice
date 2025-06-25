import random

def Day2():
    num4=(random.randrange(1,20))
    print(num4)
    num1=input("Please Enter a number")
    num2=int(num1)
    num3=num2*num4
    print(num3)

#Day2()

def Day():
    a=100
    b=40
    c=10
    if a>b and a>c:
        print(" a is Biggest number")
    elif b>a and b>c:
        print(" b is Biggest number")
    else:
        print(" c is Biggest number")

   # print(a) if a>b and a>c else print(b) if b>a and b>c else print(c)
Day()






