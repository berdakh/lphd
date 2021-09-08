# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:59:16 2018

@author: Berdakh
"""
# python bytecode complied language 

#%% closure is an inner function that has an access to the local variables 
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of
# closure makes things a little easier

square = nth_power(2) # this returns - an object squaring 
# __main__.nth_power.<locals>.exponent_of(base)>
cube = nth_power(3) # this object is a cube operator object that still take base input


#%% using closures 1) makes things simpler 2) speeds up your code
def funct(func): # we are passing a function (object) with builtin attributes 
    for i in range(10):
        print(func(i))
        
funct(nth_power(3))
funct(cube) # a simple and readable benefit of using closures 

#%% we could create the same operation with a single function 
def power(exponent, base):
    return base ** exponent
square =  power(2,2) # power == <function __main__.power(exponent, base)>
cube = power(3,2)

#%%
dict_sample = dict(x = 10, y =5) # create a dictionary 
def add(z):
    x = dict_sample['x'] # get the x-key value
    y = dict_sample['y'] # get the y-key value 
    z = z # get the z-key value 
    return x + y + z # do the addition 

# timing 
import time 

start = time.time()
for i in range(1000000):
    x = (add(3))
    
print(time.time() - start) # print the difference between the (start-current_time)

#%% closure function 
def closure_add():
    x = dict_sample['x']
    y = dict_sample['y']
    
    def add(z):
        return x + y + z
    return add 

c_add = closure_add()

start = time.time()
for i in range(1000000):
    _ = (c_add(3)) # _ = (means we don't really care about the values)
print(time.time() - start) # print the difference between the (start-current_time)

#%%  GENERATORS 
def counter(num):
    print("Function starting")
    for i in range(30):
        yield num # generate one at a time - (yield == pause)
        num += 1
        print('Now we are going to update number')

x = counter(3)

#%%
def squares_generator(num):
    while True:
        yield num
        num *= num
# it is like a recursive function where everything can be hard coded however 
# with generator we can iterative freely 
# how many time we want to run the function? 
# this is kind of a useful function using next() method

#%% 
# Scope? (L.E.G.B.) Local. Enclosing. Global. Built_in
# Namespace - a giant list of the all variables we have access to (Dilan, Mohammed, Budda) 
# 
""" 
A namespace is a hash of name, value pairs, a lot like a Python dictionary, 
but where all the keys are valid name strings. When you do an assignment, 
like a = 1, you're mutating a namespace. When you make a reference, 
like print a, Python looks through a list of namespaces to try and 
find one with the name as a key.
A scope defines which namespaces will be looked in and in what order. 
The scope of any reference always starts in the local namespace, and 
moves outwards until it reaches the module's global namespace.
 
If you have a function within a class within a module, and there's 
a reference to a name inside the function, 
Python looks in the function's namespace, then if the name's not there, 
Python looks in the class's namespace, then the module's namespace, 
eventually throwing a NameError if the name isn't found. 
When we say x is in the function's namespace, we mean it is defined there, 
locally within the function. When we say x is in the function's scope, 
we mean x is in the function's namespace or the namespace of the class 
that the function is defined in or the global namespace that the class 
is defined in.
 
Whenever you define a class or function, you create a new namespace 
and a new scope. The namespace is the new, local hash of names. 
The scope is the implied chain of namespaces that starts
at the new namespace, then works its way through 
any outer namespaces (outer scopes), up to the global namespace 
(the global scope).
The terms can be used almost interchangeably, but that's not 
because they mean the same thing; it's because they overlap
a lot in what they imply.
"""