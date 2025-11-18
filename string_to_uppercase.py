'''
4. Convert All Strings to Uppercase

Given a list of strings, use iteration to produce a new list where each string is uppercase.
'''



user1 = ["Larmeck", "Oduor","larmeckoduor@gmail.com", "Male"]

new_string_upper =[]

count =0
for a_word in user1:
    res = a_word.upper()
    new_string_upper.append(res)
    count+=1
print(new_string_upper)
    
    
