# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 15:32:22 2018

@author: Berdakh
"""
people = 30
cars = 40
trucks = 15

if cars > people and not(cars): 
    print("we should take the cars.")
elif cars < people:
    print("we should not take the cars.")
else:
    print("we can't decide.")
    

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars: 
    print("Maybe we could take the trucks.")
else:
    print("we still can't decide.")
    
    if people > trucks: 
        print("Alright, let's just take the trucks.")
    else: 
        print("Fine, let's stay home then.")
        
        
        
