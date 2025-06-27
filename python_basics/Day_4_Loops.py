def floop():

    # for loop in list
    mylist=["Apple","Banana","Pears","lemon","tomato","peas","redlime","greenlime","blacklime"]

    for x in mylist:
        #print(x)

        if x=="redlime" or x=="blacklime" :
            print("we dony need this type of lime ")
            continue

        print(x)

        if x== "greenlime":
            break

#floop()

def floop1():

    #for look with range function
    i=0

    for y in range(10):
        print(y)

        if y==7:
            break

    # or look with string and counting how many time "a" appears
    for k in "laoavaeaiasaianatahaeair":

        if k == "a":
            i=i+1

    print("Total count for a is" + "" + str(i))


    #Nested for loop
    for a in range(6):
         for b in range(1,a+1):
             print("*",end="  ")
         print()



floop1()


