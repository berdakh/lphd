# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 12:58:52 2018
@author: Berdakh
"""
#mystuff = {'apple':"I am apples!"};
#print(mystuff['apple'])

#!jupyter nbconvert --to python 23.Out-of-core_Learning_Large_Scale_Text_Classification.ipynb

#%% 
class Mystuff(object):
    def __init__(self): # class constructor (initializer)
        self.tangerine = "And now a thousand years between"    
        
    def apple(self): # class method that takes no input variables but only the object itself (SELF)
        print("I am classy apples!")       
    
""" why classes are important than modules? 
    you can take this Mystuff class and use it to craft many of them, millions at a time
    if you want, and each one won't interfere with each other. When you import a module there is
    only one for the entire program unless you do som emonster hacks. 
    ENCAPSULATION.
   
    To create an object (an instance) of a specific class.
"""
#%% dict style
mystuff = {'apples':"I am apples!"};
mystuff['apples']

#%% module style
import mystuff
mystuff.apples()
print(mystuff.tangerine)

#%% class style
from ex40 import Mystuff
thing = Mystuff() # create an instanse of an object 

thing.apple() # look for the method/attribute from thing get apple()
print(thing.tangerine)

#%% Another class definition 
class Song(object):
    
    def __init_(self,lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
#%% 
from ex40 import Song
happy_bday = Song("Happy birthday to you",
                   "I don't want to get sued",
                   "So I will stop right there")            
#%%             
class Inam(object):
    #attributes 
    birth_year = 2008
    birth_month = "July"
    date_of_month = 31
    
    def __init__(self,name = "Inam", lastname = "Abibullaev", age = 9, school = "Astana English School"):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.school = school
    
    def print_name(self):
        """ This function prints the name """
        print("Full Name :", self.name +' '+ self.lastname)
    
    def print_age(self):
        print("Age :",int(self.age)+self.birth_year)
        
#%%
class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999
#%%
date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')        
