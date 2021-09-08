# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 22:29:21 2018
@author: Berdakh
"""
# referenced data or indexed or?
# referencial data 
#%%
stuff = {'name':'Zed', 'age':39, 'Height':6*12+2}
# dictionary is a data structure that is not number based indexed 
# dict can hold any type of data structure string, array, float 
# list 
print(stuff['name'])
print(stuff['age'])
print(stuff['Height'])

stuff['city']="SF"
stuff[1] = "Wow"
stuff[2] = "Neato"
# "mapping" or "associating" is the key concept in a dictionary
#%%
states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'        
        } 

#%% 
cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
        }
# add some more cities 
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities 
print('-'*10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-'*10)
print("Michigan's abbreviation is: ",states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#%% do it by using the state then cities dict
print('-'*10)
print("Michigan has: ",cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#%%
print('-'*10)
for state, abbrev in list(states.items()):
    # comma separates and assigns values to state and abbrev
    print(f"{state} is abbreviated {abbrev}")
    
#%% print every city in state 
print('-'*10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
    
#%% now do both at the same time 
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
    
#%%
print('-'*20)
# safely get a abbreviation by state that might not be there 
state = states.get('Texas') # if the dict key/value pair does not exit then no Error is raised.

if not state:
    print("Sorry, no Texas.")
#%%    
city = cities.get('TX', 'Does Not Exist')
# if 'TX' does not exist then provide 'Does not exits' message

print(f"The city for the state 'TX' is : {city}")
#  get(...) method of builtins.dict instance
#  D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
#%% 
#a = numpy.random.standard_t(10, size=100000)
#b = list(a)
#stuff['a'] = a
#stuff['b'] = b
#stuff['dictionary'] = stuff
# dictionary is like a cell in matlab even more powerful  

#%% we have list, tuple, dictionary - to organize a data structure 
# in MATLAB you have structure or a dictionary 