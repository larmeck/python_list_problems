import random
'''
2. Count How Many Are Even

Given a list of numbers, iterate through it and count how many are even.
'''

#declaring random numbers list
random_number_list=[]

#appending random numbers to random_number_list
for num in range(1000):
    number=random.randint(1,1000000)
    random_number_list.append(number)
    
#function to count even numbers from a list  
def count_even_numbers(list):
    count = 0
    for even_number in list:
        if even_number %2 ==0:
            count += 1
            
    return count


res = count_even_numbers(random_number_list)
print(f"The total count of 1000 random even numbers from 1-1000000 is: {res}")
    