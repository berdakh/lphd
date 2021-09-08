# -*- coding: utf-8 -*-
"""
Created on Thu May  3 10:05:53 2018

@author: Berdakh
"""
# inherit explicitly 
class Parent(object):    
    def implitic(self):
        print("PARENT implitic()")

# child class inherits from the parent 
# the function with implicit()        
        
class Child(Parent):
    pass #an empty block 

#%%
dad = Parent() 
son = Child()
 
dad.implitic()
son.implitic()

#%% override explicitly 
class Parent(object):
    
    def override(self):
        print("PARENT override()")

class Child(Parent):
    
    def override(self):
        print("CHILD override()")
    
    def achildmethod(self):
        print("THIS IS A CHILD method:",5+5)

#%%
# substantiate an instance of a Parent()
# son inherits from Child()
dad = Parent()
son = Child()

# call the method override from the parent class
dad.override()
# call the method override from the inherited child class
# this example shows that .override() funciton overrides the object son method
son.override()

#%% Alter Before or After - a special way of overriding where you want to alter the
# behavior before or after the Parent class's version runs. 
class Parent(object):
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        print("I am calling super(Child,self)")
        super(Child,self).altered() # this calls Parent().altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

#%%
# all three combined - 1) implicite inheritance, 2) explicit override, 3) before and after
class Parent(object):
    # this parent class has three functions/methods 
    param = 1
    def override(self):
        print("PARENT implicit()")
        
    def implicit(self):
        print("PARENT implicit()")
        
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    
    def override(self):
        print("CHILD override()")
        print(self.param)
        
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child,self).altered()
        print("CHILD, AFTER PARENT altered()")
        
#%%
# instantiate a class instance 
dad = Parent()
son = Child()
#%% this example shows that a child object inherits directly from the parent its
# method called .implicit()
dad.implicit()
son.implicit()
print("Parent parameter inherited: ", son.param)

#%% in this example, what is shown is that child object overrides the parent method
# basically, child first inherits then overrides 
dad.override()
# it is similar to function overloading :))) 
# creating a method specific for the object (packaging data and methods-encapsulation)
son.override()

#%% This one is very interesting 
dad.altered()

# this show that 1) overrides the parent method 2) from within the override method
# it is possible to call the Parent().altered() 
# the method super(Child,self).altered() allows us to talk to the parent and envoke 
# the parent method .altered()
son.altered()
# in three words  1) inherit 2) inherit and override, 
# 3) inherit override and call the parent class metod that was overriten 

#%% COMPOSITION vs INHERITANCE EXAMPLE 
# the relationship is like 
# Child has-a Other object not Child is-a relationship

class Other(object):    
    def override(self):
        print("OTHER override()")    
    def implicit(self):
        print("OTHER implicit()")        
    def altered(self):
        print("OTHER altered()")

# another class definition         
class Child(object):    
    def __init__(self): # private method 
        # here, we are just initializing 
        # the attribute of a CHILD object 
        # to a class Other() instead of inheritance 
        self.other = Other()        
    def implicit(self):
        # it is like an inheritance - though it is not
        # it is just instantiated copy of other object in the 
        # initializer 
        self.other.implicit()    
    def override(self):
        print("CHILD override()")        
    def altered(self):
        print("CHILD,BEFORE OTHER altered()")
        self.other.altered() # not inheritance but composition here 
        print("CHILD, AFTER OTHER altered")

#%% 
son =  Child()
son.implicit()     
son.override()
son.altered()

#%% 
    
    
    
    
    
    
    






