import random

'''
3. Find the Maximum Value (without max())

Loop through the list to determine the largest number.
'''
#declaring list of random numbers
list_random_numbers =[]

#iterating through 1000 random numbers from 1-1000000 and appending them to list_random_numbers individually
count = 0
for num in range(1,1000):
    number = random.randint(1,1000000)
    list_random_numbers.append(number)
    count+=1
print(list_random_numbers)


#sorting the list_random numbers
list_random_numbers.sort()
print(list_random_numbers)

#getting the largest number (last item in the sorted list)
max_value = list_random_numbers[-1]
print(f"From the list, the max value is: {max_value}")
