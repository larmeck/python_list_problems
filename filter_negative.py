'''
5. Filter Out Negative Numbers

Iterate through the list and build a new list containing only the numbers greater than or equal to zero.
'''
#declaring a list with negative and positive numbers
my_list=[-45,8,6,-3,-81,100,46,-66,38,41]  # can we generate a list using random that contains -ve numbers as well :)

list_non_negative =[]


#get the positive numbers and append them to list_non_negative
def numbers_greater_zero(numbers):
    count = 0
    for num in numbers:
        if num >= 0:
            list_non_negative.append(num)
            count+=1
    return list_non_negative
    
    
print(numbers_greater_zero(my_list))


   
