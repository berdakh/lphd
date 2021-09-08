#%%
def whileloop(numbers, threshold):    
    i = 0
    while i < threshold:
        print(f"At the top i is {i}")
        numbers.append(i) 
        i += 1
        print(f"Numbers now: {numbers}.\n At the bottom i is {i}")        
        if i == 100:
           print('EXITING with BREAK')
           break       
           print('BREAK')           
numbers = []

# call from here
whileloop(numbers,5)

print("The numbers: ")
for num in numbers[0:11]:
    print(num)
    
#%% for-loop implementation 
numbers = []
ii = 0#
t = '...'
for ii in range(0,6):  
    print(f"Appending the list with:>> {ii}\n {t*10}")
    numbers.append(ii) # add this numbers to the empty list 
    print("Numbers now: ", numbers)
    
    if numbers[ii] == len(range(0,5)):
        print(">>><<<"*numbers[ii])        
        print(f"At the bottom i is {numbers[ii]}") 
