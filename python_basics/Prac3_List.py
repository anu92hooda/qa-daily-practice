def lis_pra():
    #list 1
    mylist1=["Apple","Banana","Mango"]
    print(mylist1)

    #assigning list values to indivisual variable
    a,b,c =mylist1
    print(a)

    # finding length of list
    l=(len(mylist1))
    print(l)

    # list can have diff data types , and list data type is list in python.
    # we can create list from list Constructor
    mylist2=list(("Apple",100,"love",True,455,677))
    print(type(mylist2))

    #Accessing List items
    print(mylist2[1:2])
    print(mylist2[:3])

    # checking is item present in list
    if 100 and "Apple" in mylist2 :
        print("yes 100 and Apple is there")

lis_pra()

def lis_pra1():
    #Change List item
    mylist3= list(("Apple", 100, "love", True, 455, 677))
    mylist3[2:3]=["You",580,"love"]
    print(mylist3)

    #Insert the item with insert method , without replacing
    mylist3.insert(5,"we")
    print(mylist3)

    #Append and extend function
    mylist4= [1,2,3,4,5]
    mylist5= [7,8,9,10,11]
    mylist4.append(6)
    print(mylist4)

    mylist4.extend(mylist5)
    print(mylist4)

    #Remove , Del and Pop
    mylist4.remove(5)
    mylist4.pop() #If no index is given it should remove last one
    print(mylist4)

    del mylist4

lis_pra1()

def lis_pra2_loop():
    mylist3 = list(("Apple", 100, "love", True, 455, 677))

    for i in mylist3:
       print(i)
    #[ print(i) for i in mylist3]

    #print((mylist3.sort()))
    #mylist3.sort(reverse=True)
    #mylist3.sort(key= str.lower)
    mylist3.reverse()
    print(mylist3)

    #Copy List
    newcoplylist3= mylist3.copy()
    print(newcoplylist3)

    copylist3= list(mylist3)
    print(copylist3)

    newcoplylist3=newcoplylist3+copylist3
    print(newcoplylist3)

    for x in copylist3:
        newcoplylist3.append(x)
        print(newcoplylist3)


lis_pra2_loop()

























