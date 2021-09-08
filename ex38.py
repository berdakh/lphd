# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 19:26:30 2018
@author: Berdakh
"""
#class Thing(object):    
#    def test(message):
#        print(message)
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]
#%%
def pop(more_stuff,ii):
    return more_stuff[-ii]
    
ii = 0
while len(stuff) !=10:
    ii += 1
    print(f"Iteration :{ii}")
    next_one = pop(more_stuff,ii) 
    # pop method remove one item at a time from the list 
   
    print("Adding: ",next_one)    
    stuff.append(next_one) # add one item at a time to the list 
    print(f"There are {len(stuff)} item now.")


print("There we go: ",stuff)
print("Let's do some things with stuff.")
print(stuff[1])
print(stuff[-1])
print(stuff.pop()) # stuff = pop(stuff,~)
print(''.join(stuff)) # what? cool
print('#'.join(stuff[3:5])) # super stellar!