# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 15:52:55 2018

@author: Berdakh
hairs = ['brown', 'blond', 'red']
eyes = ['brown','blue','green']
weights = [1,2,3,4]
"""
#for <variable> in <sequence>:
#	<statements>
#else:
#	<statements>
the_count = [1, 2, 3, 4, 5];
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# this first kinf of for-loop goes through a list 
for number in the_count: # it automatically counts the number of elements 
                         # in a list and loops over it
    print(f"This is count {number}")
# %% Same as above 
for fruit in fruits:
    print(f"A fruit of type: {fruit}")    
# %% also we can go through mixed lists too 
#    notice we have to use {} since we don't know what's in it
for i in change: 
    # for every elements in list change call it i and do print it
    print(f"I got {i}")
    
# %% we can also build lists, first start with an empty one 
elements = [] 
for i in range(0,len(change)): # range is a counter
    print(f"Adding {i} to the list.")
    # append is a function that lists understand 
    elements.append(i)
    
# %%  Now we can print them out too
for i in elements:
    # for each element in elements call it i and do (print)
    print(f"Element was: {i}")     
     
    
    

     