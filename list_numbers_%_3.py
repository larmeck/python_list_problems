import random


the_list =[]
number = random.randint(1,1000)
count =0

while count < 1000000:
    number = random.randint(1,1000)
    count +=1
    the_list.append(number)




def divisible_by_three(numbers):

    new_list = []

    for x in numbers:
        if x %3 == 0:
            new_list.append(x)
    return new_list



print(divisible_by_three(the_list))
