import random
'''
Using a loop, print:
Index: 0, Value: <item>
for each element in a list (do not use enumerate()).

'''

random_list =[]


count = 0

for num in range(1000):
    num = random.randint(1,1000000)
    random_list.append(num)
    count+=1  
    i=0
    for i in range(len(random_list)):
        
        random_list[i] =num
        i+=1
        
    print(f"index: {i} value: {num}")