from python_basics.Day_4_Loops_While import loopwhile


# Arbitrary Arguments * which take value as tuples
def nChild(num ,*name):
    print("Total number of children are " + str(num ))

    for n in name:
        print("Name " + n)

nChild(3,"Anu","Shanu","Baby")



# Keyword Arguments
def nameFun(fname,lname,age):

    print("first name is " + fname +" last name is " + lname + " and age is " + str(age))

nameFun(fname="Anu",lname="Hooda",age=28)

nameFun(fname="Shanu",lname="Hooda",age=29)



#Default Parameter Value
def dFun(fname,lname,age=16):
    print("first name is " + fname + " last name is " + lname + " and age is " + str(age))

dFun(fname="Lilly",lname="Yin",age=28)
dFun("Anu","hooda")

#fun to return a number
def numf(num):
    return num


#Passing a List as an Argument
def lFun(fruits):
    for k in fruits:
        print(k)

f=["Apple","Banana","Pear","Grapes","Oranges",100,numf(200)]

lFun(f)







