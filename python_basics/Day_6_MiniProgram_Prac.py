#Calculator (add, subtract, multiply, divide with user input)
numb1=int(input("Please enter a number "))
numb2=int(input("Please enter another number"))
opr=input("Please select the operators you want to use Add  or Subtract or Multiply  or Divide  ")

def calculator(num1,num2,operator):

    if operator.lower() == "add":
        result =num1+num2
        print(result)

    elif operator.lower() == "subtract":
        result = num1 - num2
        print(result)

    elif operator.lower() == "multiply":
        result = num1 * num2
        print(result)

    elif operator.lower() == "divide" :
        result = num1 / num2
        print(result)

    else:
        print("There is some issue please try again")



calculator(numb1,numb2,opr)


# function to check if number is prime or not
pnum= int(input("Please enter the number , to check if number is prime or not"))

def primechecker(number):

    if number<=1:
        return False

    for i in range(2,int(number**0.5)+1):
        if number% i ==0:
            return False

    return True

if primechecker(pnum):
    print(f"{pnum} Number is Prime ")

else:
    print(f"{pnum} Number is not Prime ")









