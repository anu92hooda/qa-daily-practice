from audioop import reverse

from marshmallow.fields import Integer


# Day 2 Practise
def day2():
    try:
        usernumber= int(input("Please enter a number "))

        if usernumber>0:
            print("postive")

        elif usernumber<0:
            print("negative")

        else:
            print("zero")

    except ValueError:
        print("wrong input")

#day2()

#Day 3 Practise
def day3():
    try:
        number_list = []

        for i in range(1,6):

            user_input= int(input(f"Please enter {i} number"))
            number_list.append(user_input)


        total_sum=0
        high_numb=number_list[0]
        low_num=number_list[0]

        for num in number_list:
            total_sum += num

            if num>high_numb:
                high_numb=num

            if num<low_num  :
                low_num=num


        #print(f"Total sum is {total_sum}")
        #print(f"highest num is {high_numb}")
        #print(f"lowest number is {low_num}")

        print(sum(number_list))
        print(max(number_list))
        print(min(number_list))

        rev_list= list(reversed(number_list))
        print(rev_list)

    except ValueError:
        print("Please enter correct number")

#day3()

def maxsecondNumb():

    list2=[100, 99, 13, 13, 12, 13, 5, 3, 8, 11,101, 12, 80]
    max_num= secondlast_max= float('-inf')   # starting with lowest possible int value ,-2, -2

    for num in list2:

        if num>max_num:                 #100
            secondlast_max= max_num     #-2
            max_num= num                #100

        elif num>secondlast_max and num !=max_num:
            secondlast_max=num


    if secondlast_max== float('-inf'):
        print("list no second last found")

    print(max_num)
    print(secondlast_max)

# maxsecondNumb()

def find_duplicate():
    numbers = [10, 20, 10, 30, 40, 20, 50, 50, 50]
    list=[]
    single=[]

    for i in  range(0, len(numbers)):
        for j in range(i+1, len(numbers)):

            if numbers[i]==numbers[j] and numbers[i] not in list:
                list.append(numbers[i])

        if numbers[i] not in list:
           single.append(numbers[i])

    print(f" Duplicates number are {list}")
    print(f" single number are {single} ")

#find_duplicate()


def remove_even():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd=[]

    for i in nums:
        if i%2 !=0:
            nums.append(i)

    print(f"list after removing even number {odd}")

#remove_even()


def print_unique():
    data = [1, 2, 2, 3, 4, 4, 5, 6, 1, 7]
    unique = []

    for i in data:
        if i not in unique:
            unique.append(i)

    print(unique)

#print_unique()

#print only odd numbers from 1 to 10, but stop if number reaches 7
# (Use both break and continue)
def pr():
    for i in range(1, 10):
        if i %2 !=0 and i !=7:
            print(i)

        elif i ==7:
            break

#pr()
#Loop through a list of API responses, skip empty responses, but stop entirely if any response is an error.

def alist_resp():
    res_list=  ["ok", "", "ok", "error", "ok"]

    for r in res_list:
        if r=="":
            continue

        if r=="error":
            print("found error ")
            break
        print(f"Processed {r}")

alist_resp()








































