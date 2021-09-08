# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 16:48:52 2018
@author: Berdakh
"""
def FirstFactorial(num): 
    # code goes here 
    factorial = [] 
    for i in range(0,num):
        print("inside the foor loop",i)
        factorial.append(i)  
    number = 1
    for j in range(1,len(factorial)+1):
#        print("j is equal >>>", j)
        number = j*1
        print("J*number",number)
    return number

a = FirstFactorial(8)