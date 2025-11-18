'''
7. Count Words Longer Than 5 Letters

Given a list of words, use iteration to determine how many have a length greater than 5.
'''

user1 = ["Larmeck", "Oduor","larmeckoduor@gmail.com", "Male"]



def more_than_five(number):
    count = 0
    for num in number:
        if len(num) > 5:
            print(num)
            count +=1
    return count
    
    
print(more_than_five(user1))
        
