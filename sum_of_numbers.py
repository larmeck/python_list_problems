'''
1. Sum of All Numbers

Write a program that iterates through a list of integers and computes the total sum manually (without using sum()).

'''
import random

random_number_list = []

#iterating over a list of 1000 random numbers
for number in range(1000):
    number=random.randint(1,1000000)
    random_number_list.append(number) 
    #print(random_number_list)
    
    
#function to sum 
def add_numbers(list):
    sum = 0
    for list_number in list:
        sum += list_number
    print(sum)
        


#calling the function       
add_numbers(random_number_list)
